import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function CommitHistorySection({
  repository,
  expanded,
  onToggle,
  formatDate,
  formatNumber,
}) {
  return (
    <CollapsibleSection
      section="commits"
      title="Commit Activity"
      expanded={expanded}
      onToggle={onToggle}
    >
      <dl className={styles.detailList}>
        <div className={styles.detailItem}>
          <dt>Total Commits</dt>
          <dd className={styles.highlight}>
            {formatNumber(repository.total_commits || 0)}
          </dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Repository Age</dt>
          <dd>
            {repository.age_days != null
              ? `${repository.age_days} days`
              : "N/A"}
          </dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Days Since Last Push</dt>
          <dd>
            {repository.days_since_last_push != null
              ? `${repository.days_since_last_push} days ago`
              : "N/A"}
          </dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Created</dt>
          <dd>{formatDate(repository.created_at)}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Last Push</dt>
          <dd>{formatDate(repository.pushed_at)}</dd>
        </div>
        {repository.total_commits != null && repository.age_days > 0 && (
          <div className={styles.detailItem}>
            <dt>Avg Commits / Month</dt>
            <dd>
              {((repository.total_commits / repository.age_days) * 30).toFixed(
                1,
              )}
            </dd>
          </div>
        )}
      </dl>
    </CollapsibleSection>
  );
}

export default CommitHistorySection;
