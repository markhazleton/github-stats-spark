import styles from "../../RepositoryDetail.module.css";

function CommitMetricsSection({ repository, formatDate, formatNumber, formatSize }) {
  const largestCommit = repository.commit_metrics?.largest_commit || repository.largest_commit;
  const smallestCommit = repository.commit_metrics?.smallest_commit || repository.smallest_commit;

  return (
    <section className={styles.section}>
      <h3 className={styles.sectionTitle}>Commit Metrics</h3>
      <dl className={styles.detailList}>
        <div className={styles.detailItem}>
          <dt>Average Commit Size</dt>
          <dd>{formatSize(repository.commit_metrics?.avg_size || repository.avg_commit_size)}</dd>
        </div>
        {largestCommit && (
          <div className={styles.detailItem}>
            <dt>Largest Commit</dt>
            <dd>
              {formatSize(largestCommit.size)}
              <div className={styles.textMuted}>
                {largestCommit.sha?.substring(0, 7)} • {formatDate(largestCommit.date)}
              </div>
              <div className={styles.textMuted}>
                {formatNumber(largestCommit.files_changed)} files • +
                {formatNumber(largestCommit.lines_added)} / -{formatNumber(largestCommit.lines_deleted)}
              </div>
            </dd>
          </div>
        )}
        {smallestCommit && (
          <div className={styles.detailItem}>
            <dt>Smallest Commit</dt>
            <dd>
              {formatSize(smallestCommit.size)}
              <div className={styles.textMuted}>
                {smallestCommit.sha?.substring(0, 7)} • {formatDate(smallestCommit.date)}
              </div>
            </dd>
          </div>
        )}
      </dl>
    </section>
  );
}

export default CommitMetricsSection;
