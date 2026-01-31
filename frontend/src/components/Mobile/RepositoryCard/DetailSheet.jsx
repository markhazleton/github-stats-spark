/**
 * DetailSheet Component
 *
 * Full-screen bottom sheet for displaying comprehensive repository details.
 * Accessed from expanded repository cards on mobile devices.
 *
 * Features:
 * - Full repository metadata (description, homepage, topics)
 * - Commit metrics and activity timeline
 * - Technology stack breakdown
 * - AI-generated summary (if available)
 * - Link to GitHub repository
 * - Share functionality
 * - Swipe-down to dismiss
 *
 * @example
 * <DetailSheet
 *   isOpen={isOpen}
 *   onClose={handleClose}
 *   repository={selectedRepo}
 * />
 */

import React from "react";
import BottomSheet from "../BottomSheet/BottomSheet";
import "./DetailSheet.css";

export function DetailSheet({ isOpen, onClose, repository }) {
  if (!repository) return null;

  const {
    name,
    description,
    language,
    stars = 0,
    forks = 0,
    watchers = 0,
    open_issues = 0,
    homepage,
    website_url,
    has_pages,
    screenshot,
    topics = [],
    commit_metrics = {},
    tech_stack = {},
    ai_summary,
    updated_at,
    created_at,
    license,
    size = 0,
  } = repository;

  /**
   * Format number with K/M suffixes
   */
  const formatNumber = (num) => {
    if (num >= 1000000) return `${(num / 1000000).toFixed(1)}M`;
    if (num >= 1000) return `${(num / 1000).toFixed(1)}K`;
    return num.toString();
  };

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
   * Format date to relative time
   */
  const formatDate = (dateString) => {
    if (!dateString) return "Unknown";
    const date = new Date(dateString);
    const now = new Date();
    const diffDays = Math.floor((now - date) / (1000 * 60 * 60 * 24));

    if (diffDays === 0) return "Today";
    if (diffDays === 1) return "Yesterday";
    if (diffDays < 7) return `${diffDays} days ago`;
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`;
    if (diffDays < 365) return `${Math.floor(diffDays / 30)} months ago`;
    return `${Math.floor(diffDays / 365)} years ago`;
  };

  /**
   * Format file size
   */
  const formatSize = (kb) => {
    if (kb >= 1024) return `${(kb / 1024).toFixed(1)} MB`;
    return `${kb} KB`;
  };

  /**
   * Share repository
   */
  const handleShare = async () => {
    const url = `https://github.com/${name}`;

    if (navigator.share) {
      try {
        await navigator.share({
          title: name,
          text: description || `Check out ${name} on GitHub`,
          url,
        });
      } catch (err) {
        // User cancelled or error occurred
        console.log("Share cancelled or failed:", err);
      }
    } else {
      // Fallback: copy to clipboard
      try {
        await navigator.clipboard.writeText(url);
        alert("Repository URL copied to clipboard!");
      } catch (err) {
        console.error("Failed to copy:", err);
      }
    }
  };

  return (
    <BottomSheet
      isOpen={isOpen}
      onClose={onClose}
      title={name}
      snapPoints={[0.9]}
      initialSnap={0}
    >
      <div className="detail-sheet">
        {/* Header with language badge */}
        {language && (
          <div className="detail-header">
            <span className="detail-language-badge">{language}</span>
          </div>
        )}

        {/* Description */}
        {description && (
          <section className="detail-section">
            <p className="detail-description">{description}</p>
          </section>
        )}

        {/* Website Screenshot */}
        {screenshot && (
          <section className="detail-section detail-screenshot-section">
            <a
              href={website_url || screenshot.url}
              target="_blank"
              rel="noopener noreferrer"
              className="detail-screenshot-link"
            >
              <img
                src={getScreenshotUrl(screenshot.path)}
                alt={`Screenshot of ${name} website`}
                className="detail-screenshot"
                loading="lazy"
              />
              <div className="detail-screenshot-overlay">
                <span>Visit Website →</span>
              </div>
            </a>
          </section>
        )}

        {/* Quick stats */}
        <section className="detail-section">
          <div className="detail-stats-grid">
            <div className="detail-stat">
              <span className="detail-stat-icon">⭐</span>
              <div className="detail-stat-content">
                <div className="detail-stat-value">{formatNumber(stars)}</div>
                <div className="detail-stat-label">Stars</div>
              </div>
            </div>

            <div className="detail-stat">
              <span className="detail-stat-icon">🔀</span>
              <div className="detail-stat-content">
                <div className="detail-stat-value">{formatNumber(forks)}</div>
                <div className="detail-stat-label">Forks</div>
              </div>
            </div>

            <div className="detail-stat">
              <span className="detail-stat-icon">👁️</span>
              <div className="detail-stat-content">
                <div className="detail-stat-value">
                  {formatNumber(watchers)}
                </div>
                <div className="detail-stat-label">Watchers</div>
              </div>
            </div>

            <div className="detail-stat">
              <span className="detail-stat-icon">🐛</span>
              <div className="detail-stat-content">
                <div className="detail-stat-value">
                  {formatNumber(open_issues)}
                </div>
                <div className="detail-stat-label">Issues</div>
              </div>
            </div>
          </div>
        </section>

        {/* Commit metrics */}
        {commit_metrics.total_commits > 0 && (
          <section className="detail-section">
            <h3 className="detail-section-title">Activity</h3>
            <div className="detail-metrics">
              <div className="detail-metric">
                <span className="detail-metric-label">Total Commits:</span>
                <span className="detail-metric-value">
                  {formatNumber(commit_metrics.total_commits)}
                </span>
              </div>
              {commit_metrics.commit_streak && (
                <div className="detail-metric">
                  <span className="detail-metric-label">Current Streak:</span>
                  <span className="detail-metric-value">
                    {commit_metrics.commit_streak} days
                  </span>
                </div>
              )}
            </div>
          </section>
        )}

        {/* Technology stack */}
        {tech_stack.languages && tech_stack.languages.length > 0 && (
          <section className="detail-section">
            <h3 className="detail-section-title">Technologies</h3>
            <div className="detail-tech-stack">
              {tech_stack.languages.map((lang, index) => (
                <span key={index} className="detail-tech-badge">
                  {lang}
                </span>
              ))}
            </div>
          </section>
        )}

        {/* Topics */}
        {topics.length > 0 && (
          <section className="detail-section">
            <h3 className="detail-section-title">Topics</h3>
            <div className="detail-topics">
              {topics.map((topic, index) => (
                <span key={index} className="detail-topic-tag">
                  #{topic}
                </span>
              ))}
            </div>
          </section>
        )}

        {/* AI Summary */}
        {ai_summary && (
          <section className="detail-section">
            <h3 className="detail-section-title">Summary</h3>
            <p className="detail-summary">{ai_summary}</p>
          </section>
        )}

        {/* Metadata */}
        <section className="detail-section detail-metadata">
          <h3 className="detail-section-title">Details</h3>
          <div className="detail-metadata-grid">
            <div className="detail-metadata-item">
              <span className="detail-metadata-label">Last Updated:</span>
              <span className="detail-metadata-value">
                {formatDate(updated_at)}
              </span>
            </div>
            <div className="detail-metadata-item">
              <span className="detail-metadata-label">Created:</span>
              <span className="detail-metadata-value">
                {formatDate(created_at)}
              </span>
            </div>
            {license && (
              <div className="detail-metadata-item">
                <span className="detail-metadata-label">License:</span>
                <span className="detail-metadata-value">{license}</span>
              </div>
            )}
            {size > 0 && (
              <div className="detail-metadata-item">
                <span className="detail-metadata-label">Size:</span>
                <span className="detail-metadata-value">
                  {formatSize(size)}
                </span>
              </div>
            )}
          </div>
        </section>

        {/* Actions */}
        <section className="detail-actions">
          <a
            href={`https://github.com/${name}`}
            target="_blank"
            rel="noopener noreferrer"
            className="detail-button detail-button-primary"
          >
            <span>View on GitHub</span>
            <span aria-hidden="true">→</span>
          </a>

          {homepage && (
            <a
              href={homepage}
              target="_blank"
              rel="noopener noreferrer"
              className="detail-button detail-button-secondary"
            >
              <span>Visit Homepage</span>
              <span aria-hidden="true">🔗</span>
            </a>
          )}

          {!homepage && website_url && (
            <a
              href={website_url}
              target="_blank"
              rel="noopener noreferrer"
              className="detail-button detail-button-secondary"
            >
              <span>{has_pages ? "GitHub Pages" : "Website"}</span>
              <span aria-hidden="true">📄</span>
            </a>
          )}

          <button
            onClick={handleShare}
            className="detail-button detail-button-secondary"
          >
            <span>Share</span>
            <span aria-hidden="true">📤</span>
          </button>
        </section>
      </div>
    </BottomSheet>
  );
}

export default DetailSheet;
