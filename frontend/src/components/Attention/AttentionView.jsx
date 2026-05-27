import { useMemo, useState } from "react";
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

function getSortValue(repo, key) {
  switch (key) {
    case "score":
      return repo._attention.score;
    case "name":
      return repo.name.toLowerCase();
    case "tier": {
      const order = { critical: 4, elevated: 3, watch: 2, healthy: 1 };
      return order[repo._attention.tier] ?? 0;
    }
    case "prs":
      return repo.pull_request_summary?.availability === "available"
        ? (repo.pull_request_summary.total_open ?? 0)
        : -1;
    case "alerts":
      return repo.security_summary?.active_alert_counts?.total_open ?? 0;
    case "stale":
      return repo.days_since_last_push ?? -1;
    case "readme":
      return repo.has_readme ? 1 : 0;
    default:
      return 0;
  }
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

  const [sort, setSort] = useState({ key: "score", dir: "desc" });

  function handleSort(key) {
    setSort((prev) =>
      prev.key === key
        ? { key, dir: prev.dir === "desc" ? "asc" : "desc" }
        : { key, dir: "desc" },
    );
  }

  const displayRows = useMemo(() => {
    return [...rankedRepositories].sort((a, b) => {
      const av = getSortValue(a, sort.key);
      const bv = getSortValue(b, sort.key);
      if (av < bv) return sort.dir === "asc" ? -1 : 1;
      if (av > bv) return sort.dir === "asc" ? 1 : -1;
      return 0;
    });
  }, [rankedRepositories, sort]);

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

      <section className={styles.tableCard}>
        <div className={styles.tableHeader}>
          <h3>Maintenance ranking</h3>
          <p>Higher scores indicate greater need for maintainer attention.</p>
        </div>

        <div className={styles.tableWrapper}>
          <table className={styles.table}>
            <thead>
              <tr>
                <th>#</th>
                <th
                  className={styles.sortable}
                  onClick={() => handleSort("name")}
                >
                  Repository
                  <span className={styles.sortIcon}>
                    {sort.key === "name"
                      ? sort.dir === "asc"
                        ? "↑"
                        : "↓"
                      : "↕"}
                  </span>
                </th>
                <th
                  className={styles.sortable}
                  onClick={() => handleSort("tier")}
                >
                  Tier
                  <span className={styles.sortIcon}>
                    {sort.key === "tier"
                      ? sort.dir === "asc"
                        ? "↑"
                        : "↓"
                      : "↕"}
                  </span>
                </th>
                <th
                  className={styles.sortable}
                  onClick={() => handleSort("score")}
                >
                  Score
                  <span className={styles.sortIcon}>
                    {sort.key === "score"
                      ? sort.dir === "asc"
                        ? "↑"
                        : "↓"
                      : "↕"}
                  </span>
                </th>
                <th
                  className={styles.sortable}
                  onClick={() => handleSort("prs")}
                >
                  PRs
                  <span className={styles.sortIcon}>
                    {sort.key === "prs"
                      ? sort.dir === "asc"
                        ? "↑"
                        : "↓"
                      : "↕"}
                  </span>
                </th>
                <th
                  className={styles.sortable}
                  onClick={() => handleSort("alerts")}
                >
                  Alerts
                  <span className={styles.sortIcon}>
                    {sort.key === "alerts"
                      ? sort.dir === "asc"
                        ? "↑"
                        : "↓"
                      : "↕"}
                  </span>
                </th>
                <th
                  className={styles.sortable}
                  onClick={() => handleSort("stale")}
                >
                  Stale (days)
                  <span className={styles.sortIcon}>
                    {sort.key === "stale"
                      ? sort.dir === "asc"
                        ? "↑"
                        : "↓"
                      : "↕"}
                  </span>
                </th>
                <th
                  className={styles.sortable}
                  onClick={() => handleSort("readme")}
                >
                  README
                  <span className={styles.sortIcon}>
                    {sort.key === "readme"
                      ? sort.dir === "asc"
                        ? "↑"
                        : "↓"
                      : "↕"}
                  </span>
                </th>
              </tr>
            </thead>
            <tbody>
              {displayRows.map((repo, index) => {
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
                      {repo.security_summary?.active_alert_counts?.total_open ??
                        0}
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
      </aside>
    </div>
  );
}

AttentionView.propTypes = {
  repositories: PropTypes.array.isRequired,
  onRepoClick: PropTypes.func,
};

export default AttentionView;
