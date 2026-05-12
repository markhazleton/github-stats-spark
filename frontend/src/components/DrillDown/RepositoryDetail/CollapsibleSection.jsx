import styles from "../RepositoryDetail.module.css";

function CollapsibleSection({
  section,
  title,
  expanded,
  onToggle,
  badge,
  children,
}) {
  return (
    <section className={styles.section}>
      <h3
        className={`${styles.sectionTitle} ${styles.collapsible}`}
        onClick={() => onToggle(section)}
        role="button"
        tabIndex={0}
        onKeyDown={(e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            onToggle(section);
          }
        }}
        aria-expanded={expanded}
      >
        <span>{title}</span>
        {badge}
        <span className={styles.chevron}>{expanded ? "▲" : "▼"}</span>
      </h3>
      {expanded && children}
    </section>
  );
}

export default CollapsibleSection;
