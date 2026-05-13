import { useMemo } from "react";
import styles from "./RepositoryDetail.module.css";
import { useRepositoryDetailInteractions } from "./RepositoryDetail/hooks/useRepositoryDetailInteractions";
import { useSectionToggles } from "./RepositoryDetail/hooks/useSectionToggles";
import {
  calculateLanguagePercentage,
  formatDate,
  formatNumber,
  formatReason,
  formatRelativeDate,
  formatSize,
  getAvailabilityBadgeClass,
  getDependencyBadgeClass,
  getScreenshotUrl,
  getSecurityStateBadgeClass,
  getTopDependencies,
} from "./RepositoryDetail/utils/repositoryDetailUtils";
import RepositoryDetailHeader from "./RepositoryDetail/sections/RepositoryDetailHeader";
import RepositoryDetailFooter from "./RepositoryDetail/sections/RepositoryDetailFooter";
import SummarySection from "./RepositoryDetail/sections/SummarySection";
import WebsiteSection from "./RepositoryDetail/sections/WebsiteSection";
import RepositoryInfoSection from "./RepositoryDetail/sections/RepositoryInfoSection";
import QualitySection from "./RepositoryDetail/sections/QualitySection";
import LanguagesSection from "./RepositoryDetail/sections/LanguagesSection";
import SignalsSection from "./RepositoryDetail/sections/SignalsSection";
import CommitHistorySection from "./RepositoryDetail/sections/CommitHistorySection";
import CommitMetricsSection from "./RepositoryDetail/sections/CommitMetricsSection";
import ActivityMetricsSection from "./RepositoryDetail/sections/ActivityMetricsSection";
import RankingSection from "./RepositoryDetail/sections/RankingSection";
import TechStackSection from "./RepositoryDetail/sections/TechStackSection";

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
  const { expandedSections, toggleSection } = useSectionToggles();
  const bind = useRepositoryDetailInteractions({ onClose, onNext, onPrevious });

  const pullRequestSummary = repository.pull_request_summary || {};
  const securitySummary = repository.security_summary || {};
  const openSecurityAlerts =
    securitySummary.active_alert_counts?.total_open || 0;
  const topDependencies = useMemo(
    () => getTopDependencies(repository),
    [repository],
  );

  return (
    <div className={styles.backdrop} onClick={onClose}>
      <div
        {...bind()}
        className={styles.modal}
        onClick={(e) => e.stopPropagation()}
      >
        <div className={styles.modalContent}>
          <RepositoryDetailHeader
            repository={repository}
            onClose={onClose}
            formatNumber={formatNumber}
          />

          {/* Body */}
          <div className={styles.modalBody}>
            <SummarySection
              summary={repository.ai_summary}
              expanded={expandedSections.summary}
              onToggle={toggleSection}
            />

            <WebsiteSection
              repository={repository}
              expanded={expandedSections.website}
              onToggle={toggleSection}
              formatDate={formatDate}
              getScreenshotUrl={getScreenshotUrl}
            />

            {/* Main Content Grid */}
            <div className={styles.contentGrid}>
              {/* Left Column */}
              <div className={styles.column}>
                <RepositoryInfoSection
                  repository={repository}
                  expanded={expandedSections.info}
                  onToggle={toggleSection}
                  formatDate={formatDate}
                  formatRelativeDate={formatRelativeDate}
                  formatNumber={formatNumber}
                />

                <QualitySection
                  repository={repository}
                  expanded={expandedSections.quality}
                  onToggle={toggleSection}
                />

                <LanguagesSection
                  repository={repository}
                  expanded={expandedSections.languages}
                  onToggle={toggleSection}
                  calculateLanguagePercentage={(bytes) =>
                    calculateLanguagePercentage(
                      repository.language_stats,
                      bytes,
                    )
                  }
                />
              </div>

              {/* Right Column */}
              <div className={styles.column}>
                <SignalsSection
                  pullRequestSummary={pullRequestSummary}
                  securitySummary={securitySummary}
                  openSecurityAlerts={openSecurityAlerts}
                  expanded={expandedSections.signals}
                  onToggle={toggleSection}
                  formatNumber={formatNumber}
                  formatReason={formatReason}
                  getAvailabilityBadgeClass={(availability) =>
                    getAvailabilityBadgeClass(styles, availability)
                  }
                  getSecurityStateBadgeClass={(overallState) =>
                    getSecurityStateBadgeClass(styles, overallState)
                  }
                />

                <CommitHistorySection
                  repository={repository}
                  expanded={expandedSections.commits}
                  onToggle={toggleSection}
                  formatDate={formatDate}
                  formatNumber={formatNumber}
                  formatSize={formatSize}
                />

                <CommitMetricsSection
                  repository={repository}
                  formatDate={formatDate}
                  formatNumber={formatNumber}
                  formatSize={formatSize}
                />

                <ActivityMetricsSection
                  repository={repository}
                  formatDate={formatDate}
                  formatNumber={formatNumber}
                />

                <RankingSection repository={repository} />
              </div>
            </div>

            {/* Full Width Sections */}

            <TechStackSection
              repository={repository}
              expanded={expandedSections.tech}
              onToggle={toggleSection}
              topDependencies={topDependencies}
              formatNumber={formatNumber}
              getDependencyBadgeClass={(status) =>
                getDependencyBadgeClass(styles, status)
              }
            />
          </div>

          <RepositoryDetailFooter
            onClose={onClose}
            onNext={onNext}
            onPrevious={onPrevious}
          />
        </div>
      </div>
    </div>
  );
}

export default RepositoryDetail;
