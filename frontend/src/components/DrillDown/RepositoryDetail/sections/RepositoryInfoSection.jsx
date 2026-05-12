import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function RepositoryInfoSection({
  repository,
  expanded,
  onToggle,
  formatDate,
  formatRelativeDate,
  formatNumber,
}) {
  return (
    <CollapsibleSection
      section="info"
      title="Repository Info"
      expanded={expanded}
      onToggle={onToggle}
    >
      <dl className={styles.detailList}>
        <div className={styles.detailItem}>
          <dt>Language</dt>
          <dd>
            <span className={styles.badge}>
              {repository.language || "Unknown"}
            </span>
          </dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Created</dt>
          <dd>{formatDate(repository.created_at)}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Last Updated</dt>
          <dd>{formatDate(repository.updated_at)}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Last Push</dt>
          <dd>
            {formatDate(repository.pushed_at)}
            {repository.days_since_last_push != null && (
              <span className={styles.textMuted}>
                {" "}
                ({formatRelativeDate(repository.days_since_last_push)})
              </span>
            )}
          </dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Age</dt>
          <dd>{repository.age_days ? `${repository.age_days} days` : "N/A"}</dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Size</dt>
          <dd>
            {repository.size_kb
              ? `${formatNumber(repository.size_kb)} KB`
              : "N/A"}
          </dd>
        </div>
        <div className={styles.detailItem}>
          <dt>Repository URL</dt>
          <dd>
            <a
              href={repository.url}
              target="_blank"
              rel="noopener noreferrer"
              className={styles.link}
            >
              View on GitHub →
            </a>
          </dd>
        </div>
        {repository.website_url && (
          <div className={styles.detailItem}>
            <dt>Website</dt>
            <dd>
              <a
                href={repository.website_url}
                target="_blank"
                rel="noopener noreferrer"
                className={styles.link}
              >
                {repository.homepage ? "🌐 Homepage" : "📄 GitHub Pages"} →
              </a>
            </dd>
          </div>
        )}
        {repository.has_pages &&
          !repository.homepage &&
          repository.pages_url && (
            <div className={styles.detailItem}>
              <dt>GitHub Pages</dt>
              <dd>
                <a
                  href={repository.pages_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={styles.link}
                >
                  📄 View Site →
                </a>
              </dd>
            </div>
          )}
      </dl>
    </CollapsibleSection>
  );
}

export default RepositoryInfoSection;
