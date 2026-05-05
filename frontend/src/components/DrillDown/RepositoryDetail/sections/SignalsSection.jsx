import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function SignalsSection({
  pullRequestSummary,
  securitySummary,
  openSecurityAlerts,
  expanded,
  onToggle,
  formatNumber,
  formatReason,
  getAvailabilityBadgeClass,
  getSecurityStateBadgeClass,
}) {
  return (
    <CollapsibleSection section="signals" title="Repository Signals" expanded={expanded} onToggle={onToggle}>
      <div className={styles.sectionContent}>
        <h4 className={styles.subsectionTitle}>Pull Requests</h4>
        <dl className={styles.detailList}>
          <div className={styles.detailItem}>
            <dt>Availability</dt>
            <dd>
              <span className={getAvailabilityBadgeClass(pullRequestSummary.availability)}>
                {pullRequestSummary.availability || "unavailable"}
              </span>
            </dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Open Pull Requests</dt>
            <dd>{formatNumber(pullRequestSummary.total_open || 0)}</dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Draft / Review Requested</dt>
            <dd>
              {formatNumber(pullRequestSummary.draft_count || 0)} / {formatNumber(pullRequestSummary.review_requested_count || 0)}
            </dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Oldest Open PR</dt>
            <dd>{pullRequestSummary.oldest_open_age_days != null ? `${pullRequestSummary.oldest_open_age_days} days` : "N/A"}</dd>
          </div>
          {formatReason(pullRequestSummary.reason) && (
            <div className={styles.detailItem}>
              <dt>Reason</dt>
              <dd className={styles.textMuted}>{formatReason(pullRequestSummary.reason)}</dd>
            </div>
          )}
        </dl>

        <h4 className={styles.subsectionTitle}>Security</h4>
        <dl className={styles.detailList}>
          <div className={styles.detailItem}>
            <dt>Availability</dt>
            <dd>
              <span className={getAvailabilityBadgeClass(securitySummary.availability)}>
                {securitySummary.availability || "unavailable"}
              </span>
            </dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Overall State</dt>
            <dd>
              <span className={getSecurityStateBadgeClass(securitySummary.overall_state)}>
                {securitySummary.overall_state ? securitySummary.overall_state.replace(/_/g, " ") : "unknown"}
              </span>
            </dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Open Alerts</dt>
            <dd>
              {formatNumber(openSecurityAlerts)}
              {securitySummary.active_alert_counts && (
                <div className={styles.textMuted}>
                  C: {securitySummary.active_alert_counts.critical || 0} | H: {securitySummary.active_alert_counts.high || 0} | M: {securitySummary.active_alert_counts.medium || 0} | L: {securitySummary.active_alert_counts.low || 0}
                </div>
              )}
            </dd>
          </div>
          {formatReason(securitySummary.reason) && (
            <div className={styles.detailItem}>
              <dt>Reason</dt>
              <dd className={styles.textMuted}>{formatReason(securitySummary.reason)}</dd>
            </div>
          )}
        </dl>

        {securitySummary.feature_status && (
          <div>
            <h4 className={styles.subsectionTitle}>Feature Status</h4>
            <div className={styles.badgeList}>
              {Object.entries(securitySummary.feature_status).map(([feature, status]) => (
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
              ))}
            </div>
          </div>
        )}
      </div>
    </CollapsibleSection>
  );
}

export default SignalsSection;
