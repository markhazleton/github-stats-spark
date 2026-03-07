"""Regression coverage for dashboard generator profile aggregation."""

from spark.dashboard_generator import DashboardGenerator


class StubFetcher:
    """Simple fetcher stub for dashboard tests."""

    def get_user(self):
        return {
            "login": "markhazleton",
            "avatar_url": "https://example.com/avatar.png",
            "public_repos": 2,
            "html_url": "https://github.com/markhazleton",
        }


def test_generate_user_profile_aggregates_included_repository_totals(dashboard_repositories):
    generator = DashboardGenerator({"dashboard": {"enabled": True}}, "markhazleton")
    generator.fetcher = StubFetcher()

    profile = generator.generate_user_profile(dashboard_repositories)

    assert profile.total_commits == 20
    assert profile.total_stars == 12
    assert profile.total_forks == 5


def test_generate_uses_repository_set_for_profile_totals(monkeypatch, dashboard_repositories):
    generator = DashboardGenerator({"dashboard": {"enabled": True}}, "markhazleton")
    generator.fetcher = StubFetcher()
    monkeypatch.setattr(generator, "generate_dashboard_data", lambda: dashboard_repositories)

    dashboard_data = generator.generate()

    assert dashboard_data.metadata.repository_count == 2
    assert dashboard_data.profile.total_stars == 12
    assert dashboard_data.profile.total_forks == 5