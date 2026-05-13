import styles from "../../RepositoryDetail.module.css";

function RankingSection({ repository }) {
  const score = repository.readme_quality_score;
  if (score == null) return null;

  const getScoreColor = (s) => {
    if (s >= 80) return "#16a34a";
    if (s >= 60) return "#d97706";
    return "#dc2626";
  };

  const getScoreLabel = (s) => {
    if (s >= 80) return "Good";
    if (s >= 60) return "Fair";
    return "Needs work";
  };

  return (
    <section className={styles.section}>
      <h3 className={styles.sectionTitle}>README Quality</h3>
      <dl className={styles.detailList}>
        <div className={styles.detailItem}>
          <dt>Quality Score</dt>
          <dd className={styles.highlight}>
            {score}
            <span style={{ fontSize: "0.75rem", color: "var(--color-text-muted)", marginLeft: "4px" }}>
              / 100
            </span>
          </dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Assessment</dt>
          <dd>
            <span
              style={{
                display: "inline-block",
                padding: "1px 8px",
                borderRadius: "4px",
                fontSize: "0.75rem",
                fontWeight: 600,
                background: getScoreColor(score),
                color: "#fff",
              }}
            >
              {getScoreLabel(score)}
            </span>
          </dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Has README</dt>
          <dd>{repository.has_readme ? "✓ Yes" : "✗ No"}</dd>
        </div>
      </dl>
    </section>
  );
}

export default RankingSection;
