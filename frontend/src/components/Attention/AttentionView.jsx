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

function computeAttentionScore(repo) {
  let score = 0;
  const reasons = [];

  const staleDays = repo.days_since_last_push ?? 0;
  if (staleDays > 180) {
    score += 30;
    reasons.push("inactive 6+ months");
  } else if (staleDays > 90) {
    score += 20;
    reasons.push("inactive 90+ days");
  } else if (staleDays > 30) {
    score += 5;
  }

  if (!repo.has_readme) {
    score += 20;
    reasons.push("no README");
  }

  if (!repo.has_license) {
    score += 10;
    reasons.push("no license");
  }
  if (!repo.has_ci_cd) {
    score += 10;
    reasons.push("no CI/CD");
  }

  const issues = repo.open_issues ?? 0;
  score += Math.min(issues * 2, 15);
  if (issues > 3) reasons.push(`${issues} open issues`);

  const prs =
    repo.pull_request_summary?.availability === "available"
      ? (repo.pull_request_summary.total_open ?? 0)
      : 0;
  score += Math.min(prs * 3, 15);
  if (prs > 2) reasons.push(`${prs} open PRs`);

  const alerts = repo.security_summary?.active_alert_counts?.total_open ?? 0;
  score += Math.min(alerts * 10, 30);
  if (alerts > 0) reasons.push(`${alerts} security alerts`);

  let tier = "healthy";
  if (score >= 50) tier = "critical";
  else if (score >= 30) tier = "elevated";
  else if (score >= 15) tier = "watch";

  return { score, tier, reasons, needs_attention: score >= 15 };
}

function AttentionView({ repositories, onRepoClick }) {
  const rankedRepositories = useMemo(() => {
    return [...repositories]
      .map((repo) => ({ ...repo, _attention: computeAttentionScore(repo) }))
      .sort((a, b) => b._attention.score - a._attention.score);
  }, [repositories]);

  const summary = useMemo(() => {
    const needsAttention = rankedRepositories.filter(
      (r) => r._attention.needs_attention,
    );
    return {
      total: needsAttention.length,
      critical: needsAttention.filter((r) => r._attention.tier === "critical")
        .length,
      securityBacklog: rankedRepositories.filter(
        (r) => (r.security_summary?.active_alert_counts?.total_open ?? 0) > 0,
      ).length,
      stale: rankedRepositories.filter(
        (r) => (r.days_since_last_push ?? 0) >= 90,
      ).length,
    };
  }, [rankedRepositories]);

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
                  <th>Stale (days)</th>
                  <th>README</th>
                </tr>
              </thead>
              <tbody>
                {rankedRepositories.map((repo, index) => {
                  const att = repo._attention;
                  return (
                    <tr
                      key={repo.name}
                      className={styles.row}
                      onClick={() => onRepoClick && onRepoClick(repo)}
                    >
                      <td>{index + 1}</td>
                      <td>
                        <div className={styles.repoCell}>
                          <strong>{repo.name}</strong>
                          <span>{repo.language || "Unknown"}</span>
                        </div>
                      </td>
                      <td>
                        <span
                          className={`${styles.tierBadge} ${
                            tierClassNames[att.tier] || styles.tierHealthy
                          }`}
                        >
                          {tierLabels[att.tier] || att.tier}
                        </span>
                      </td>
                      <td>{att.score.toFixed(0)}</td>
                      <td>
                        {repo.pull_request_summary?.availability === "available"
                          ? repo.pull_request_summary.total_open
                          : "n/a"}
                      </td>
                      <td>
                        {repo.security_summary?.active_alert_counts
                          ?.total_open ?? 0}
                      </td>
                      <td>{repo.days_since_last_push ?? "n/a"}</td>
                      <td>{repo.has_readme ? "Yes" : "No"}</td>
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
            <li>Staleness: up to 30 pts for repos inactive 6+ months.</li>
            <li>Missing README adds 20 pts.</li>
            <li>Missing license or CI/CD each add 10 pts.</li>
            <li>Open issues contribute up to 15 pts; open PRs up to 15 pts.</li>
            <li>Security alerts contribute up to 30 pts.</li>
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
                    {repo._attention.reasons.slice(0, 2).join(", ") ||
                      "all good"}
                  </small>
                </span>
                <span>{repo._attention.score.toFixed(0)}</span>
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
