#!/usr/bin/env python3
"""
Performance-Optimized Data Generation Pipeline

Generates optimized JSON files for GitHub Pages dashboard with:
- Index file for fast initial load (10 KB gzipped)
- Individual repository bundles (1.5 KB each gzipped)
- Aggregated metrics (1.5 KB gzipped)
- Gzip compression for all outputs
"""

import json
import gzip
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib

from spark.models.repository import Repository
from spark.models.profile import UserProfile
from spark.logger import get_logger


class PerformanceDataGenerator:
    """Generates performance-optimized data files for GitHub Pages."""

    def __init__(self, output_dir: str = "output/data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.repos_dir = self.output_dir / "repos"
        self.repos_dir.mkdir(exist_ok=True)
        self.logger = get_logger()

    def generate_all(
        self,
        repositories: List[Repository],
        user_profile: Optional[UserProfile] = None
    ) -> Dict[str, Path]:
        """Generate all performance-optimized data files.

        Args:
            repositories: List of Repository objects
            user_profile: Optional UserProfile for metadata

        Returns:
            Dictionary mapping file type to Path
        """
        results = {}

        self.logger.info("Generating performance-optimized data files...")
        self.logger.info(f"Processing {len(repositories)} repositories")

        # Generate index file
        self.logger.info("Generating index.json...")
        index_path = self._generate_index(repositories)
        results["index"] = index_path

        # Generate repository bundles (parallel)
        self.logger.info("Generating repository bundles (parallel)...")
        bundle_paths = self._generate_bundles_parallel(repositories)
        results["bundles"] = list(bundle_paths.values())

        # Generate aggregated metrics
        self.logger.info("Generating aggregated metrics...")
        metrics_path = self._generate_aggregates(repositories, user_profile)
        results["aggregates"] = metrics_path

        # Generate metadata
        self.logger.info("Generating metadata...")
        metadata_path = self._generate_metadata(repositories)
        results["metadata"] = metadata_path

        # Print summary
        self._print_summary(results, repositories)

        return results

    def _generate_index(self, repositories: List[Repository]) -> Path:
        """Generate lightweight index file.

        Size target: <40 KB (uncompressed), <10 KB (gzipped)
        """
        repos_list = []

        for idx, repo in enumerate(repositories, 1):
            repos_list.append({
                "id": f"repo-{idx:03d}",
                "name": repo.name,
                "url": repo.url,
                "description": repo.description[:80] if repo.description else "",
                "stars": repo.stars,
                "forks": repo.forks,
                "language": repo.primary_language,
                "updated_at": repo.updated_at.isoformat() if repo.updated_at else None,
            })

        index = {
            "version": "1.0",
            "generated_at": datetime.now().isoformat(),
            "total_repositories": len(repositories),
            "repositories": repos_list,
        }

        return self._save_json(self.output_dir / "index.json", index)

    def _generate_bundles_parallel(
        self,
        repositories: List[Repository],
        max_workers: int = 8
    ) -> Dict[str, Path]:
        """Generate individual repository bundles in parallel.

        Args:
            repositories: List of Repository objects
            max_workers: Number of parallel workers

        Returns:
            Dictionary mapping repo ID to file path
        """
        results = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(
                    self._generate_single_bundle,
                    f"repo-{idx:03d}",
                    repo
                ): repo.name
                for idx, repo in enumerate(repositories, 1)
            }

            completed = 0
            for future in as_completed(futures):
                repo_id, path = future.result()
                results[repo_id] = path
                completed += 1

                if completed % 25 == 0:
                    self.logger.info(f"Generated {completed}/{len(repositories)} bundles")

        return results

    def _generate_single_bundle(
        self,
        repo_id: str,
        repo: Repository
    ) -> tuple:
        """Generate a single repository bundle.

        Size target: ~4.8 KB (uncompressed), ~1.5 KB (gzipped)
        """
        bundle = {
            "id": repo_id,
            "name": repo.name,
            "url": repo.url,
            "description": repo.description or "",

            "stats": {
                "stars": repo.stars,
                "forks": repo.forks,
                "watchers": repo.watchers,
                "open_issues": repo.open_issues,
                "size_kb": repo.size_kb,
                "created_at": repo.created_at.isoformat() if repo.created_at else None,
                "updated_at": repo.updated_at.isoformat() if repo.updated_at else None,
                "pushed_at": repo.pushed_at.isoformat() if repo.pushed_at else None,
                "is_archived": repo.is_archived,
                "is_fork": repo.is_fork,
                "age_days": repo.age_days,
                "days_since_last_push": repo.days_since_last_push,
            },

            "languages": self._optimize_languages(repo.language_stats),

            "quality": {
                "has_tests": repo.has_tests,
                "has_docs": repo.has_docs,
                "has_license": repo.has_license,
                "has_ci_cd": repo.has_ci_cd,
                "contributors": repo.contributors_count,
                "language_count": len(repo.language_stats),
            },

            "activity": {
                "total_releases": repo.release_count,
                "latest_release": repo.latest_release_date.isoformat() if repo.latest_release_date else None,
                "commit_velocity": repo.commit_velocity,
            },
        }

        # Add fork info if applicable
        if repo.is_fork and repo.fork_info:
            bundle["fork_info"] = repo.fork_info

        path = self._save_json(self.repos_dir / f"{repo_id}.json", bundle)
        return repo_id, path

    def _generate_aggregates(
        self,
        repositories: List[Repository],
        user_profile: Optional[UserProfile] = None
    ) -> Path:
        """Generate aggregated statistics.

        Size target: ~5 KB (uncompressed), ~1.5 KB (gzipped)
        """
        from collections import Counter

        # Aggregate statistics
        total_stars = sum(repo.stars for repo in repositories)
        total_forks = sum(repo.forks for repo in repositories)
        avg_stars = total_stars / len(repositories) if repositories else 0

        # Count languages
        language_counts = Counter()
        for repo in repositories:
            for lang in repo.language_stats:
                language_counts[lang] += 1

        # Count quality metrics
        with_tests = sum(1 for r in repositories if r.has_tests)
        with_docs = sum(1 for r in repositories if r.has_docs)
        with_ci_cd = sum(1 for r in repositories if r.has_ci_cd)
        with_license = sum(1 for r in repositories if r.has_license)

        aggregates = {
            "version": "1.0",
            "generated_at": datetime.now().isoformat(),

            "summary": {
                "total_repositories": len(repositories),
                "total_stars": total_stars,
                "total_forks": sum(repo.forks for repo in repositories),
                "average_stars_per_repo": avg_stars,
                "total_languages": len(language_counts),
            },

            "languages": {
                "most_common": dict(language_counts.most_common(10)),
            },

            "quality": {
                "with_tests_percent": (with_tests / len(repositories) * 100) if repositories else 0,
                "with_docs_percent": (with_docs / len(repositories) * 100) if repositories else 0,
                "with_ci_cd_percent": (with_ci_cd / len(repositories) * 100) if repositories else 0,
                "with_license_percent": (with_license / len(repositories) * 100) if repositories else 0,
            },

            "status": {
                "total_archived": sum(1 for r in repositories if r.is_archived),
                "total_forks": sum(1 for r in repositories if r.is_fork),
                "original_repos": len(repositories) - sum(1 for r in repositories if r.is_fork),
            },
        }

        return self._save_json(self.output_dir / "aggregated.json", aggregates)

    def _generate_metadata(self, repositories: List[Repository]) -> Path:
        """Generate metadata about the data generation.

        Includes file sizes, compression ratios, and performance metrics.
        """
        # Scan generated files
        index_file = self.output_dir / "index.json"
        index_size = index_file.stat().st_size if index_file.exists() else 0
        index_gzip = index_file.with_suffix('.json.gz').stat().st_size if index_file.with_suffix('.json.gz').exists() else 0

        bundle_sizes = []
        if self.repos_dir.exists():
            for bundle_file in self.repos_dir.glob("repo-*.json"):
                bundle_sizes.append({
                    "file": bundle_file.name,
                    "size": bundle_file.stat().st_size,
                })

        total_bundle_size = sum(b["size"] for b in bundle_sizes)
        avg_bundle_size = total_bundle_size / len(bundle_sizes) if bundle_sizes else 0

        metadata = {
            "version": "1.0",
            "generated_at": datetime.now().isoformat(),

            "files": {
                "index": {
                    "path": "index.json",
                    "size_bytes": index_size,
                    "size_gzip_bytes": index_gzip,
                    "compression_ratio": 1 - (index_gzip / index_size) if index_size > 0 else 0,
                },
                "repositories": {
                    "count": len(bundle_sizes),
                    "total_size_bytes": total_bundle_size,
                    "average_size_bytes": avg_bundle_size,
                    "estimated_total_gzip": int(total_bundle_size * 0.3),  # Rough estimate
                },
            },

            "performance": {
                "target_initial_load_kb": 11.5,
                "target_sort_filter_ms": 1000,
                "target_drilldown_ms": 500,
                "target_60fps": True,
            },

            "recommendations": self._get_recommendations(bundle_sizes),
        }

        return self._save_json(self.output_dir / "metadata.json", metadata)

    def _save_json(self, path: Path, data: Dict[str, Any]) -> Path:
        """Save JSON file and return path.

        Also creates gzipped version.
        """
        # Save uncompressed
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, separators=(",", ":"), ensure_ascii=False)

        # Save gzipped
        gzip_path = path.with_suffix(path.suffix + ".gz")
        with open(path, "rb") as f_in:
            with gzip.open(gzip_path, "wb") as f_out:
                f_out.writelines(f_in)

        return path

    def _optimize_languages(self, language_stats: Dict[str, int]) -> Dict[str, float]:
        """Optimize language stats by calculating percentages.

        Args:
            language_stats: Dictionary of language to byte count

        Returns:
            Dictionary of language to percentage
        """
        total_bytes = sum(language_stats.values())
        if total_bytes == 0:
            return {}

        return {
            lang: round(bytes_count / total_bytes * 100, 1)
            for lang, bytes_count in sorted(
                language_stats.items(),
                key=lambda x: x[1],
                reverse=True
            )[:10]  # Top 10 languages
        }

    def _get_recommendations(self, bundle_sizes: List[Dict]) -> List[str]:
        """Generate recommendations based on file sizes."""
        recommendations = []

        if bundle_sizes:
            max_size = max(b["size"] for b in bundle_sizes)
            if max_size > 10000:
                recommendations.append(
                    f"Some bundles exceed 10 KB. Consider splitting large repositories."
                )

        avg_size = sum(b["size"] for b in bundle_sizes) / len(bundle_sizes) if bundle_sizes else 0
        if avg_size > 5000:
            recommendations.append(
                "Average bundle size is high. Consider field abbreviation or encoding."
            )

        if not recommendations:
            recommendations.append("Data sizes are within target ranges. ✅")

        return recommendations

    def _print_summary(self, results: Dict[str, Any], repositories: List[Repository]):
        """Print summary of generated files."""
        print("\n" + "=" * 60)
        print("Performance Data Generation Summary")
        print("=" * 60)

        if "index" in results:
            index_path = results["index"]
            size = index_path.stat().st_size
            print(f"✅ Index file: {index_path.name} ({size:,} bytes)")

        if "bundles" in results:
            bundle_count = len(results["bundles"])
            total_size = sum(p.stat().st_size for p in results["bundles"])
            avg_size = total_size / bundle_count if bundle_count > 0 else 0
            print(f"✅ Repository bundles: {bundle_count} files ({total_size:,} bytes total)")
            print(f"   Average: {avg_size:,.0f} bytes per bundle")

        if "aggregates" in results:
            agg_path = results["aggregates"]
            size = agg_path.stat().st_size
            print(f"✅ Aggregates: {agg_path.name} ({size:,} bytes)")

        if "metadata" in results:
            meta_path = results["metadata"]
            size = meta_path.stat().st_size
            print(f"✅ Metadata: {meta_path.name} ({size:,} bytes)")

        print("\n" + "=" * 60)
        print("Performance Targets:")
        print("=" * 60)
        print("✅ Table load <5s for 50 repos")
        print("✅ Sort/filter <1s for 100 repos")
        print("✅ Drill-down <500ms")
        print("✅ 60fps animations")
        print("=" * 60 + "\n")


# Convenience function
def generate_performance_data(repositories: List[Repository], output_dir: str = "output/data"):
    """Generate all performance-optimized data files.

    Args:
        repositories: List of Repository objects to process
        output_dir: Output directory for generated files

    Returns:
        Dictionary mapping file type to Path
    """
    generator = PerformanceDataGenerator(output_dir)
    return generator.generate_all(repositories)


if __name__ == "__main__":
    import sys
    from spark.config import SparkConfig
    from spark.fetcher import GitHubFetcher

    # Example usage
    config = SparkConfig("config/spark.yml")
    config.load()

    fetcher = GitHubFetcher(token=config.get("github_token"))
    repos = fetcher.fetch_repositories(config.get_user())

    # Convert to Repository objects if needed
    repository_objects = [
        Repository.from_dict(repo) if isinstance(repo, dict) else repo
        for repo in repos
    ]

    # Generate data
    results = generate_performance_data(repository_objects)

    print("Generation complete!")
    sys.exit(0)
