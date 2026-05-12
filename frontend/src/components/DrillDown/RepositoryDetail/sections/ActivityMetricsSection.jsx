import styles from "../../RepositoryDetail.module.css";

function ActivityMetricsSection({ repository, formatDate, formatNumber }) {
  return (
    <section className={styles.section}>
      <h3 className={styles.sectionTitle}>Activity Metrics</h3>
      <dl className={styles.detailList}>
        {repository.contributors_count != null && (
          <div className={styles.detailItem}>
            <dt>Contributors</dt>
            <dd>{formatNumber(repository.contributors_count)}</dd>
          </div>
        )}
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

        {repository.total_additions != null ||
        repository.total_deletions != null ? (
          <>
            <div className={styles.detailItem}>
              <dt>Lines Added</dt>
              <dd>+{(repository.total_additions ?? 0).toLocaleString()}</dd>
            </div>
            <div className={styles.detailItem}>
              <dt>Lines Deleted</dt>
              <dd>-{(repository.total_deletions ?? 0).toLocaleString()}</dd>
            </div>
            {repository.code_churn != null && (
              <div className={styles.detailItem}>
                <dt>Code Churn</dt>
                <dd>{repository.code_churn.toLocaleString()} lines</dd>
              </div>
            )}
          </>
        ) : (
          <div className={styles.detailItem}>
            <dt>Commit Volume</dt>
            <dd className={styles.textMuted}>Stats not available</dd>
          </div>
        )}

        <div className={styles.detailItem}>
          <dt>Bus Factor</dt>
          <dd>
            {repository.bus_factor != null ? (
              <span>
                {repository.bus_factor}{" "}
                <span
                  style={{
                    display: "inline-block",
                    padding: "1px 6px",
                    borderRadius: "4px",
                    fontSize: "0.75rem",
                    fontWeight: 600,
                    background:
                      repository.bus_factor_health === "critical"
                        ? "#dc2626"
                        : repository.bus_factor_health === "warning"
                          ? "#d97706"
                          : "#16a34a",
                    color: "#fff",
                  }}
                >
                  {repository.bus_factor_health ?? "unknown"}
                </span>
              </span>
            ) : (
              <span className={styles.textMuted}>N/A</span>
            )}
          </dd>
        </div>
      </dl>
    </section>
  );
}

export default ActivityMetricsSection;
