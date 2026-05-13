import React from "react";
import Tooltip from "@/components/Common/Tooltip";
import styles from "./RepositoryTable.module.css";

const TableRow = React.memo(function TableRow({ repository, onClick }) {
  const formatDate = (dateString) => {
    if (!dateString) return "N/A";
    try {
      const date = new Date(dateString);
      if (isNaN(date.getTime())) return "N/A";
      return date.toLocaleDateString("en-US", {
        year: "numeric",
        month: "short",
        day: "numeric",
      });
    } catch {
      return "N/A";
    }
  };

  const handleRowClick = (e) => {
    if (e.target.tagName === "A") return;
    if (onClick) onClick(repository);
  };

  const language = repository.language || "Unknown";
  const totalCommits = repository.total_commits || 0;
  const pullRequestSummary = repository.pull_request_summary || {};
  const securitySummary = repository.security_summary || {};
  const securityAlerts = securitySummary.active_alert_counts?.total_open || 0;
  const openPullRequests =
    pullRequestSummary.availability === "available"
      ? pullRequestSummary.total_open || 0
      : repository.open_prs || 0;

  const pullRequestLabel =
    pullRequestSummary.availability === "available"
      ? `PR ${openPullRequests}`
      : repository.open_prs != null
        ? `PR ${repository.open_prs}`
        : "PR n/a";

  const securityUnavailable =
    securitySummary.availability !== "available" &&
    securitySummary.availability !== "partial";

  let securityLabel = "SEC n/a";
  if (!securityUnavailable) {
    securityLabel = securityAlerts > 0 ? `SEC ${securityAlerts}` : "SEC clear";
  }

  const readmeScore = repository.readme_quality_score;
  const releaseCount = repository.release_count ?? 0;

  return (
    <tr className={styles.tableRow} onClick={handleRowClick} role="row">
      <td className={styles.tableCell}>
        <div className={styles.tableCellContent}>
          <button
            className={styles.repoNameButton}
            onClick={() => onClick && onClick(repository)}
            title={`View details for ${repository.name}`}
          >
            {repository.name}
          </button>
        </div>
      </td>

      <td className={styles.tableCell}>
        <span
          className={`${styles.badge} ${styles[`badge--${language.toLowerCase()}`]}`}
        >
          {language}
        </span>
      </td>

      <td className={styles.tableCell}>
        <div className={styles.signalGroup}>
          <span
            className={`${styles.signalPill} ${
              pullRequestSummary.availability !== "available" &&
              repository.open_prs == null
                ? styles.signalPillMuted
                : openPullRequests > 0
                  ? styles.signalPillWarning
                  : styles.signalPillSuccess
            }`}
            title="Open pull requests"
          >
            {pullRequestLabel}
          </span>
          <span
            className={`${styles.signalPill} ${
              securityUnavailable
                ? styles.signalPillMuted
                : securityAlerts > 0
                  ? styles.signalPillError
                  : styles.signalPillSuccess
            }`}
            title="Open security alerts"
          >
            {securityLabel}
          </span>
        </div>
      </td>

      <td className={styles.tableCell}>{formatDate(repository.pushed_at)}</td>

      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        {totalCommits.toLocaleString()}
      </td>

      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="GitHub stars">
          {repository.stars?.toLocaleString() || 0}
        </Tooltip>
      </td>

      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="README quality score (0–100)">
          {readmeScore != null ? readmeScore : "N/A"}
        </Tooltip>
      </td>

      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="Number of published releases">
          {releaseCount}
        </Tooltip>
      </td>
    </tr>
  );
});

export default TableRow;
