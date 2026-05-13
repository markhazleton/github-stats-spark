import styles from "../../RepositoryDetail.module.css";

function ActivityMetricsSection({ repository, formatDate, formatNumber }) {
  return (
    <section className={styles.section}>
      <h3 className={styles.sectionTitle}>Activity Metrics</h3>
      <dl className={styles.detailList}>
        <div className={styles.detailItem}>
          <dt>Open Pull Requests</dt>
          <dd>
            {repository.open_prs != null ? (
              <span
                style={{
                  fontWeight: repository.open_prs > 0 ? 600 : "inherit",
                  color:
                    repository.open_prs > 5
                      ? "#dc2626"
                      : repository.open_prs > 2
                        ? "#d97706"
                        : "inherit",
                }}
              >
                {formatNumber(repository.open_prs)}
              </span>
            ) : (
              <span className={styles.textMuted}>N/A</span>
            )}
          </dd>
        </div>

        <div className={styles.detailItem}>
          <dt>Open Issues</dt>
          <dd>
            {repository.open_issues != null ? (
              formatNumber(repository.open_issues)
            ) : (
              <span className={styles.textMuted}>N/A</span>
            )}
          </dd>
        </div>

        {repository.release_count != null && (
          <div className={styles.detailItem}>
            <dt>Releases</dt>
            <dd>{formatNumber(repository.release_count)}</dd>
          </div>
        )}

        {repository.latest_release_date && (
          <div className={styles.detailItem}>
            <dt>Latest Release</dt>
            <dd>{formatDate(repository.latest_release_date)}</dd>
          </div>
        )}

        <div className={styles.detailItem}>
          <dt>Repository Size</dt>
          <dd>
            {repository.size_kb != null ? (
              `${formatNumber(repository.size_kb)} KB`
            ) : (
              <span className={styles.textMuted}>N/A</span>
            )}
          </dd>
        </div>

        {repository.issue_close_ratio != null && (
          <div className={styles.detailItem}>
            <dt>Issue Close Ratio</dt>
            <dd>{(repository.issue_close_ratio * 100).toFixed(0)}%</dd>
          </div>
        )}
      </dl>
    </section>
  );
}

export default ActivityMetricsSection;
