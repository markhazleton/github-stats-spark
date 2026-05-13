import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function QualityBadge({ icon, label, active }) {
  return (
    <span
      className={`${styles.qualityBadge} ${active ? styles.qualityBadgeActive : styles.qualityBadgeInactive}`}
      title={label}
    >
      {icon}
      <span className={styles.qualityBadgeLabel}>{label}</span>
    </span>
  );
}

function QualitySection({ repository, expanded, onToggle }) {
  return (
    <CollapsibleSection
      section="quality"
      title="Quality Indicators"
      expanded={expanded}
      onToggle={onToggle}
    >
      <div className={styles.qualityGrid}>
        <QualityBadge icon="📄" label="README" active={repository.has_readme} />
        <QualityBadge icon="⚖️" label="License" active={repository.has_license} />
        <QualityBadge icon="🔄" label="CI/CD" active={repository.has_ci_cd} />
        <QualityBadge icon="🧪" label="Tests" active={repository.has_tests} />
        <QualityBadge icon="📚" label="Docs" active={repository.has_docs} />
        <QualityBadge icon="💬" label="Discussions" active={repository.has_discussions} />
        <QualityBadge icon="🤝" label="Contributing" active={repository.has_contributing} />
        <QualityBadge icon="🛡️" label="Security Policy" active={repository.has_security_policy} />
      </div>
    </CollapsibleSection>
  );
}

export default QualitySection;
