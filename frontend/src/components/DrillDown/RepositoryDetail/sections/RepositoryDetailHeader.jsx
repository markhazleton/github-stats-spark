import styles from "../../RepositoryDetail.module.css";

function RepositoryDetailHeader({ repository, onClose, formatNumber }) {
  return (
    <>
      <div className={styles.modalHeader}>
        {onClose && (
          <button className={styles.backButton} onClick={onClose} aria-label="Back to list">
            ← Back
          </button>
        )}
        <div className={styles.headerContent}>
          <h2 className={styles.modalTitle}>{repository.name}</h2>
          {repository.description && <p className={styles.modalDescription}>{repository.description}</p>}
        </div>
        <button className={styles.closeButton} onClick={onClose} aria-label="Close">
          ×
        </button>
      </div>

      <div className={styles.statsBar}>
        <div className={styles.statItem}>
          <span className={styles.statValue}>⭐ {formatNumber(repository.stars)}</span>
          <span className={styles.statLabel}>Stars</span>
        </div>
        <div className={styles.statItem}>
          <span className={styles.statValue}>🔀 {formatNumber(repository.forks)}</span>
          <span className={styles.statLabel}>Forks</span>
        </div>
        <div className={styles.statItem}>
          <span className={styles.statValue}>👁️ {formatNumber(repository.watchers)}</span>
          <span className={styles.statLabel}>Watchers</span>
        </div>
        <div className={styles.statItem}>
          <span className={styles.statValue}>🐛 {formatNumber(repository.open_issues)}</span>
          <span className={styles.statLabel}>Issues</span>
        </div>
        {repository.rank && (
          <div className={styles.statItem}>
            <span className={styles.statValue}>🏆 #{repository.rank}</span>
            <span className={styles.statLabel}>Rank</span>
          </div>
        )}
      </div>
    </>
  );
}

export default RepositoryDetailHeader;
