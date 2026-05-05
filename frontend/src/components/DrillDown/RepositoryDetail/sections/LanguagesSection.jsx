import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function LanguagesSection({ repository, expanded, onToggle, calculateLanguagePercentage }) {
  if (!repository.language_stats || Object.keys(repository.language_stats).length === 0) {
    return null;
  }

  return (
    <CollapsibleSection
      section="languages"
      title={`Languages (${repository.language_count})`}
      expanded={expanded}
      onToggle={onToggle}
    >
      <div className={styles.languageList}>
        {Object.entries(repository.language_stats)
          .sort(([, a], [, b]) => b - a)
          .slice(0, 10)
          .map(([lang, bytes]) => (
            <div key={lang} className={styles.languageItem}>
              <div className={styles.languageHeader}>
                <span className={styles.languageName}>{lang}</span>
                <span className={styles.languagePercent}>{calculateLanguagePercentage(bytes)}%</span>
              </div>
              <div className={styles.languageBar}>
                <div
                  className={styles.languageBarFill}
                  style={{ width: `${calculateLanguagePercentage(bytes)}%` }}
                />
              </div>
            </div>
          ))}
      </div>
    </CollapsibleSection>
  );
}

export default LanguagesSection;
