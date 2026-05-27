import React from "react";
import PropTypes from "prop-types";
import ChartWrapper from "./ChartWrapper";

function scoreColor(score) {
  if (score >= 70) return "#28a745"; // green
  if (score >= 45) return "#ffc107"; // amber
  return "#fd7e14"; // orange
}

export default function HealthChart({
  repositories,
  onRepoClick,
  maxRepos = 15,
}) {
  if (!repositories || repositories.length === 0) {
    return (
      <ChartWrapper
        type="bar"
        data={{ labels: [], datasets: [] }}
        emptyMessage="No repository data available"
      />
    );
  }

  const sorted = [...repositories]
    .filter((r) => r.composite_score != null)
    .sort((a, b) => (b.composite_score || 0) - (a.composite_score || 0))
    .slice(0, maxRepos);

  const chartData = {
    labels: sorted.map((r) => r.name),
    datasets: [
      {
        label: "Composite Score",
        data: sorted.map((r) => +(r.composite_score ?? 0).toFixed(1)),
        backgroundColor: sorted.map((r) => scoreColor(r.composite_score ?? 0)),
        borderWidth: 0,
        borderRadius: 4,
        barThickness: 22,
        maxBarThickness: 30,
      },
    ],
  };

  const options = {
    indexAxis: "y",
    responsive: true,
    maintainAspectRatio: false,
    onClick: (event, elements) => {
      if (elements.length > 0 && onRepoClick) {
        const index = elements[0].index;
        onRepoClick({ fullData: sorted[index] });
      }
    },
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: (context) => {
            const repo = sorted[context.dataIndex];
            const flags = [
              repo.has_readme && "README",
              repo.has_license && "License",
              repo.has_ci_cd && "CI/CD",
              repo.has_tests && "Tests",
              repo.has_docs && "Docs",
            ].filter(Boolean);
            return [
              `Score: ${context.parsed.x.toFixed(1)} / 100`,
              `Features: ${flags.length ? flags.join(", ") : "none"}`,
              `Total commits: ${repo.total_commits?.toLocaleString() ?? "n/a"}`,
              `Stars: ${repo.stars ?? 0}  Forks: ${repo.forks ?? 0}`,
            ];
          },
        },
      },
    },
    scales: {
      x: {
        min: 0,
        max: 100,
        grid: { display: true, color: "rgba(128,128,128,0.1)" },
        ticks: { font: { size: 11 } },
        title: {
          display: true,
          text: "Composite Score (0–100)",
          font: { size: 11 },
        },
      },
      y: {
        grid: { display: false },
        ticks: { font: { size: 11 }, autoSkip: false },
      },
    },
  };

  return (
    <ChartWrapper
      type="bar"
      data={chartData}
      options={options}
      title="Composite Score — Top 15 Repositories"
      enableHorizontalScroll={false}
      maxDataPoints={maxRepos}
    />
  );
}

HealthChart.propTypes = {
  repositories: PropTypes.array.isRequired,
  onRepoClick: PropTypes.func,
  maxRepos: PropTypes.number,
};
