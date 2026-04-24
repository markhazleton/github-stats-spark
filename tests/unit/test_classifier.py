"""Unit tests for RepositoryClassifier (portfolio intelligence engine)."""

import pytest
from spark.classifier import ClassificationResult, RepositoryClassifier


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _clf(overrides=None):
    return RepositoryClassifier(overrides=overrides or {})


# ---------------------------------------------------------------------------
# Automated classification threshold boundaries
# ---------------------------------------------------------------------------

class TestAutomatedTier:
    def test_core_exact_boundary(self):
        clf = _clf()
        result = clf.classify("repo", commits_90d=5, days_since_push=90, has_tests=False, has_ci_cd=True)
        assert result.classification == "core"

    def test_core_all_three_factors_required(self):
        clf = _clf()
        # Fails quality check (no tests, no CI) → not Core
        result = clf.classify("repo", commits_90d=10, days_since_push=30, has_tests=False, has_ci_cd=False)
        assert result.classification == "supporting"

    def test_core_requires_min_commits(self):
        clf = _clf()
        # Only 4 commits — below threshold of 5
        result = clf.classify("repo", commits_90d=4, days_since_push=30, has_tests=True, has_ci_cd=False)
        assert result.classification == "supporting"

    def test_core_pushed_at_boundary_fail(self):
        clf = _clf()
        # 91 days ago — just outside Core window
        result = clf.classify("repo", commits_90d=10, days_since_push=91, has_tests=True, has_ci_cd=True)
        assert result.classification == "supporting"

    def test_supporting_by_recency(self):
        clf = _clf()
        result = clf.classify("repo", commits_90d=0, days_since_push=364, has_tests=False, has_ci_cd=False)
        assert result.classification == "supporting"

    def test_supporting_by_commit(self):
        clf = _clf()
        # Old push but 1 commit in 90d
        result = clf.classify("repo", commits_90d=1, days_since_push=400, has_tests=False, has_ci_cd=False)
        assert result.classification == "supporting"

    def test_archive_fallback(self):
        clf = _clf()
        result = clf.classify("repo", commits_90d=0, days_since_push=400, has_tests=False, has_ci_cd=False)
        assert result.classification == "archive"

    def test_brand_new_repo_no_commits(self):
        clf = _clf()
        # Pushed today but zero commits somehow — Supporting by recency
        result = clf.classify("repo", commits_90d=0, days_since_push=0, has_tests=False, has_ci_cd=False)
        assert result.classification == "supporting"


# ---------------------------------------------------------------------------
# Config override priority
# ---------------------------------------------------------------------------

class TestConfigOverride:
    def test_named_override_beats_automated_core(self):
        clf = _clf({"devspark": "core"})
        # Would be Archive without override
        result = clf.classify("devspark", commits_90d=0, days_since_push=500, has_tests=False, has_ci_cd=False)
        assert result.classification == "core"
        assert result.relevance == "high"

    def test_named_override_archive_beats_automated_core(self):
        clf = _clf({"active-repo": "archive"})
        # Would be Core without override
        result = clf.classify("active-repo", commits_90d=20, days_since_push=10, has_tests=True, has_ci_cd=True)
        assert result.classification == "archive"

    def test_named_override_supporting(self):
        clf = _clf({"BootstrapSpark": "supporting"})
        result = clf.classify("BootstrapSpark", commits_90d=0, days_since_push=500, has_tests=False, has_ci_cd=False)
        assert result.classification == "supporting"

    def test_wildcard_default_applies_to_unspecified_archive(self):
        clf = _clf({"*": "archive"})
        result = clf.classify("unknown-repo", commits_90d=0, days_since_push=400, has_tests=False, has_ci_cd=False)
        assert result.classification == "archive"

    def test_wildcard_does_not_override_named_entry(self):
        clf = _clf({"devspark": "core", "*": "archive"})
        result = clf.classify("devspark", commits_90d=0, days_since_push=500, has_tests=False, has_ci_cd=False)
        assert result.classification == "core"

    def test_wildcard_does_not_downgrade_automated_core(self):
        # Wildcard only applies when automated result is archive
        clf = _clf({"*": "archive"})
        result = clf.classify("hot-repo", commits_90d=10, days_since_push=30, has_tests=True, has_ci_cd=True)
        assert result.classification == "core"

    def test_empty_overrides_uses_automated(self):
        clf = _clf({})
        result = clf.classify("repo", commits_90d=10, days_since_push=30, has_tests=True, has_ci_cd=True)
        assert result.classification == "core"


# ---------------------------------------------------------------------------
# Signal score formula
# ---------------------------------------------------------------------------

