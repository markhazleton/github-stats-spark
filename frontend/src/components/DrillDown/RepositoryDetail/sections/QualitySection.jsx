import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function QualitySection({ repository, expanded, onToggle }) {
  return (
    <CollapsibleSection section="quality" title="Quality Indicators" expanded={expanded} onToggle={onToggle}>
      <div className={styles.badgeGrid}>
        <span className={repository.has_readme ? styles.badgeSuccess : styles.badgeError}>
          {repository.has_readme ? "✓" : "✗"} README
        </span>
        <span className={repository.has_license ? styles.badgeSuccess : styles.badgeError}>
          {repository.has_license ? "✓" : "✗"} License
        </span>
        <span className={repository.has_ci_cd ? styles.badgeSuccess : styles.badgeError}>
          {repository.has_ci_cd ? "✓" : "✗"} CI/CD
        </span>
        <span className={repository.has_tests ? styles.badgeSuccess : styles.badgeError}>
          {repository.has_tests ? "✓" : "✗"} Tests
        </span>
        <span className={repository.has_docs ? styles.badgeSuccess : styles.badgeError}>
          {repository.has_docs ? "✓" : "✗"} Docs
        </span>
        {repository.is_archived && <span className={styles.badgeWarning}>📦 Archived</span>}
        {repository.is_fork && <span className={styles.badgeInfo}>🔀 Fork</span>}
      </div>
    </CollapsibleSection>
  );
}

export default QualitySection;
