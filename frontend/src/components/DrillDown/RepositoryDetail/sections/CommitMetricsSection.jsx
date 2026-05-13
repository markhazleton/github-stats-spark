import styles from "../../RepositoryDetail.module.css";

function CommitMetricsSection({ repository, formatDate, formatNumber }) {
  return (
    <section className={styles.section}>
      <h3 className={styles.sectionTitle}>Releases &amp; Issues</h3>
      <dl className={styles.detailList}>
        <div className={styles.detailItem}>
          <dt>Total Releases</dt>
          <dd className={styles.highlight}>
            {formatNumber(repository.release_count ?? 0)}
          </dd>
        </div>

        {repository.latest_release_tag && (
          <div className={styles.detailItem}>
            <dt>Latest Release</dt>
            <dd>
              {repository.latest_release_tag}
              {repository.latest_release_date && (
                <div className={styles.textMuted}>
                  {formatDate(repository.latest_release_date)}
                </div>
              )}
            </dd>
          </div>
        )}

        <div className={styles.detailItem}>
          <dt>Open Issues</dt>
          <dd>
            {repository.open_issues != null
              ? formatNumber(repository.open_issues)
              : "N/A"}
          </dd>
        </div>

        <div className={styles.detailItem}>
          <dt>Open Pull Requests</dt>
          <dd>
            {repository.open_prs != null
              ? formatNumber(repository.open_prs)
              : "N/A"}
          </dd>
        </div>

        {repository.issue_close_ratio != null && (
          <div className={styles.detailItem}>
            <dt>Issue Close Ratio</dt>
            <dd>{(repository.issue_close_ratio * 100).toFixed(0)}%</dd>
          </div>
        )}

        <div className={styles.detailItem}>
          <dt>Watchers</dt>
          <dd>{formatNumber(repository.watchers ?? 0)}</dd>
        </div>
      </dl>
    </section>
  );
}

export default CommitMetricsSection;
