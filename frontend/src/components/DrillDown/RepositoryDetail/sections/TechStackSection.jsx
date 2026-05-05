import styles from "../../RepositoryDetail.module.css";
import CollapsibleSection from "../CollapsibleSection";

function TechStackSection({ repository, expanded, onToggle, topDependencies, formatNumber, getDependencyBadgeClass }) {
  if (!repository.tech_stack) return null;

  return (
    <CollapsibleSection section="tech" title="Technology Stack" expanded={expanded} onToggle={onToggle}>
      <div className={styles.techStackGrid}>
        {repository.tech_stack.frameworks && repository.tech_stack.frameworks.length > 0 && (
          <div>
            <h4 className={styles.subsectionTitle}>Frameworks</h4>
            <div className={styles.badgeList}>
              {repository.tech_stack.frameworks.map((framework) => (
                <span key={framework} className={styles.badge}>
                  {framework}
                </span>
              ))}
            </div>
          </div>
        )}

        {repository.tech_stack.total_dependencies > 0 && (
          <div>
            <h4 className={styles.subsectionTitle}>Dependencies</h4>
            <dl className={styles.detailList}>
              <div className={styles.detailItem}>
                <dt>Total</dt>
                <dd>{formatNumber(repository.tech_stack.total_dependencies)}</dd>
              </div>
              <div className={styles.detailItem}>
                <dt>Outdated</dt>
                <dd className={repository.tech_stack.outdated_count > 0 ? styles.textWarning : ""}>
                  {formatNumber(repository.tech_stack.outdated_count)} ({repository.tech_stack.outdated_percentage}%)
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
                          : repository.tech_stack.currency_score >= 60
                            ? styles.scoreBarWarning
                            : styles.scoreBarError
                      }`}
                      style={{ width: `${repository.tech_stack.currency_score}%` }}
                    />
                  </div>
                  <span>{repository.tech_stack.currency_score}/100</span>
                </dd>
              </div>
              <div className={styles.detailItem}>
                <dt>Known Versions</dt>
                <dd>
                  {formatNumber(repository.tech_stack.known_versions_count)}/
                  {formatNumber(repository.tech_stack.total_dependencies)} (
                  {repository.tech_stack.version_coverage_percentage}%)
                </dd>
              </div>
              <div className={styles.detailItem}>
                <dt>Registry Coverage</dt>
                <dd>
                  {formatNumber(repository.tech_stack.resolved_latest_versions_count)}/
                  {formatNumber(repository.tech_stack.total_dependencies)} (
                  {repository.tech_stack.latest_version_coverage_percentage}%)
                </dd>
              </div>
            </dl>

            {topDependencies.length > 0 && (
              <div className={styles.dependencySection}>
                <h5 className={styles.dependencyHeading}>Dependency Snapshot</h5>
                <div className={styles.dependencyList}>
                  {topDependencies.map((dependency) => (
                    <div key={`${dependency.name}-${dependency.ecosystem}`} className={styles.dependencyRow}>
                      <div>
                        <div className={styles.dependencyNameRow}>
                          <span className={styles.dependencyName}>{dependency.name}</span>
                          <span className={getDependencyBadgeClass(dependency.status)}>
                            {dependency.status.replace(/_/g, " ")}
                          </span>
                        </div>
                        <div className={styles.dependencyMeta}>
                          {dependency.current_version_known
                            ? `${dependency.current_version}${dependency.latest_version ? ` -> ${dependency.latest_version}` : ""}`
                            : dependency.version_requirement || dependency.current_version}
                        </div>
                      </div>
                      <div className={styles.dependencyAux}>{dependency.source_file || dependency.ecosystem}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </CollapsibleSection>
  );
}

export default TechStackSection;
