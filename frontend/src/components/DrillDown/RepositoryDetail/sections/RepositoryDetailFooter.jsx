import styles from "../../RepositoryDetail.module.css";

function RepositoryDetailFooter({ onClose, onNext, onPrevious }) {
  return (
    <div className={styles.modalFooter}>
      <div className={styles.navigationButtons}>
        {onPrevious && (
          <button className={styles.btnSecondary} onClick={onPrevious}>
            ← Previous
          </button>
        )}
        {onNext && (
          <button className={styles.btnSecondary} onClick={onNext}>
            Next →
          </button>
        )}
      </div>
      <button className={styles.btnPrimary} onClick={onClose}>
        Close
      </button>
    </div>
  );
}

export default RepositoryDetailFooter;
