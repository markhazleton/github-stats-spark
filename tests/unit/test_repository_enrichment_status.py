"""Unit tests for repository enrichment status model behavior."""

from datetime import datetime, timezone

from spark.models.repository import Repository, RepositoryPullRequestSummary, RepositorySecuritySummary


def test_repository_pull_request_summary_defaults_round_trip():
    summary = RepositoryPullRequestSummary()
    payload = summary.to_dict()
    restored = RepositoryPullRequestSummary.from_dict(payload)

    assert restored.availability == "unavailable"
    assert restored.reason == "not_requested"
    assert restored.total_open == 0


def test_repository_security_summary_defaults_round_trip():
    summary = RepositorySecuritySummary()
    payload = summary.to_dict()
    restored = RepositorySecuritySummary.from_dict(payload)

    assert restored.availability == "unavailable"
    assert restored.overall_state == "unavailable"
    assert restored.active_alert_counts["total_open"] == 0


def test_repository_from_dict_preserves_enrichment_objects():
    repo = Repository.from_dict(
        {
            "name": "sample",
            "url": "https://github.com/markhazleton/sample",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "is_private": False,
            "pull_request_summary": {
                "availability": "available",
                "reason": "none",
                "has_open_pull_requests": True,
                "total_open": 1,
                "draft_count": 0,
                "review_requested_count": 1,
                "oldest_open_age_days": 5,
                "source": "rest.pulls.list",
            },
            "security_summary": {
                "availability": "partial",
                "reason": "permission_denied",
                "overall_state": "warning_present",
                "feature_status": {
                    "advanced_security": "unavailable",
                    "secret_scanning": "unavailable",
                    "secret_scanning_push_protection": "unavailable",
                    "dependency_alerts": "enabled",
                    "automated_security_fixes": "enabled",
                },
                "active_alert_counts": {
                    "total_open": 2,
                    "critical": 1,
                    "high": 1,
                    "medium": 0,
                    "low": 0,
                },
                "sources": ["rest.dependabot.alerts"],
            },
        }
    )

    assert repo.pull_request_summary.total_open == 1
    assert repo.security_summary.availability == "partial"
    assert repo.to_dict()["security_summary"]["active_alert_counts"]["critical"] == 1
