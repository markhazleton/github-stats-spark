import styles from "../../RepositoryDetail.module.css";

const LANGUAGE_COLORS = {
  "C#": "#178600",
  TypeScript: "#3178c6",
  Python: "#3572A5",
  JavaScript: "#f1e05a",
  HTML: "#e34c26",
  CSS: "#563d7c",
  SCSS: "#c6538c",
  PowerShell: "#012456",
  PHP: "#4F5D95",
  "Visual Basic .NET": "#945db7",
  Shell: "#89e051",
  Go: "#00ADD8",
  Rust: "#dea584",
  Java: "#b07219",
  Ruby: "#701516",
  Markdown: "#083fa1",
  Vue: "#4FC08D",
  Swift: "#F05138",
  Kotlin: "#A97BFF",
  Dockerfile: "#384d54",
};

const MATURITY_CONFIG = {
  stable: { label: "Stable", color: "#22c55e", bg: "rgba(34, 197, 94, 0.1)" },
  "active-development": {
    label: "Active Dev",
    color: "#3b82f6",
    bg: "rgba(59, 130, 246, 0.1)",
  },
  experimental: {
    label: "Experimental",
    color: "#f59e0b",
    bg: "rgba(245, 158, 11, 0.1)",
  },
  archived: {
    label: "Archived",
    color: "#6b7280",
    bg: "rgba(107, 114, 128, 0.1)",
  },
};

function RepositoryDetailHeader({ repository, onClose, formatNumber }) {
  const language = repository.language || "Unknown";
  const langColor = LANGUAGE_COLORS[language] || "#8b949e";
  const aiSummary = repository.ai_summary;
  const maturity = aiSummary?.project_maturity;
  const maturityConfig = MATURITY_CONFIG[maturity] || null;

  const daysSincePush = repository.days_since_last_push;
  const isRecent = daysSincePush != null && daysSincePush <= 3;
  const activityLabel =
    daysSincePush == null
      ? "Unknown"
      : daysSincePush === 0
        ? "Today"
        : daysSincePush === 1
          ? "Yesterday"
          : daysSincePush <= 7
            ? `${daysSincePush}d ago`
            : daysSincePush <= 30
              ? `${Math.round(daysSincePush / 7)}w ago`
              : daysSincePush <= 365
                ? `${Math.round(daysSincePush / 30)}mo ago`
                : `${Math.round(daysSincePush / 365)}y ago`;

  return (
    <>
      <div className={styles.modalAccent} style={{ background: langColor }} />

      <div className={styles.modalHeader}>
        {onClose && (
          <button
            className={styles.backButton}
            onClick={onClose}
            aria-label="Back to list"
          >
            ← Back
          </button>
        )}

        <div className={styles.headerContent}>
          <div className={styles.headerTitleRow}>
            <h2 className={styles.modalTitle}>{repository.name}</h2>
            <a
              href={repository.url}
              target="_blank"
              rel="noopener noreferrer"
              className={styles.headerExternalLink}
              title="View on GitHub"
              aria-label="View on GitHub"
            >
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                aria-hidden="true"
              >
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                <polyline points="15 3 21 3 21 9" />
                <line x1="10" y1="14" x2="21" y2="3" />
              </svg>
            </a>
            {repository.homepage && (
              <a
                href={repository.homepage}
                target="_blank"
                rel="noopener noreferrer"
                className={styles.headerExternalLink}
                title="Live site"
                aria-label="Visit live site"
              >
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  aria-hidden="true"
                >
                  <circle cx="12" cy="12" r="10" />
                  <line x1="2" y1="12" x2="22" y2="12" />
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
                </svg>
              </a>
            )}
          </div>

          <div className={styles.headerMeta}>
            <span className={styles.langChip}>
              <span
                className={styles.langDot}
                style={{ background: langColor }}
              />
              <span className={styles.langName}>{language}</span>
            </span>
            {maturityConfig && (
              <span
                className={styles.maturityBadge}
                style={{
                  color: maturityConfig.color,
                  background: maturityConfig.bg,
                  border: `1px solid ${maturityConfig.color}30`,
                }}
              >
                {maturityConfig.label}
              </span>
            )}
            {isRecent && <span className={styles.recentBadge}>🔥 Hot</span>}
            {repository.is_archived && (
              <span className={styles.archivedBadge}>📦 Archived</span>
            )}
            {repository.is_fork && (
              <span className={styles.forkBadge}>🔀 Fork</span>
            )}
          </div>

          {repository.description && (
            <p className={styles.modalDescription}>{repository.description}</p>
          )}

          {repository.topics?.length > 0 && (
            <div className={styles.headerTopics}>
              {repository.topics.slice(0, 8).map((topic) => (
                <span key={topic} className={styles.headerTopic}>
                  {topic}
                </span>
              ))}
              {repository.topics.length > 8 && (
                <span className={styles.headerTopicMore}>
                  +{repository.topics.length - 8}
                </span>
              )}
            </div>
          )}

          <div className={styles.headerStats}>
            <span className={styles.headerStat} title="Stars">
              <svg
                viewBox="0 0 24 24"
                fill="currentColor"
                aria-hidden="true"
                className={styles.headerStatIcon}
              >
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
              </svg>
              {formatNumber(repository.stars)}
            </span>
            <span className={styles.headerStat} title="Forks">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                aria-hidden="true"
                className={styles.headerStatIcon}
              >
                <circle cx="12" cy="18" r="3" />
                <circle cx="6" cy="6" r="3" />
                <circle cx="18" cy="6" r="3" />
                <path d="M18 9v1a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V9" />
                <line x1="12" y1="12" x2="12" y2="15" />
              </svg>
              {formatNumber(repository.forks)}
            </span>
            <span className={styles.headerStat} title="Total commits">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                aria-hidden="true"
                className={styles.headerStatIcon}
              >
                <circle cx="12" cy="12" r="4" />
                <line x1="1.05" y1="12" x2="7" y2="12" />
                <line x1="17.01" y1="12" x2="22.96" y2="12" />
              </svg>
              {formatNumber(repository.total_commits)} commits
            </span>
            <span className={styles.headerStat} title="Open issues">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                aria-hidden="true"
                className={styles.headerStatIcon}
              >
                <circle cx="12" cy="12" r="10" />
                <line x1="12" y1="8" x2="12" y2="12" />
                <line x1="12" y1="16" x2="12.01" y2="16" />
              </svg>
              {formatNumber(repository.open_issues)} issues
            </span>
            <span
              className={`${styles.headerStat} ${isRecent ? styles.headerStatRecent : ""}`}
              title={`Last push ${activityLabel}`}
            >
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                aria-hidden="true"
                className={styles.headerStatIcon}
              >
                <circle cx="12" cy="12" r="10" />
                <polyline points="12 6 12 12 16 14" />
              </svg>
              {activityLabel}
            </span>
          </div>
        </div>

        <button
          className={styles.closeButton}
          onClick={onClose}
          aria-label="Close"
        >
          ×
        </button>
      </div>
    </>
  );
}

export default RepositoryDetailHeader;
