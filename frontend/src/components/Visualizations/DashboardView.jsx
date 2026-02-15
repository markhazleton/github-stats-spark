import React, { Suspense, lazy, useMemo } from "react";
import PropTypes from "prop-types";
import StatCards from "./StatCards";
import HealthChart from "./HealthChart";
import LoadingState from "@/components/Common/LoadingState";

const BarChart = lazy(() => import("./BarChart"));
const PieChart = lazy(() => import("./PieChart"));
const ScatterPlot = lazy(() => import("./ScatterPlot"));

export default function DashboardView({ repositories, profile, onRepoClick }) {
  const scoreData = useMemo(() => {
    return [...repositories]
      .sort((a, b) => (b.composite_score || 0) - (a.composite_score || 0))
      .map((r) => ({
        name: r.name,
        value: r.composite_score || 0,
        language: r.language || "Unknown",
        fullData: r,
      }));
  }, [repositories]);

  const languageData = useMemo(() => {
    const counts = {};
    repositories.forEach((r) => {
      const lang = r.language || "Unknown";
      counts[lang] = (counts[lang] || 0) + 1;
    });
    return Object.entries(counts)
      .map(([name, value]) => ({ name, value }))
      .sort((a, b) => b.value - a.value);
  }, [repositories]);

  const activityScatterData = useMemo(() => {
    return repositories
      .filter((r) => r.age_days != null && r.total_commits != null)
      .map((r) => ({
        name: r.name,
        x: r.age_days,
        y: r.total_commits,
        r: r.composite_score || 0,
        language: r.language || "Unknown",
        fullData: r,
      }));
  }, [repositories]);

  const recentActivityData = useMemo(() => {
    return [...repositories]
      .filter((r) => (r.recent_commits_90d || 0) > 0)
      .sort((a, b) => (b.recent_commits_90d || 0) - (a.recent_commits_90d || 0))
      .slice(0, 15)
      .map((r) => ({
        name: r.name,
        value: r.recent_commits_90d || 0,
        language: r.language || "Unknown",
        fullData: r,
      }));
  }, [repositories]);

  const handleChartClick = (data) => {
    if (data?.fullData && onRepoClick) {
      onRepoClick(data.fullData);
    }
  };

  return (
    <div className="dashboard-panels">
      <StatCards repositories={repositories} profile={profile} />

      <div className="dashboard-grid">
        <div className="dashboard-panel dashboard-panel--wide">
          <Suspense fallback={<LoadingState message="Loading chart..." />}>
            <BarChart
              data={scoreData}
              metricLabel="Spark Score"
              onBarClick={handleChartClick}
              horizontal={true}
              maxBars={36}
            />
          </Suspense>
        </div>

        <div className="dashboard-panel">
          <Suspense fallback={<LoadingState message="Loading chart..." />}>
            <PieChart
              data={languageData}
              title="Language Distribution"
              doughnut={true}
              cutout={50}
            />
          </Suspense>
        </div>

        <div className="dashboard-panel dashboard-panel--wide">
          <Suspense fallback={<LoadingState message="Loading chart..." />}>
            <ScatterPlot
              data={activityScatterData}
              xAxisLabel="Repository Age (days)"
              yAxisLabel="Total Commits"
              sizeLabel="Spark Score"
              onPointClick={handleChartClick}
            />
          </Suspense>
        </div>

        <div className="dashboard-panel">
          <Suspense fallback={<LoadingState message="Loading chart..." />}>
            <BarChart
              data={recentActivityData}
              metricLabel="Commits (Last 90 Days)"
              onBarClick={handleChartClick}
              horizontal={true}
              maxBars={15}
            />
          </Suspense>
        </div>

        <div className="dashboard-panel dashboard-panel--wide">
          <HealthChart
            repositories={repositories}
            onRepoClick={handleChartClick}
            maxRepos={15}
          />
        </div>
      </div>

      <div className="spark-score-explainer">
        <h3>How the Spark Score Works</h3>
        <p>
          The Spark Score is a composite metric (0&ndash;100) that ranks
          repositories across three weighted dimensions:
        </p>

        <div className="score-factors">
          <div className="score-factor">
            <div className="score-factor-header">
              <span className="score-factor-weight">45%</span>
              <strong>Activity</strong>
            </div>
            <p>
              Measures commit frequency across three time windows: 90 days
              (50%), 180 days (30%), and 365 days (20%). A recency bonus of up
              to +30 points rewards repos pushed within the last week, while
              repos inactive for over a year receive a penalty.
            </p>
          </div>

          <div className="score-factor">
            <div className="score-factor-header">
              <span className="score-factor-weight">30%</span>
              <strong>Popularity</strong>
            </div>
            <p>
              Uses logarithmic scaling of stars, forks, and watchers (weighted
              1.0, 0.5, 0.3 respectively). The log scale ensures that a repo
              with 10 stars still scores meaningfully while preventing
              mega-repos from dominating.
            </p>
          </div>

          <div className="score-factor">
            <div className="score-factor-header">
              <span className="score-factor-weight">25%</span>
              <strong>Health</strong>
            </div>
            <p>
              Evaluates documentation (README presence), maturity (age + commit
              count), issue management (open issues vs. recent commits), and
              community engagement (fork-to-star ratio).
            </p>
          </div>
        </div>

        <h4>How to Improve Your Score</h4>
        <ul>
          <li>
            <strong>Commit regularly</strong> &mdash; Recent, consistent
            activity in the last 90 days has the highest impact on the Activity
            component.
          </li>
          <li>
            <strong>Push frequently</strong> &mdash; Repos pushed within the
            last 7 days get a +30 recency bonus; after 6 months the score drops
            sharply.
          </li>
          <li>
            <strong>Add a README</strong> &mdash; Worth 30 of the 100 Health
            points. The simplest single improvement you can make.
          </li>
          <li>
            <strong>Grow the community</strong> &mdash; Stars, forks, and
            watchers all feed the Popularity score. Open-source visibility
            matters.
          </li>
          <li>
            <strong>Manage issues</strong> &mdash; A low ratio of open issues to
            recent commits signals a well-maintained project.
          </li>
          <li>
            <strong>Avoid archiving</strong> &mdash; Archived repos receive a
            50&ndash;90% penalty. Keep projects active or clearly sunset them.
          </li>
        </ul>
      </div>
    </div>
  );
}

DashboardView.propTypes = {
  repositories: PropTypes.array.isRequired,
  profile: PropTypes.object,
  onRepoClick: PropTypes.func,
};
