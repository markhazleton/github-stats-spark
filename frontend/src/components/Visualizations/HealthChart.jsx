import React from "react";
import PropTypes from "prop-types";
import ChartWrapper from "./ChartWrapper";

const HEALTH_FEATURES = [
  { key: "has_readme", label: "README", color: "#28a745" },
  { key: "has_license", label: "License", color: "#0366d6" },
  { key: "has_ci_cd", label: "CI/CD", color: "#6f42c1" },
  { key: "has_tests", label: "Tests", color: "#fd8c73" },
  { key: "has_docs", label: "Docs", color: "#ffd33d" },
];

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
    .sort((a, b) => (b.composite_score || 0) - (a.composite_score || 0))
    .slice(0, maxRepos);

  const chartData = {
    labels: sorted.map((r) => r.name),
    datasets: HEALTH_FEATURES.map((feature) => ({
      label: feature.label,
      data: sorted.map((r) => (r[feature.key] ? 1 : 0)),
      backgroundColor: feature.color,
      borderWidth: 0,
      barThickness: 20,
    })),
  };

  const options = {
    indexAxis: "y",
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      mode: "nearest",
      intersect: false,
    },
    onClick: (event, elements) => {
      if (elements.length > 0 && onRepoClick) {
        const index = elements[0].index;
        onRepoClick({ fullData: sorted[index] });
      }
    },
    plugins: {
      legend: {
        display: true,
        position: "top",
        labels: {
          padding: 12,
          font: { size: 11 },
          usePointStyle: true,
          boxWidth: 10,
        },
      },
      tooltip: {
        callbacks: {
          label: (context) => {
            const repoIndex = context.dataIndex;
            const repo = sorted[repoIndex];
            const feature = HEALTH_FEATURES[context.datasetIndex];
            return `${feature.label}: ${repo[feature.key] ? "Yes" : "No"}`;
          },
        },
      },
    },
    scales: {
      x: {
        stacked: true,
        max: 5,
        grid: { display: false },
        ticks: {
          stepSize: 1,
          callback: (value) => value,
        },
        title: {
          display: true,
          text: "Features Present",
          font: { size: 11 },
        },
      },
      y: {
        stacked: true,
        grid: { display: false },
        ticks: {
          font: { size: 11 },
          autoSkip: false,
        },
      },
    },
  };

  return (
    <ChartWrapper
      type="bar"
      data={chartData}
      options={options}
      title="Repository Health (Top 15 by Spark Score)"
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
