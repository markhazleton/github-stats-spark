import { useMemo } from "react";
import PropTypes from "prop-types";
import styles from "./AttentionView.module.css";

const tierLabels = {
  critical: "Critical",
  elevated: "Elevated",
  watch: "Watch",
  healthy: "Healthy",
};

const tierClassNames = {
  critical: styles.tierCritical,
  elevated: styles.tierElevated,
  watch: styles.tierWatch,
  healthy: styles.tierHealthy,
};

function formatScore(value) {
  return typeof value === "number" ? value.toFixed(1) : "0.0";
}

function AttentionView({ repositories, onRepoClick }) {
  const rankedRepositories = useMemo(() => {
    return [...repositories]
      .filter((repo) => repo.attention_metrics)
      .sort((a, b) => (b.attention_score || 0) - (a.attention_score || 0));
  }, [repositories]);

  const summary = useMemo(() => {
    const needsAttention = rankedRepositories.filter(
      (repo) => repo.attention_metrics?.needs_attention,
    );
    const critical = needsAttention.filter(
      (repo) => repo.attention_metrics?.tier === "critical",
    );
    const securityBacklog = rankedRepositories.filter(
      (repo) =>
        (repo.security_summary?.active_alert_counts?.total_open || 0) > 0,
    );
    const stale = rankedRepositories.filter(
      (repo) => (repo.days_since_last_push || 0) >= 90,
    );

    return {
      total: needsAttention.length,
      critical: critical.length,
      securityBacklog: securityBacklog.length,
      stale: stale.length,
    };
  }, [rankedRepositories]);

  if (rankedRepositories.length === 0) {
    return (
      <div className={styles.emptyState}>
        <h3>No attention signals available</h3>
        <p>
          Generate repositories.json with schema 2.2.0 or later to populate the
          maintenance ranking view.
        </p>
      </div>
    );
  }

  return (
    <div className={styles.layout}>
      <div className={styles.summaryGrid}>
        <article className={styles.summaryCard}>
          <span className={styles.summaryLabel}>Need attention</span>
          <strong className={styles.summaryValue}>{summary.total}</strong>
        </article>
        <article className={styles.summaryCard}>
          <span className={styles.summaryLabel}>Critical</span>
          <strong className={styles.summaryValue}>{summary.critical}</strong>
        </article>
        <article className={styles.summaryCard}>
          <span className={styles.summaryLabel}>Security backlog</span>
          <strong className={styles.summaryValue}>
            {summary.securityBacklog}
          </strong>
        </article>
        <article className={styles.summaryCard}>
          <span className={styles.summaryLabel}>Stale 90+ days</span>
          <strong className={styles.summaryValue}>{summary.stale}</strong>
        </article>
      </div>

      <div className={styles.contentGrid}>
        <section className={styles.tableCard}>
          <div className={styles.tableHeader}>
            <h3>Maintenance ranking</h3>
            <p>Higher scores indicate greater need for maintainer attention.</p>
          </div>

          <div className={styles.tableWrapper}>
            <table className={styles.table}>
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Repository</th>
                  <th>Tier</th>
                  <th>Score</th>
                  <th>PRs</th>
                  <th>Alerts</th>
                  <th>Stale</th>
                  <th>Deps</th>
                </tr>
              </thead>
              <tbody>
                {rankedRepositories.map((repo) => {
                  const attention = repo.attention_metrics;
                  const components = attention.components;
                  return (
                    <tr
                      key={repo.name}
                      className={styles.row}
                      onClick={() => onRepoClick && onRepoClick(repo)}
                    >
                      <td>{repo.attention_rank || "-"}</td>
                      <td>
                        <div className={styles.repoCell}>
                          <strong>{repo.name}</strong>
                          <span>{repo.language || "Unknown"}</span>
                        </div>
                      </td>
                      <td>
                        <span
                          className={`${styles.tierBadge} ${tierClassNames[attention.tier] || styles.tierHealthy}`}
                        >
                          {tierLabels[attention.tier] || attention.tier}
                        </span>
                      </td>
                      <td>{formatScore(repo.attention_score)}</td>
                      <td>{components.pull_requests.total_open}</td>
                      <td>
                        {components.security.active_alert_counts?.total_open ||
                          0}
                      </td>
                      <td>{repo.days_since_last_push ?? "n/a"}</td>
                      <td>
                        {components.dependencies.outdated_count}/
                        {components.dependencies.total_dependencies}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </section>

        <aside className={styles.explainerCard}>
          <h3>What drives the score</h3>
          <ul className={styles.explainerList}>
            <li>
              Security contributes 35% with weighted critical and high alerts.
            </li>
            <li>
              Pull requests contribute 25% based on backlog, age, and review
              load.
            </li>
            <li>Staleness contributes 25% from days since the last push.</li>
            <li>
              Dependencies contribute 15% from outdated packages and version
              coverage gaps.
            </li>
          </ul>

          <h4>Quick triage</h4>
          <div className={styles.topList}>
            {rankedRepositories.slice(0, 5).map((repo) => (
              <button
                key={repo.name}
                className={styles.topListItem}
                onClick={() => onRepoClick && onRepoClick(repo)}
              >
                <span>
                  <strong>{repo.name}</strong>
                  <small>
                    {repo.attention_metrics?.reasons?.join(", ") || "general"}
                  </small>
                </span>
                <span>{formatScore(repo.attention_score)}</span>
              </button>
            ))}
          </div>
        </aside>
      </div>
    </div>
  );
}

AttentionView.propTypes = {
  repositories: PropTypes.array.isRequired,
  onRepoClick: PropTypes.func,
};

export default AttentionView;
