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
  const totalRepos = repositories.length;
  const totalCommits = repositories.reduce(
    (sum, r) => sum + (r.total_commits || 0),
    0,
  );
  const languages = [
    ...new Set(repositories.map((r) => r.language).filter(Boolean)),
  ];
  const avgScore =
    repositories.reduce((sum, r) => sum + (r.composite_score || 0), 0) /
    totalRepos;
  const activeRepos = repositories.filter(
    (r) => (r.recent_commits_90d || 0) > 0,
  ).length;

  return (
    <div className="stat-cards-grid">
      <StatCard label="Repositories" value={totalRepos} />
      <StatCard
        label="Total Commits"
        value={totalCommits.toLocaleString()}
        sublabel={`${activeRepos} active in 90d`}
      />
      <StatCard label="Languages" value={languages.length} />
      <StatCard
        label="Avg Spark Score"
        value={avgScore.toFixed(1)}
        sublabel="out of 100"
      />
    </div>
  );
}

StatCards.propTypes = {
  repositories: PropTypes.array.isRequired,
};

export { getLanguageColor, LANGUAGE_COLORS };
