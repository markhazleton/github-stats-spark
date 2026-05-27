import React from "react";
import PropTypes from "prop-types";

const LANGUAGE_COLORS = {
  "C#": "#178600",
  TypeScript: "#3178c6",
  JavaScript: "#f1e05a",
  Python: "#3572A5",
  HTML: "#e34c26",
  CSS: "#563d7c",
  SCSS: "#c6538c",
  PHP: "#4F5D95",
  "Visual Basic .NET": "#945db7",
  Unknown: "#586069",
};

function getLanguageColor(language) {
  return LANGUAGE_COLORS[language] || "#586069";
}

function StatCard({ label, value, sublabel }) {
  return (
    <div className="stat-card">
      <div className="stat-card-value">{value}</div>
      <div className="stat-card-label">{label}</div>
      {sublabel && <div className="stat-card-sublabel">{sublabel}</div>}
    </div>
  );
}

export default function StatCards({ repositories }) {
  const getTotalCommits = (repo) =>
    repo.commit_history?.total_commits || repo.total_commits || 0;

  const getReadmeCoverage = (repo) => (repo.has_readme ? 1 : 0);

  const getOpenPullRequests = (repo) =>
    repo.pull_request_summary?.availability === "available"
      ? repo.pull_request_summary.total_open || 0
      : 0;

  const getOpenSecurityAlerts = (repo) =>
    repo.security_summary?.availability === "available"
      ? repo.security_summary.active_alert_counts?.total_open || 0
      : 0;

  const totalRepos = repositories.length;
  const totalCommits = repositories.reduce(
    (sum, r) => sum + getTotalCommits(r),
    0,
  );
  const languages = [
    ...new Set(repositories.map((r) => r.language).filter(Boolean)),
  ];
  const avgReadmeQuality =
    totalRepos > 0
      ? (repositories.reduce((sum, r) => sum + getReadmeCoverage(r), 0) /
          totalRepos) *
        100
      : 0;
  const activeRepos = repositories.filter(
    (r) => (r.days_since_last_push ?? 999) <= 30,
  ).length;

  const totalOpenPullRequests = repositories.reduce(
    (sum, r) => sum + getOpenPullRequests(r),
    0,
  );
  const reposWithOpenPullRequests = repositories.filter(
    (r) => getOpenPullRequests(r) > 0,
  ).length;

  const totalSecurityAlerts = repositories.reduce(
    (sum, r) => sum + getOpenSecurityAlerts(r),
    0,
  );
  const reposWithSecurityAlerts = repositories.filter(
    (r) => getOpenSecurityAlerts(r) > 0,
  ).length;

  const unavailableSecurityData = repositories.filter(
    (r) => r.security_summary?.availability !== "available",
  ).length;

  return (
    <div className="stat-cards-grid">
      <StatCard label="Repositories" value={totalRepos} />
      <StatCard
        label="Total Commits"
        value={totalCommits.toLocaleString()}
        sublabel={`${activeRepos} active in 30d`}
      />
      <StatCard label="Languages" value={languages.length} />
      <StatCard
        label="README Coverage"
        value={avgReadmeQuality.toFixed(0)}
        sublabel={`${activeRepos} active in 30d`}
      />
      <StatCard
        label="Open Pull Requests"
        value={totalOpenPullRequests.toLocaleString()}
        sublabel={`${reposWithOpenPullRequests} repos with open PRs`}
      />
      <StatCard
        label="Security Alerts"
        value={totalSecurityAlerts.toLocaleString()}
        sublabel={
          unavailableSecurityData > 0
            ? `${reposWithSecurityAlerts} repos with alerts • ${unavailableSecurityData} unavailable`
            : `${reposWithSecurityAlerts} repos with alerts`
        }
      />
    </div>
  );
}

StatCards.propTypes = {
  repositories: PropTypes.array.isRequired,
};

export { getLanguageColor, LANGUAGE_COLORS };
