import React from "react";
import Tooltip from "@/components/Common/Tooltip";
import styles from "./RepositoryTable.module.css";

/**
 * TableRow Component
 *
 * Renders a single repository row with all metrics.
 * Handles formatting, edge cases (missing data), and user interactions.
 * Optimized with React.memo for performance with 100+ rows.
 *
 * @component
 * @param {Object} props - Component props
 * @param {Object} props.repository - Repository object with metrics
 * @param {Function} [props.onClick] - Callback when row is clicked for drill-down
 *
 * @example
 * <TableRow
 *   repository={repo}
 *   onClick={(repo) => showDetails(repo)}
 * />
 */
const TableRow = React.memo(function TableRow({ repository, onClick }) {
  /**
   * Format date to readable string (MM/DD/YYYY)
   */
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

  /**
   * Handle row click (for drill-down)
   */
  const handleRowClick = (e) => {
    // Don't trigger if clicking link
    if (e.target.tagName === "A") {
      return;
    }

    if (onClick) {
      onClick(repository);
    }
  };

  const language = repository.language || "Unknown";

  // Extract commit data from nested structure (unified data format)
  const commitHistory = repository.commit_history || {};
  const totalCommits =
    commitHistory.total_commits || repository.commit_count || 0;
  const firstCommitDate =
    commitHistory.first_commit_date || repository.first_commit_date;
  const lastCommitDate =
    commitHistory.last_commit_date || repository.last_commit_date;
  const pullRequestSummary = repository.pull_request_summary || {};
  const securitySummary = repository.security_summary || {};
  const securityAlerts = securitySummary.active_alert_counts?.total_open || 0;
  const openPullRequests = pullRequestSummary.total_open || 0;
  const signalUnavailable =
    pullRequestSummary.availability !== "available" ||
    securitySummary.availability !== "available";

  const pullRequestLabel =
    pullRequestSummary.availability === "available"
      ? `PR ${openPullRequests}`
      : "PR n/a";

  let securityLabel = "SEC n/a";
  if (securitySummary.availability === "available") {
    securityLabel = securityAlerts > 0 ? `SEC ${securityAlerts}` : "SEC clear";
  }

  return (
    <tr className={styles.tableRow} onClick={handleRowClick} role="row">
      {/* Repository Name */}
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

      {/* Language */}
      <td className={styles.tableCell}>
        <span
          className={`${styles.badge} ${styles[`badge--${language.toLowerCase()}`]}`}
        >
          {language}
        </span>
      </td>

      {/* Signals */}
      <td className={styles.tableCell}>
        <div className={styles.signalGroup}>
          <span
            className={`${styles.signalPill} ${
              pullRequestSummary.availability !== "available"
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
              signalUnavailable
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

      {/* First Commit Date */}
      <td className={styles.tableCell}>{formatDate(firstCommitDate)}</td>

      {/* Last Commit Date */}
      <td className={styles.tableCell}>{formatDate(lastCommitDate)}</td>

      {/* Total Commits */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        {totalCommits.toLocaleString()}
      </td>

      {/* Stars */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="GitHub stars">
          {repository.stars?.toLocaleString() || 0}
        </Tooltip>
      </td>

      {/* Spark Score */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="Composite score: 45% activity, 30% popularity, 25% health">
          {repository.composite_score != null
            ? repository.composite_score.toFixed(1)
            : "N/A"}
        </Tooltip>
      </td>

      {/* Bus Factor (T029) */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="Minimum contributors for 50% of commits. Low = higher risk.">
          {repository.bus_factor != null ? (
            <span
              style={{
                display: "inline-flex",
                alignItems: "center",
                gap: "4px",
              }}
            >
              {repository.bus_factor}
              <span
                style={{
                  display: "inline-block",
                  width: "8px",
                  height: "8px",
                  borderRadius: "50%",
                  background:
                    repository.bus_factor_health === "critical"
                      ? "#dc2626"
                      : repository.bus_factor_health === "warning"
                        ? "#d97706"
                        : "#16a34a",
                }}
                aria-label={repository.bus_factor_health ?? "unknown"}
              />
            </span>
          ) : (
            "N/A"
          )}
        </Tooltip>
      </td>
    </tr>
  );
});

export default TableRow;
