import React, { useMemo } from "react";
import PropTypes from "prop-types";
import ChartWrapper from "@/components/Visualizations/ChartWrapper";

// Tier colours — WCAG AA verified against dashboard backgrounds
const TIER_COLORS = {
  core: "#0366d6",       // blue — accent
  supporting: "#28a745", // green — secondary
  archive: "#6a737d",    // grey — muted
};

const TIER_ORDER = ["core", "supporting", "archive"];
const TIER_LABELS = { core: "Core", supporting: "Supporting", archive: "Archive" };

export default function PortfolioBreakdown({ repositories }) {
  // Compute Core/Supporting/Archive counts client-side from classification field
  // per data-model.md PortfolioBreakdown shape
  const breakdown = useMemo(() => {
    const counts = { core: 0, supporting: 0, archive: 0 };
    repositories.forEach((r) => {
      const tier = (r.classification || "archive").toLowerCase();
      if (tier in counts) counts[tier]++;
    });
    const total = repositories.length || 1;
    return TIER_ORDER.map((tier) => ({
      tier,
      label: TIER_LABELS[tier],
      count: counts[tier],
      percentage: Math.round((counts[tier] / total) * 100),
      color: TIER_COLORS[tier],
    }));
  }, [repositories]);

  const chartData = useMemo(() => ({
    labels: breakdown.map((b) => `${b.label} (${b.count})`),
    datasets: [
      {
        data: breakdown.map((b) => b.count),
        backgroundColor: breakdown.map((b) => b.color),
        borderWidth: 0,
      },
    ],
  }), [breakdown]);

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: "bottom" },
      tooltip: {
        callbacks: {
          label: (ctx) => {
            const b = breakdown[ctx.dataIndex];
            return ` ${b.label}: ${b.count} repos (${b.percentage}%)`;
          },
        },
      },
    },
  };

  return (
    <div className="portfolio-breakdown">
      <h3 className="panel-title">Portfolio Signal Tiers</h3>
      <ChartWrapper type="doughnut" data={chartData} options={chartOptions} height={220} />
      <div className="tier-summary">
        {breakdown.map((b) => (
          <div key={b.tier} className="tier-summary-item">
            <span className="tier-dot" style={{ background: b.color }} />
            <span className="tier-label">{b.label}</span>
            <span className="tier-count">{b.count}</span>
            <span className="tier-pct">{b.percentage}%</span>
          </div>
        ))}
      </div>
    </div>
  );
}

PortfolioBreakdown.propTypes = {
  repositories: PropTypes.arrayOf(
    PropTypes.shape({
      classification: PropTypes.string,
    })
  ).isRequired,
};
