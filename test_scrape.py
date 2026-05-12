"""Full pipeline: generate LLM summaries + build repositories.json."""
import time
from spark.config import SparkConfig
from spark.cache import APICache
from spark.fetcher import GitHubFetcher
from spark.repo_detail_builder import write_repo_details
from spark.repo_summary_pipeline import generate_summaries, build_repositories_json

config = SparkConfig("config/spark.yml")
config.load()
cache = APICache(cache_dir=config.get_cache_dir())
fetcher = GitHubFetcher(cache=cache, max_repos=500, api_version_settings=config.get_github_api_version_config())

username = "markhazleton"
detail_dir = f"data/users/{username}/repos"

print("=" * 70)
print(f"FULL PIPELINE: LLM Summaries + repositories.json")
print("=" * 70)

# Step 1: Load repos
t0 = time.time()
repos = fetcher.fetch_repositories(username, exclude_private=True, exclude_forks=True, exclude_archived=True)
print(f"\n[Step 1] Loaded {len(repos)} repos ({time.time() - t0:.2f}s)")

# Step 2: Ensure detail files exist
t1 = time.time()
write_repo_details(cache, username, repos, output_dir=detail_dir)
print(f"\n[Step 2] Detail files written ({time.time() - t1:.2f}s)")

# Step 3: Generate LLM summaries
print(f"\n[Step 3] Generating LLM summaries...")
t2 = time.time()
summaries = generate_summaries(detail_dir, cache, username)
t2_elapsed = time.time() - t2
print(f"  Elapsed: {t2_elapsed:.1f}s")

# Step 4: Build repositories.json
print(f"\n[Step 4] Building repositories.json...")
t3 = time.time()
output_file = build_repositories_json(repos, detail_dir, summaries, username)
print(f"  Done ({time.time() - t3:.2f}s)")

# Summary
total = time.time() - t0
print(f"\n{'=' * 70}")
print(f"PIPELINE COMPLETE")
print(f"  Total time:     {total:.1f}s")
print(f"  Repos:          {len(repos)}")
print(f"  Summaries:      {sum(1 for v in summaries.values() if v)}/{len(repos)}")
print(f"  Output:         {output_file}")
print(f"{'=' * 70}")

# Show a sample summary
for name, s in list(summaries.items())[:3]:
    if s:
        print(f"\n  [{name}]")
        print(f"    {s.get('summary', '?')}")
        print(f"    Purpose: {s.get('purpose', '?')}")
        print(f"    Tech: {s.get('tech_highlights', [])}")
        print(f"    Maturity: {s.get('project_maturity', '?')}")
