import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function CommitHistorySection({ repository, expanded, onToggle, formatDate, formatNumber, formatSize }) {
  if (!repository.commit_history) return null;

  return (
    <CollapsibleSection section="commits" title="Commit Activity" expanded={expanded} onToggle={onToggle}>
      <dl className={styles.detailList}>
        <div className={styles.detailItem}>
          <dt>Total Commits</dt>
          <dd className={styles.highlight}>{formatNumber(repository.commit_history.total_commits)}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Last 90 Days</dt>
          <dd>{formatNumber(repository.commit_history.recent_90d)}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Last 180 Days</dt>
          <dd>{formatNumber(repository.commit_history.recent_180d)}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Last 365 Days</dt>
          <dd>{formatNumber(repository.commit_history.recent_365d)}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>First Commit</dt>
          <dd>{formatDate(repository.commit_history.first_commit_date)}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Last Commit</dt>
          <dd>{formatDate(repository.commit_history.last_commit_date)}</dd>
        </div>
        {repository.commit_velocity != null && (
          <div className={styles.detailItem}>
            <dt>Commit Velocity</dt>
            <dd>{formatSize(repository.commit_velocity)} commits/month</dd>
          </div>
        )}
      </dl>
    </CollapsibleSection>
  );
}

export default CommitHistorySection;
