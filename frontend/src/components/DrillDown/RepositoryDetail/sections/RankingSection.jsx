import styles from "../../RepositoryDetail.module.css";

function RankingSection({ repository }) {
  if (repository.composite_score == null) return null;

  return (
    <section className={styles.section}>
      <h3 className={styles.sectionTitle}>Ranking</h3>
      <dl className={styles.detailList}>
        {repository.rank && (
          <div className={styles.detailItem}>
            <dt>Rank</dt>
            <dd className={styles.highlight}>#{repository.rank}</dd>
          </div>
        )}
        <div className={styles.detailItem}>
          <dt>Composite Score</dt>
          <dd>{repository.composite_score.toFixed(2)}</dd>
        </div>
      </dl>
    </section>
  );
}

export default RankingSection;
