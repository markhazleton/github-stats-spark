import { useEffect, useState, useRef } from "react";
import { useGesture } from "@use-gesture/react";
import styles from "./RepositoryDetail.module.css";

/**
 * RepositoryDetail Component
 *
 * Modal/overlay component that displays comprehensive details for a single repository.
 * Mobile-first with collapsible sections for better mobile UX.
 * Shows all attributes from the unified repositories.json including:
 * - Basic metadata (name, description, dates)
 * - Repository stats (stars, forks, watchers, issues)
 * - Commit history and metrics
 * - Language statistics
 * - Tech stack and dependencies (if available)
 * - AI summary (if available)
 * - Quality indicators (CI/CD, tests, docs, license)
 *
 * @component
 * @param {Object} props - Component props
 * @param {Object} props.repository - Repository object with all attributes
 * @param {Function} props.onClose - Callback to close the modal
 * @param {Function} [props.onNext] - Callback to navigate to next repository
 * @param {Function} [props.onPrevious] - Callback to navigate to previous repository
 */
function RepositoryDetail({ repository, onClose, onNext, onPrevious }) {
  const modalRef = useRef(null);

  // Track expanded/collapsed state for each modal section.
  const [expandedSections, setExpandedSections] = useState({
    summary: true, // Summary expanded by default
    website: true, // Website/screenshot expanded by default
    info: true,
    signals: true,
    commits: false,
    languages: false,
    tech: false,
    quality: false,
  });

  // Support swipe gestures for close and previous/next repository navigation.
  const bind = useGesture({
    onDrag: ({
      down,
      movement: [mx, my],
      direction: [xDir, yDir],
      velocity: [vx, vy],
    }) => {
      // Swipe down to dismiss (must be moving down with velocity)
      if (!down && yDir > 0 && vy > 0.3 && my > 50) {
        onClose();
      }
      // Swipe right to go to previous repository
      else if (!down && xDir > 0 && vx > 0.5 && mx > 100 && onPrevious) {
        onPrevious();
      }
      // Swipe left to go to next repository
      else if (!down && xDir < 0 && vx > 0.5 && mx < -100 && onNext) {
        onNext();
      }
    },
  });

  /**
   * Toggle section expansion
   */
  const toggleSection = (section) => {
    setExpandedSections((prev) => ({
      ...prev,
      [section]: !prev[section],
    }));
  };
  /**
   * Handle ESC key to close modal and Arrow keys for navigation
   */
  useEffect(() => {
    const handleKeyboard = (e) => {
      if (e.key === "Escape") {
        onClose();
      } else if (e.key === "ArrowRight" && onNext) {
        onNext();
      } else if (e.key === "ArrowLeft" && onPrevious) {
        onPrevious();
      }
    };

    document.addEventListener("keydown", handleKeyboard);
    return () => document.removeEventListener("keydown", handleKeyboard);
  }, [onClose, onNext, onPrevious]);

  /**
   * Get screenshot URL with base path
   */
  const getScreenshotUrl = (screenshotPath) => {
    if (!screenshotPath) return null;
    const basePath = import.meta.env.BASE_URL || "/";
    const normalizedPath = screenshotPath.replace(/\\/g, "/");
    return `${basePath}${normalizedPath}`;
  };

  /**
   * Format date to readable string
   */
  const formatDate = (dateString) => {
    if (!dateString) return "N/A";
    try {
      const date = new Date(dateString);
      if (isNaN(date.getTime())) return "N/A";
      return date.toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      });
    } catch {
      return "N/A";
    }
  };

  /**
   * Format relative date (e.g., "3 days ago")
   */
  const formatRelativeDate = (days) => {
    if (days == null) return "N/A";
    if (days === 0) return "Today";
    if (days === 1) return "Yesterday";
    if (days < 30) return `${days} days ago`;
    if (days < 365) return `${Math.floor(days / 30)} months ago`;
    return `${Math.floor(days / 365)} years ago`;
  };

  /**
   * Format number with commas
   */
  const formatNumber = (num) => {
    if (num == null || isNaN(num)) return "N/A";
    return num.toLocaleString();
  };

  /**
   * Format size with proper decimals
   */
  const formatSize = (size) => {
    if (size == null || isNaN(size)) return "N/A";
    return parseFloat(size).toFixed(1);
  };

  /**
   * Calculate percentage from language stats
   */
  const calculateLanguagePercentage = (bytes) => {
    if (!repository.language_stats) return 0;
    const total = Object.values(repository.language_stats).reduce(
      (sum, val) => sum + val,
      0,
    );
    return total > 0 ? ((bytes / total) * 100).toFixed(1) : 0;
  };

  const pullRequestSummary = repository.pull_request_summary || {};
  const securitySummary = repository.security_summary || {};
  const openSecurityAlerts =
    securitySummary.active_alert_counts?.total_open || 0;

  const formatReason = (reason) => {
    if (!reason || reason === "none") return null;
    return reason.replace(/_/g, " ");
  };

  const getAvailabilityBadgeClass = (availability) => {
    if (availability === "available") return styles.badgeSuccess;
    if (availability === "partial") return styles.badgeWarning;
    return styles.badgeError;
  };

  const getSecurityStateBadgeClass = (overallState) => {
    if (overallState === "clear") return styles.badgeSuccess;
    if (overallState === "alerts_detected") return styles.badgeError;
    return styles.badgeInfo;
  };

  return (
    <div className={styles.backdrop} onClick={onClose}>
      <div
        ref={modalRef}
        {...bind()}
        className={styles.modal}
        onClick={(e) => e.stopPropagation()}
      >
        <div className={styles.modalContent}>
          {/* Header */}
          <div className={styles.modalHeader}>
            {/* T066: Back button for mobile navigation */}
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
              <h2 className={styles.modalTitle}>{repository.name}</h2>
              {repository.description && (
                <p className={styles.modalDescription}>
                  {repository.description}
                </p>
              )}
            </div>
            <button
              className={styles.closeButton}
              onClick={onClose}
              aria-label="Close"
            >
              ×
            </button>
          </div>

          {/* Body */}
          <div className={styles.modalBody}>
            {/* Quick Stats Bar */}
            <div className={styles.statsBar}>
              <div className={styles.statItem}>
                <span className={styles.statValue}>
                  ⭐ {formatNumber(repository.stars)}
                </span>
                <span className={styles.statLabel}>Stars</span>
              </div>
              <div className={styles.statItem}>
                <span className={styles.statValue}>
                  🔀 {formatNumber(repository.forks)}
                </span>
                <span className={styles.statLabel}>Forks</span>
              </div>
              <div className={styles.statItem}>
                <span className={styles.statValue}>
                  👁️ {formatNumber(repository.watchers)}
                </span>
                <span className={styles.statLabel}>Watchers</span>
              </div>
              <div className={styles.statItem}>
                <span className={styles.statValue}>
                  🐛 {formatNumber(repository.open_issues)}
                </span>
                <span className={styles.statLabel}>Issues</span>
              </div>
              {repository.rank && (
                <div className={styles.statItem}>
                  <span className={styles.statValue}>
                    🏆 #{repository.rank}
                  </span>
                  <span className={styles.statLabel}>Rank</span>
                </div>
              )}
            </div>

            {/* AI Summary - Moved to top */}
            {repository.summary && (
              <section className={styles.section}>
                <h3
                  className={`${styles.sectionTitle} ${styles.collapsible}`}
                  onClick={() => toggleSection("summary")}
                  role="button"
                  tabIndex={0}
                  onKeyPress={(e) => {
                    if (e.key === "Enter" || e.key === " ") {
                      e.preventDefault();
                      toggleSection("summary");
                    }
                  }}
                  aria-expanded={expandedSections.summary}
                >
                  <span>Summary</span>
                  {repository.summary.ai_generated && (
                    <span className={styles.badgeAi}>✨ AI Generated</span>
                  )}
                  <span className={styles.chevron}>
                    {expandedSections.summary ? "▲" : "▼"}
                  </span>
                </h3>
                {expandedSections.summary && (
                  <div className={styles.sectionContent}>
                    <p className={styles.summaryText}>
                      {repository.summary.text}
                    </p>
                    {repository.summary.model_used && (
                      <div className={styles.textMuted}>
                        Generated by {repository.summary.model_used}
                        {repository.summary.confidence_score && (
                          <>
                            {" "}
                            • Confidence: {repository.summary.confidence_score}%
                          </>
                        )}
                      </div>
                    )}
                  </div>
                )}
              </section>
            )}

            {/* Website Screenshot Section */}
            {repository.screenshot && (
              <section className={styles.section}>
                <h3
                  className={`${styles.sectionTitle} ${styles.collapsible}`}
                  onClick={() => toggleSection("website")}
                  role="button"
                  tabIndex={0}
                  onKeyPress={(e) => {
                    if (e.key === "Enter" || e.key === " ") {
                      e.preventDefault();
                      toggleSection("website");
                    }
                  }}
                  aria-expanded={expandedSections.website}
                >
                  <span>🌐 Website Preview</span>
                  <span className={styles.chevron}>
                    {expandedSections.website ? "▲" : "▼"}
                  </span>
                </h3>
                {expandedSections.website && (
                  <div className={styles.sectionContent}>
                    <div className={styles.screenshotContainer}>
                      <a
                        href={
                          repository.website_url || repository.screenshot.url
                        }
                        target="_blank"
                        rel="noopener noreferrer"
                        className={styles.screenshotLink}
                      >
                        <img
                          src={getScreenshotUrl(repository.screenshot.path)}
                          alt={`Screenshot of ${repository.name} website`}
                          className={styles.screenshot}
                          loading="lazy"
                        />
                        <div className={styles.screenshotOverlay}>
                          <span>Visit Website →</span>
                        </div>
                      </a>
                    </div>
                    <div className={styles.screenshotMeta}>
                      <span className={styles.textMuted}>
                        Captured {formatDate(repository.screenshot.captured_at)}
                        {repository.screenshot.file_size_kb && (
                          <>
                            {" "}
                            • {repository.screenshot.file_size_kb.toFixed(1)} KB
                          </>
                        )}
                      </span>
                    </div>
                  </div>
                )}
              </section>
            )}

            {/* Main Content Grid */}
            <div className={styles.contentGrid}>
              {/* Left Column */}
              <div className={styles.column}>
                {/* Repository Info Section */}
                <section className={styles.section}>
                  <h3
                    className={`${styles.sectionTitle} ${styles.collapsible}`}
                    onClick={() => toggleSection("info")}
                    role="button"
                    tabIndex={0}
                    onKeyPress={(e) => {
                      if (e.key === "Enter" || e.key === " ") {
                        e.preventDefault();
                        toggleSection("info");
                      }
                    }}
                    aria-expanded={expandedSections.info}
                  >
                    <span>Repository Info</span>
                    <span className={styles.chevron}>
                      {expandedSections.info ? "▲" : "▼"}
                    </span>
                  </h3>
                  {expandedSections.info && (
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
                              (
                              {formatRelativeDate(
                                repository.days_since_last_push,
                              )}
                              )
                            </span>
                          )}
                        </dd>
                      </div>
                      <div className={styles.detailItem}>
                        <dt>Age</dt>
                        <dd>
                          {repository.age_days
                            ? `${repository.age_days} days`
                            : "N/A"}
                        </dd>
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
                              {repository.homepage
                                ? "🌐 Homepage"
                                : "📄 GitHub Pages"}{" "}
                              →
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
                  )}
                </section>

                {/* Quality Indicators */}
                <section className={styles.section}>
                  <h3
                    className={`${styles.sectionTitle} ${styles.collapsible}`}
                    onClick={() => toggleSection("quality")}
                    role="button"
                    tabIndex={0}
                    onKeyPress={(e) => {
                      if (e.key === "Enter" || e.key === " ") {
                        e.preventDefault();
                        toggleSection("quality");
                      }
                    }}
                    aria-expanded={expandedSections.quality}
                  >
                    <span>Quality Indicators</span>
                    <span className={styles.chevron}>
                      {expandedSections.quality ? "▲" : "▼"}
                    </span>
                  </h3>
                  {expandedSections.quality && (
                    <div className={styles.badgeGrid}>
                      <span
                        className={
                          repository.has_readme
                            ? styles.badgeSuccess
                            : styles.badgeError
                        }
                      >
                        {repository.has_readme ? "✓" : "✗"} README
                      </span>
                      <span
                        className={
                          repository.has_license
                            ? styles.badgeSuccess
                            : styles.badgeError
                        }
                      >
                        {repository.has_license ? "✓" : "✗"} License
                      </span>
                      <span
                        className={
                          repository.has_ci_cd
                            ? styles.badgeSuccess
                            : styles.badgeError
                        }
                      >
                        {repository.has_ci_cd ? "✓" : "✗"} CI/CD
                      </span>
                      <span
                        className={
                          repository.has_tests
                            ? styles.badgeSuccess
                            : styles.badgeError
                        }
                      >
                        {repository.has_tests ? "✓" : "✗"} Tests
                      </span>
                      <span
                        className={
                          repository.has_docs
                            ? styles.badgeSuccess
                            : styles.badgeError
                        }
                      >
                        {repository.has_docs ? "✓" : "✗"} Docs
                      </span>
                      {repository.is_archived && (
                        <span className={styles.badgeWarning}>📦 Archived</span>
                      )}
                      {repository.is_fork && (
                        <span className={styles.badgeInfo}>🔀 Fork</span>
                      )}
                    </div>
                  )}
                </section>

                {/* Language Statistics */}
                {repository.language_stats &&
                  Object.keys(repository.language_stats).length > 0 && (
                    <section className={styles.section}>
                      <h3
                        className={`${styles.sectionTitle} ${styles.collapsible}`}
                        onClick={() => toggleSection("languages")}
                        role="button"
                        tabIndex={0}
                        onKeyPress={(e) => {
                          if (e.key === "Enter" || e.key === " ") {
                            e.preventDefault();
                            toggleSection("languages");
                          }
                        }}
                        aria-expanded={expandedSections.languages}
                      >
                        <span>Languages ({repository.language_count})</span>
                        <span className={styles.chevron}>
                          {expandedSections.languages ? "▲" : "▼"}
                        </span>
                      </h3>
                      {expandedSections.languages && (
                        <div className={styles.languageList}>
                          {Object.entries(repository.language_stats)
                            .sort(([, a], [, b]) => b - a)
                            .slice(0, 10)
                            .map(([lang, bytes]) => (
                              <div key={lang} className={styles.languageItem}>
                                <div className={styles.languageHeader}>
                                  <span className={styles.languageName}>
                                    {lang}
                                  </span>
                                  <span className={styles.languagePercent}>
                                    {calculateLanguagePercentage(bytes)}%
                                  </span>
                                </div>
                                <div className={styles.languageBar}>
                                  <div
                                    className={styles.languageBarFill}
                                    style={{
                                      width: `${calculateLanguagePercentage(bytes)}%`,
                                    }}
                                  />
                                </div>
                              </div>
                            ))}
                        </div>
                      )}
                    </section>
                  )}
              </div>

              {/* Right Column */}
              <div className={styles.column}>
                <section className={styles.section}>
                  <h3
                    className={`${styles.sectionTitle} ${styles.collapsible}`}
                    onClick={() => toggleSection("signals")}
                    role="button"
                    tabIndex={0}
                    onKeyPress={(e) => {
                      if (e.key === "Enter" || e.key === " ") {
                        e.preventDefault();
                        toggleSection("signals");
                      }
                    }}
                    aria-expanded={expandedSections.signals}
                  >
                    <span>Repository Signals</span>
                    <span className={styles.chevron}>
                      {expandedSections.signals ? "▲" : "▼"}
                    </span>
                  </h3>
                  {expandedSections.signals && (
                    <div className={styles.sectionContent}>
                      <h4 className={styles.subsectionTitle}>Pull Requests</h4>
                      <dl className={styles.detailList}>
                        <div className={styles.detailItem}>
                          <dt>Availability</dt>
                          <dd>
                            <span
                              className={getAvailabilityBadgeClass(
                                pullRequestSummary.availability,
                              )}
                            >
                              {pullRequestSummary.availability || "unavailable"}
                            </span>
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Open Pull Requests</dt>
                          <dd>
                            {formatNumber(pullRequestSummary.total_open || 0)}
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Draft / Review Requested</dt>
                          <dd>
                            {formatNumber(pullRequestSummary.draft_count || 0)}{" "}
                            /{" "}
                            {formatNumber(
                              pullRequestSummary.review_requested_count || 0,
                            )}
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Oldest Open PR</dt>
                          <dd>
                            {pullRequestSummary.oldest_open_age_days != null
                              ? `${pullRequestSummary.oldest_open_age_days} days`
                              : "N/A"}
                          </dd>
                        </div>
                        {formatReason(pullRequestSummary.reason) && (
                          <div className={styles.detailItem}>
                            <dt>Reason</dt>
                            <dd className={styles.textMuted}>
                              {formatReason(pullRequestSummary.reason)}
                            </dd>
                          </div>
                        )}
                      </dl>

                      <h4 className={styles.subsectionTitle}>Security</h4>
                      <dl className={styles.detailList}>
                        <div className={styles.detailItem}>
                          <dt>Availability</dt>
                          <dd>
                            <span
                              className={getAvailabilityBadgeClass(
                                securitySummary.availability,
                              )}
                            >
                              {securitySummary.availability || "unavailable"}
                            </span>
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Overall State</dt>
                          <dd>
                            <span
                              className={getSecurityStateBadgeClass(
                                securitySummary.overall_state,
                              )}
                            >
                              {securitySummary.overall_state
                                ? securitySummary.overall_state.replace(
                                    /_/g,
                                    " ",
                                  )
                                : "unknown"}
                            </span>
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Open Alerts</dt>
                          <dd>
                            {formatNumber(openSecurityAlerts)}
                            {securitySummary.active_alert_counts && (
                              <div className={styles.textMuted}>
                                C:{" "}
                                {securitySummary.active_alert_counts.critical ||
                                  0}{" "}
                                | H:{" "}
                                {securitySummary.active_alert_counts.high || 0}{" "}
                                | M:{" "}
                                {securitySummary.active_alert_counts.medium ||
                                  0}{" "}
                                | L:{" "}
                                {securitySummary.active_alert_counts.low || 0}
                              </div>
                            )}
                          </dd>
                        </div>
                        {formatReason(securitySummary.reason) && (
                          <div className={styles.detailItem}>
                            <dt>Reason</dt>
                            <dd className={styles.textMuted}>
                              {formatReason(securitySummary.reason)}
                            </dd>
                          </div>
                        )}
                      </dl>

                      {securitySummary.feature_status && (
                        <div>
                          <h4 className={styles.subsectionTitle}>
                            Feature Status
                          </h4>
                          <div className={styles.badgeList}>
                            {Object.entries(securitySummary.feature_status).map(
                              ([feature, status]) => (
                                <span
                                  key={feature}
                                  className={
                                    status === "enabled"
                                      ? styles.badgeSuccess
                                      : status === "disabled"
                                        ? styles.badgeError
                                        : styles.badgeInfo
                                  }
                                  title={feature.replace(/_/g, " ")}
                                >
                                  {feature.replace(/_/g, " ")}: {status}
                                </span>
                              ),
                            )}
                          </div>
                        </div>
                      )}
                    </div>
                  )}
                </section>

                {/* Commit History */}
                {repository.commit_history && (
                  <section className={styles.section}>
                    <h3
                      className={`${styles.sectionTitle} ${styles.collapsible}`}
                      onClick={() => toggleSection("commits")}
                      role="button"
                      tabIndex={0}
                      onKeyPress={(e) => {
                        if (e.key === "Enter" || e.key === " ") {
                          e.preventDefault();
                          toggleSection("commits");
                        }
                      }}
                      aria-expanded={expandedSections.commits}
                    >
                      <span>Commit Activity</span>
                      <span className={styles.chevron}>
                        {expandedSections.commits ? "▲" : "▼"}
                      </span>
                    </h3>
                    {expandedSections.commits && (
                      <dl className={styles.detailList}>
                        <div className={styles.detailItem}>
                          <dt>Total Commits</dt>
                          <dd className={styles.highlight}>
                            {formatNumber(
                              repository.commit_history.total_commits,
                            )}
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Last 90 Days</dt>
                          <dd>
                            {formatNumber(repository.commit_history.recent_90d)}
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Last 180 Days</dt>
                          <dd>
                            {formatNumber(
                              repository.commit_history.recent_180d,
                            )}
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Last 365 Days</dt>
                          <dd>
                            {formatNumber(
                              repository.commit_history.recent_365d,
                            )}
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>First Commit</dt>
                          <dd>
                            {formatDate(
                              repository.commit_history.first_commit_date,
                            )}
                          </dd>
                        </div>
                        <div className={styles.detailItem}>
                          <dt>Last Commit</dt>
                          <dd>
                            {formatDate(
                              repository.commit_history.last_commit_date,
                            )}
                          </dd>
                        </div>
                        {repository.commit_velocity != null && (
                          <div className={styles.detailItem}>
                            <dt>Commit Velocity</dt>
                            <dd>
                              {formatSize(repository.commit_velocity)}{" "}
                              commits/month
                            </dd>
                          </div>
                        )}
                      </dl>
                    )}
                  </section>
                )}

                {/* Commit Metrics */}
                <section className={styles.section}>
                  <h3 className={styles.sectionTitle}>Commit Metrics</h3>
                  <dl className={styles.detailList}>
                    <div className={styles.detailItem}>
                      <dt>Average Commit Size</dt>
                      <dd>
                        {formatSize(
                          repository.commit_metrics?.avg_size ||
                            repository.avg_commit_size,
                        )}
                      </dd>
                    </div>
                    {(repository.commit_metrics?.largest_commit ||
                      repository.largest_commit) && (
                      <div className={styles.detailItem}>
                        <dt>Largest Commit</dt>
                        <dd>
                          {formatSize(
                            (
                              repository.commit_metrics?.largest_commit ||
                              repository.largest_commit
                            ).size,
                          )}
                          <div className={styles.textMuted}>
                            {(
                              repository.commit_metrics?.largest_commit ||
                              repository.largest_commit
                            ).sha?.substring(0, 7)}{" "}
                            •{" "}
                            {formatDate(
                              (
                                repository.commit_metrics?.largest_commit ||
                                repository.largest_commit
                              ).date,
                            )}
                          </div>
                          <div className={styles.textMuted}>
                            {formatNumber(
                              (
                                repository.commit_metrics?.largest_commit ||
                                repository.largest_commit
                              ).files_changed,
                            )}{" "}
                            files • +
                            {formatNumber(
                              (
                                repository.commit_metrics?.largest_commit ||
                                repository.largest_commit
                              ).lines_added,
                            )}{" "}
                            / -
                            {formatNumber(
                              (
                                repository.commit_metrics?.largest_commit ||
                                repository.largest_commit
                              ).lines_deleted,
                            )}
                          </div>
                        </dd>
                      </div>
                    )}
                    {(repository.commit_metrics?.smallest_commit ||
                      repository.smallest_commit) && (
                      <div className={styles.detailItem}>
                        <dt>Smallest Commit</dt>
                        <dd>
                          {formatSize(
                            (
                              repository.commit_metrics?.smallest_commit ||
                              repository.smallest_commit
                            ).size,
                          )}
                          <div className={styles.textMuted}>
                            {(
                              repository.commit_metrics?.smallest_commit ||
                              repository.smallest_commit
                            ).sha?.substring(0, 7)}{" "}
                            •{" "}
                            {formatDate(
                              (
                                repository.commit_metrics?.smallest_commit ||
                                repository.smallest_commit
                              ).date,
                            )}
                          </div>
                        </dd>
                      </div>
                    )}
                  </dl>
                </section>

                {/* Activity Metrics */}
                <section className={styles.section}>
                  <h3 className={styles.sectionTitle}>Activity Metrics</h3>
                  <dl className={styles.detailList}>
                    {repository.contributors_count != null && (
                      <div className={styles.detailItem}>
                        <dt>Contributors</dt>
                        <dd>{formatNumber(repository.contributors_count)}</dd>
                      </div>
                    )}
                    {repository.release_count != null && (
                      <div className={styles.detailItem}>
                        <dt>Releases</dt>
                        <dd>{formatNumber(repository.release_count)}</dd>
                      </div>
                    )}
                    {repository.latest_release_date && (
                      <div className={styles.detailItem}>
                        <dt>Latest Release</dt>
                        <dd>{formatDate(repository.latest_release_date)}</dd>
                      </div>
                    )}
                  </dl>
                </section>

                {/* Ranking */}
                {repository.composite_score != null && (
                  <section className={styles.section}>
                    <h3 className={styles.sectionTitle}>Ranking</h3>
                    <dl className={styles.detailList}>
                      {repository.rank && (
                        <div className={styles.detailItem}>
                          <dt>Rank</dt>
                          <dd className={styles.highlight}>
                            #{repository.rank}
                          </dd>
                        </div>
                      )}
                      <div className={styles.detailItem}>
                        <dt>Composite Score</dt>
                        <dd>{repository.composite_score.toFixed(2)}</dd>
                      </div>
                    </dl>
                  </section>
                )}
              </div>
            </div>

            {/* Full Width Sections */}

            {/* Tech Stack */}
            {repository.tech_stack && (
              <section className={styles.section}>
                <h3
                  className={`${styles.sectionTitle} ${styles.collapsible}`}
                  onClick={() => toggleSection("tech")}
                  role="button"
                  tabIndex={0}
                  onKeyPress={(e) => {
                    if (e.key === "Enter" || e.key === " ") {
                      e.preventDefault();
                      toggleSection("tech");
                    }
                  }}
                  aria-expanded={expandedSections.tech}
                >
                  <span>Technology Stack</span>
                  <span className={styles.chevron}>
                    {expandedSections.tech ? "▲" : "▼"}
                  </span>
                </h3>
                {expandedSections.tech && (
                  <div className={styles.techStackGrid}>
                    {repository.tech_stack.frameworks &&
                      repository.tech_stack.frameworks.length > 0 && (
                        <div>
                          <h4 className={styles.subsectionTitle}>Frameworks</h4>
                          <div className={styles.badgeList}>
                            {repository.tech_stack.frameworks.map(
                              (framework) => (
                                <span key={framework} className={styles.badge}>
                                  {framework}
                                </span>
                              ),
                            )}
                          </div>
                        </div>
                      )}

                    {repository.tech_stack.total_dependencies > 0 && (
                      <div>
                        <h4 className={styles.subsectionTitle}>Dependencies</h4>
                        <dl className={styles.detailList}>
                          <div className={styles.detailItem}>
                            <dt>Total</dt>
                            <dd>
                              {formatNumber(
                                repository.tech_stack.total_dependencies,
                              )}
                            </dd>
                          </div>
                          <div className={styles.detailItem}>
                            <dt>Outdated</dt>
                            <dd
                              className={
                                repository.tech_stack.outdated_count > 0
                                  ? styles.textWarning
                                  : ""
                              }
                            >
                              {formatNumber(
                                repository.tech_stack.outdated_count,
                              )}
                              ({repository.tech_stack.outdated_percentage}%)
                            </dd>
                          </div>
                          <div className={styles.detailItem}>
                            <dt>Currency Score</dt>
                            <dd>
                              <div className={styles.scoreBar}>
                                <div
                                  className={`${styles.scoreBarFill} ${
                                    repository.tech_stack.currency_score >= 80
                                      ? styles.scoreBarSuccess
                                      : repository.tech_stack.currency_score >=
                                          60
                                        ? styles.scoreBarWarning
                                        : styles.scoreBarError
                                  }`}
                                  style={{
                                    width: `${repository.tech_stack.currency_score}%`,
                                  }}
                                />
                              </div>
                              <span>
                                {repository.tech_stack.currency_score}/100
                              </span>
                            </dd>
                          </div>
                        </dl>
                      </div>
                    )}
                  </div>
                )}
              </section>
            )}
          </div>

          {/* Footer with Navigation */}
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
        </div>
      </div>
    </div>
  );
}

export default RepositoryDetail;
