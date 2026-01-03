import React, { useMemo } from "react";
import PropTypes from "prop-types";
import styles from "./ComparisonView.module.css";
import {
  formatNumber,
  formatDate,
  calculatePercentageDifference,
} from "@/services/metricsCalculator";

/**
 * ComparisonView Component
 *
 * Displays side-by-side comparison of selected repositories with
 * color-coded metric differences and percentage calculations.
 *
 * @component
 * @param {Object} props
 * @param {Array} props.repositories - Array of repository objects to compare
 * @param {Function} props.onRemoveRepo - Callback to remove a repository from comparison
 */
function ComparisonView({ repositories, onRemoveRepo }) {
  /**
   * Metrics to compare across repositories - wrapped in useMemo for stability
   */
  const comparisonMetrics = useMemo(
    () => [
      { key: "stars", label: "Stars", type: "number" },
      { key: "forks", label: "Forks", type: "number" },
      { key: "watchers", label: "Watchers", type: "number" },
      { key: "open_issues", label: "Open Issues", type: "number" },
      { key: "size_kb", label: "Size (KB)", type: "number" },
      {
        key: "commit_history.total_commits",
        label: "Total Commits",
        type: "number",
      },
      {
        key: "commit_history.recent_90d",
        label: "Commits (90d)",
        type: "number",
      },
      {
        key: "commit_metrics.avg_size",
        label: "Avg Commit Size",
        type: "number",
      },
      {
        key: "commit_velocity",
        label: "Commit Velocity",
        type: "number",
        decimals: 2,
      },
      { key: "age_days", label: "Age (days)", type: "number" },
      { key: "days_since_last_push", label: "Days Since Push", type: "number" },
      { key: "language", label: "Language", type: "string" },
      { key: "created_at", label: "Created", type: "date" },
      { key: "updated_at", label: "Last Updated", type: "date" },
      { key: "has_readme", label: "Has README", type: "boolean" },
      { key: "has_license", label: "Has License", type: "boolean" },
      { key: "has_ci_cd", label: "Has CI/CD", type: "boolean" },
      { key: "has_tests", label: "Has Tests", type: "boolean" },
    ],
    [],
  );

  /**
   * Get nested value from object using dot notation
   */
  const getNestedValue = (obj, path) => {
    return path.split(".").reduce((acc, part) => acc?.[part], obj);
  };

  /**
   * Calculate comparison data with differences
   */
  const comparisonData = useMemo(() => {
    if (repositories.length === 0) return [];

    return comparisonMetrics.map((metric) => {
      const values = repositories.map((repo) =>
        getNestedValue(repo, metric.key),
      );

      // Find min and max for numeric comparisons
      let min = null;
      let max = null;
      if (metric.type === "number") {
        const numericValues = values.filter((v) => v != null && !isNaN(v));
        if (numericValues.length > 0) {
          min = Math.min(...numericValues);
          max = Math.max(...numericValues);
        }
      }

      return {
        metric,
        values,
        min,
        max,
      };
    });
  }, [repositories, comparisonMetrics]);

  /**
   * Get color coding class based on value comparison
   */
  const getColorClass = (value, min, max, type) => {
    if (type !== "number" || value == null || min === max) return "";

    if (value === max) return styles.highest;
    if (value === min) return styles.lowest;
    return styles.middle;
  };

  /**
   * Format value based on type
   */
  const formatValue = (value, type, decimals = 0) => {
    if (value == null || value === undefined) return "N/A";

    switch (type) {
      case "number":
        return formatNumber(value, decimals);
      case "date":
        return formatDate(value);
      case "boolean":
        return value ? "✓" : "✗";
      case "string":
      default:
        return String(value);
    }
  };

  if (repositories.length === 0) {
    return (
      <div className={styles.emptyState}>
        <p>No repositories selected for comparison.</p>
        <p className="text-muted text-sm">
          Select 2 or more repositories from the table to compare their metrics.
        </p>
      </div>
    );
  }

  return (
    <div className={styles.comparisonView}>
      <div className={styles.comparisonGrid}>
        {/* Header Row */}
        <div className={styles.headerRow}>
          <div className={styles.metricLabel}>Metric</div>
          {repositories.map((repo) => (
            <div key={repo.name} className={styles.repoHeader}>
              <div className={styles.repoName}>{repo.name}</div>
              <button
                className={styles.removeButton}
                onClick={() => onRemoveRepo(repo.name)}
                aria-label={`Remove ${repo.name} from comparison`}
                title={`Remove ${repo.name}`}
              >
                ×
              </button>
            </div>
          ))}
        </div>

        {/* Metric Rows */}
        {comparisonData.map((item) => (
          <div key={item.metric.key} className={styles.metricRow}>
            <div className={styles.metricLabel}>{item.metric.label}</div>
            {item.values.map((value, colIndex) => {
              const colorClass = getColorClass(
                value,
                item.min,
                item.max,
                item.metric.type,
              );

              // Calculate percentage difference from max
              const percentDiff =
                item.metric.type === "number" &&
                item.max != null &&
                value != null
                  ? calculatePercentageDifference(value, item.max)
                  : null;

              return (
                <div
                  key={colIndex}
                  className={`${styles.metricValue} ${colorClass}`}
                >
                  <div className={styles.value}>
                    {formatValue(value, item.metric.type, item.metric.decimals)}
                  </div>
                  {percentDiff !== null && percentDiff !== 0 && (
                    <div className={styles.percentDiff}>
                      {percentDiff > 0 ? "+" : ""}
                      {percentDiff}%
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        ))}
      </div>

      {/* Legend */}
      <div className={styles.legend}>
        <div className={styles.legendItem}>
          <span className={`${styles.legendBox} ${styles.highest}`}></span>
          <span>Highest Value</span>
        </div>
        <div className={styles.legendItem}>
          <span className={`${styles.legendBox} ${styles.lowest}`}></span>
          <span>Lowest Value</span>
        </div>
        <div className={styles.legendItem}>
          <span className={styles.legendNote}>
            Percentage shows difference from maximum value
          </span>
        </div>
      </div>
    </div>
  );
}

ComparisonView.propTypes = {
  repositories: PropTypes.arrayOf(PropTypes.object).isRequired,
  onRemoveRepo: PropTypes.func.isRequired,
};

export default ComparisonView;