class TestSignalScore:
    def test_perfect_core_score(self):
        # pushed today, 30+ commits, Core tier
        score = RepositoryClassifier.compute_signal_score(0, 30, "core")
        assert score == round((100 + 100 + 100) / 3)  # 100

    def test_archive_zero_activity(self):
        # pushed 365+ days ago, 0 commits, Archive
        score = RepositoryClassifier.compute_signal_score(365, 0, "archive")
        assert score == round((0 + 0 + 20) / 3)  # 7

    def test_recency_boundary_365d(self):
        score = RepositoryClassifier.compute_signal_score(365, 0, "archive")
        assert score == round((0 + 0 + 20) / 3)

    def test_volume_ceiling_at_30_commits(self):
        score_30 = RepositoryClassifier.compute_signal_score(0, 30, "core")
        score_60 = RepositoryClassifier.compute_signal_score(0, 60, "core")
        assert score_30 == score_60  # volume capped at 100

    def test_supporting_mid_range(self):
        # pushed 180d ago, 3 commits, Supporting
        recency = max(0, 100 - 180 / 365 * 100)
        volume = min(100, 3 / 30 * 100)
        expected = round((recency + volume + 60) / 3)
        assert RepositoryClassifier.compute_signal_score(180, 3, "supporting") == expected

    def test_score_clamped_non_negative(self):
        score = RepositoryClassifier.compute_signal_score(1000, 0, "archive")
        assert score >= 0

    def test_score_max_100(self):
        score = RepositoryClassifier.compute_signal_score(0, 100, "core")
        assert score <= 100


# ---------------------------------------------------------------------------
# Notes generation
# ---------------------------------------------------------------------------

class TestGenerateNotes:
    def test_override_notes_returned_verbatim(self):
        notes = RepositoryClassifier.generate_notes("archive", 0, "Custom note here")
        assert notes == "Custom note here"

    def test_core_high_activity(self):
        notes = RepositoryClassifier.generate_notes("core", 15)
        assert "15 commits" in notes
        assert "90 days" in notes

    def test_core_low_activity(self):
        notes = RepositoryClassifier.generate_notes("core", 3)
        assert "focused" in notes.lower()

    def test_supporting_with_commits(self):
        notes = RepositoryClassifier.generate_notes("supporting", 2)
        assert "recent" in notes.lower()

    def test_supporting_no_commits(self):
        notes = RepositoryClassifier.generate_notes("supporting", 0)
        assert "periodically" in notes.lower()

    def test_archive(self):
        notes = RepositoryClassifier.generate_notes("archive", 0)
        assert "historical" in notes.lower()

    def test_notes_always_non_empty(self):
        for tier in ("core", "supporting", "archive"):
            for commits in (0, 5, 15):
                assert RepositoryClassifier.generate_notes(tier, commits)


# ---------------------------------------------------------------------------
# Relevance derivation
# ---------------------------------------------------------------------------

class TestRelevance:
    @pytest.mark.parametrize("tier,expected", [
        ("core", "high"),
        ("supporting", "medium"),
        ("archive", "low"),
    ])
    def test_relevance_matches_tier(self, tier, expected):
        clf = _clf({})
        result = clf.classify("repo", commits_90d=0, days_since_push=500,
                               has_tests=False, has_ci_cd=False)
        # Force tier via override for determinism
        clf2 = _clf({"repo": tier})
        r = clf2.classify("repo", commits_90d=0, days_since_push=500,
                          has_tests=False, has_ci_cd=False)
        assert r.relevance == expected


# ---------------------------------------------------------------------------
# classify_repo_dict integration
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# T018 acceptance scenario (US2): config override beats automated rule
# ---------------------------------------------------------------------------

class TestUS2Acceptance:
    def test_config_override_core_beats_archive_rule(self):
        """Given override {"devspark": "core"} + repo that would be Archive,
        classification must be "core" and relevance "high"."""
        clf = _clf({"devspark": "core"})
        result = clf.classify(
            "devspark",
            commits_90d=0,
            days_since_push=500,  # would be Archive
            has_tests=False,
            has_ci_cd=False,
        )
        assert result.classification == "core"
        assert result.relevance == "high"
        assert result.signal_score > 0

    def test_config_override_archive_beats_core_rule(self):
        clf = _clf({"hot-repo": "archive"})
        result = clf.classify(
            "hot-repo",
            commits_90d=20,
            days_since_push=5,  # would be Core
            has_tests=True,
            has_ci_cd=True,
        )
        assert result.classification == "archive"
        assert result.relevance == "low"


class TestClassifyRepoDict:
    def test_basic_dict(self):
        clf = _clf({"myrepo": "core"})
        repo_dict = {
            "name": "myrepo",
            "recent_commits_90d": 0,
            "days_since_last_push": 500,
            "has_tests": False,
            "has_ci_cd": False,
        }
        result = clf.classify_repo_dict(repo_dict)
        assert result.classification == "core"

    def test_missing_fields_default_to_zero(self):
        clf = _clf()
        result = clf.classify_repo_dict({"name": "repo"})
        assert result.classification in ("core", "supporting", "archive")
        assert 0 <= result.signal_score <= 100
        assert result.notes
