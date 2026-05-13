import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function SignalsSection({
  pullRequestSummary,
  securitySummary,
  diagnosticsSummary,
  screenshotAudit,
  openSecurityAlerts,
  expanded,
  onToggle,
  formatNumber,
  formatReason,
  getAvailabilityBadgeClass,
  getSecurityStateBadgeClass,
}) {
  return (
    <CollapsibleSection
      section="signals"
      title="Repository Signals"
      expanded={expanded}
      onToggle={onToggle}
    >
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
            <dd>{formatNumber(pullRequestSummary.total_open || 0)}</dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Draft / Review Requested</dt>
            <dd>
              {formatNumber(pullRequestSummary.draft_count || 0)} /{" "}
              {formatNumber(pullRequestSummary.review_requested_count || 0)}
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
                  ? securitySummary.overall_state.replace(/_/g, " ")
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
                  C: {securitySummary.active_alert_counts.critical || 0} | H:{" "}
                  {securitySummary.active_alert_counts.high || 0} | M:{" "}
                  {securitySummary.active_alert_counts.medium || 0} | L:{" "}
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
            <h4 className={styles.subsectionTitle}>Feature Status</h4>
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

        <h4 className={styles.subsectionTitle}>Diagnostics</h4>
        <dl className={styles.detailList}>
          <div className={styles.detailItem}>
            <dt>Availability</dt>
            <dd>
              <span
                className={getAvailabilityBadgeClass(
                  diagnosticsSummary.availability,
                )}
              >
                {diagnosticsSummary.availability || "unavailable"}
              </span>
            </dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Issue Backlog</dt>
            <dd>
              {formatNumber(diagnosticsSummary.issues?.total_open || 0)} open
              {diagnosticsSummary.issues?.stale_over_30d != null && (
                <div className={styles.textMuted}>
                  Stale: {formatNumber(diagnosticsSummary.issues.stale_over_30d)}
                  / {formatNumber(diagnosticsSummary.issues.stale_over_90d || 0)}
                </div>
              )}
            </dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Workflow Health</dt>
            <dd>
              {formatNumber(diagnosticsSummary.actions?.failure_count || 0)}
              failed in {formatNumber(diagnosticsSummary.actions?.recent_runs || 0)} runs
              {diagnosticsSummary.actions?.last_run_conclusion && (
                <div className={styles.textMuted}>
                  Last run: {diagnosticsSummary.actions.last_run_conclusion}
                </div>
              )}
            </dd>
          </div>
          <div className={styles.detailItem}>
            <dt>Security Detail</dt>
            <dd>
              Dependabot {formatNumber(diagnosticsSummary.security?.dependabot?.open_alerts || 0)}
              open, code scanning {formatNumber(diagnosticsSummary.security?.code_scanning?.open_alerts || 0)} open
            </dd>
          </div>
        </dl>

        {screenshotAudit?.status && (
          <>
            <h4 className={styles.subsectionTitle}>Screenshot Audit</h4>
            <dl className={styles.detailList}>
              <div className={styles.detailItem}>
                <dt>Status</dt>
                <dd>
                  <span
                    className={getAvailabilityBadgeClass(
                      screenshotAudit.status === "ok" ? "available" : "partial",
                    )}
                  >
                    {screenshotAudit.status}
                  </span>
                </dd>
              </div>
              <div className={styles.detailItem}>
                <dt>Flags</dt>
                <dd>
                  {screenshotAudit.flags?.length > 0
                    ? screenshotAudit.flags.join(", ")
                    : "none"}
                </dd>
              </div>
              {screenshotAudit.http?.status_code != null && (
                <div className={styles.detailItem}>
                  <dt>HTTP</dt>
                  <dd>
                    {screenshotAudit.http.status_code}
                    {screenshotAudit.http.page_title
                      ? ` · ${screenshotAudit.http.page_title}`
                      : ""}
                  </dd>
                </div>
              )}
            </dl>
          </>
        )}
      </div>
    </CollapsibleSection>
  );
}

export default SignalsSection;
