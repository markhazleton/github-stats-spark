import React, { Suspense, lazy, useCallback, useMemo } from "react";
import PropTypes from "prop-types";
import StatCards from "./StatCards";
import HealthChart from "./HealthChart";
import LoadingState from "@/components/Common/LoadingState";

const BarChart = lazy(() => import("./BarChart"));
const PieChart = lazy(() => import("./PieChart"));
const ScatterPlot = lazy(() => import("./ScatterPlot"));

export default function DashboardView({ repositories, profile, onRepoClick }) {
  const commitData = useMemo(() => {
    return [...repositories]
      .sort((a, b) => (b.total_commits || 0) - (a.total_commits || 0))
      .map((r) => ({
        name: r.name,
        value: r.total_commits || 0,
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
        r: Math.min(r.stars || 0, 20),
        language: r.language || "Unknown",
        fullData: r,
      }));
  }, [repositories]);

  const readmeCoverageData = useMemo(() => {
    return [...repositories]
      .filter((r) => r.has_readme != null)
      .sort((a, b) => Number(b.has_readme) - Number(a.has_readme))
      .map((r) => ({
        name: r.name,
        value: r.has_readme ? 1 : 0,
        language: r.language || "Unknown",
        fullData: r,
      }));
  }, [repositories]);

  const handleChartClick = useCallback(
    (data) => {
      if (data?.fullData && onRepoClick) {
        onRepoClick(data.fullData);
      }
    },
    [onRepoClick],
  );

  return (
    <div className="dashboard-panels">
      <StatCards repositories={repositories} profile={profile} />

      <div className="dashboard-grid">
        <div className="dashboard-panel dashboard-panel--wide">
          <Suspense fallback={<LoadingState message="Loading chart..." />}>
            <BarChart
              data={commitData}
              metricLabel="Total Commits"
              onBarClick={handleChartClick}
              horizontal={true}
              maxBars={30}
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
              sizeLabel="Stars"
              onPointClick={handleChartClick}
            />
          </Suspense>
        </div>

        <div className="dashboard-panel">
          <Suspense fallback={<LoadingState message="Loading chart..." />}>
            <BarChart
              data={readmeCoverageData}
              metricLabel="README Present"
              onBarClick={handleChartClick}
              horizontal={true}
              maxBars={30}
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
    </div>
  );
}

DashboardView.propTypes = {
  repositories: PropTypes.array.isRequired,
  profile: PropTypes.object,
  onRepoClick: PropTypes.func,
};
