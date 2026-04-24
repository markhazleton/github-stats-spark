import React, { useMemo } from "react";
import PropTypes from "prop-types";
import ChartWrapper from "@/components/Visualizations/ChartWrapper";

const TIER_COLORS = {
  core: "#0366d6",
  supporting: "#28a745",
  archive: "#6a737d",
};

const MAX_REPOS = 20;

export default function SignalDistribution({ repositories, onRepoClick }) {
  const chartRepos = useMemo(() => {
    return [...repositories]
      .filter((r) => r.signal_score != null)
      .sort((a, b) => (b.signal_score || 0) - (a.signal_score || 0))
      .slice(0, MAX_REPOS);
  }, [repositories]);

  const chartData = useMemo(() => ({
    labels: chartRepos.map((r) => r.name),
    datasets: [
      {
        label: "Signal Score",
        data: chartRepos.map((r) => r.signal_score || 0),
        backgroundColor: chartRepos.map((r) =>
          TIER_COLORS[(r.classification || "archive").toLowerCase()] || TIER_COLORS.archive
        ),
        borderWidth: 0,
        barThickness: 14,
      },
    ],
  }), [chartRepos]);

  const chartOptions = {
    indexAxis: "y",
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: { min: 0, max: 100, title: { display: true, text: "Signal Score" } },
      y: { ticks: { font: { size: 11 } } },
    },
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: (ctx) => {
            const r = chartRepos[ctx.dataIndex];
            const tier = (r.classification || "archive");
            return ` Score: ${r.signal_score} | ${tier} | ${r.relevance || ""}`;
          },
          afterLabel: (ctx) => {
            const r = chartRepos[ctx.dataIndex];
            return r.notes ? ` ${r.notes}` : "";
          },
        },
      },
    },
    onClick: (_, elements) => {
      if (elements.length && onRepoClick) {
        onRepoClick(chartRepos[elements[0].index]);
      }
    },
  };

  const height = Math.max(200, chartRepos.length * 22 + 40);

  return (
    <div className="signal-distribution">
      <h3 className="panel-title">Signal Distribution</h3>
      <p className="panel-subtitle">Top {chartRepos.length} repositories by portfolio signal score</p>
      <ChartWrapper type="bar" data={chartData} options={chartOptions} height={height} />
    </div>
  );
}

SignalDistribution.propTypes = {
  repositories: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string,
      signal_score: PropTypes.number,
      classification: PropTypes.string,
      relevance: PropTypes.string,
      notes: PropTypes.string,
    })
  ).isRequired,
  onRepoClick: PropTypes.func,
};
