import React, { useMemo, useState } from "react";
import PropTypes from "prop-types";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler,
} from "chart.js";
import { Line } from "react-chartjs-2";
import { computeTimelineData } from "../../services/metricsCalculator";
import styles from "./ActivityTimeline.module.css";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler,
);

/**
 * ActivityTimeline renders a multi-series line chart of weekly activity:
 *  - Series 1: Weekly commit count
 *  - Series 2: Active repositories per week
 *
 * Supports interactive legend toggle via Chart.js built-in behaviour.
 *
 * @param {Object} props
 * @param {Array}  props.weeklyActivity - Array of {week, label, commits, active_repos}
 * @param {string} [props.className]   - Extra CSS class
 */
export default function ActivityTimeline({ weeklyActivity, className }) {
  const [, setHiddenDatasets] = useState({});

  const chartData = useMemo(
    () => computeTimelineData(weeklyActivity),
    [weeklyActivity],
  );

  if (!Array.isArray(weeklyActivity) || weeklyActivity.length === 0) {
    return (
      <div className={`${styles.timeline} ${className ?? ""}`.trim()}>
        <p className={styles.empty}>No weekly activity data available.</p>
      </div>
    );
  }

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    interaction: {
      mode: "index",
      intersect: false,
    },
    plugins: {
      legend: {
        display: true,
        position: "top",
        labels: {
          usePointStyle: true,
          pointStyleWidth: 16,
          color: "var(--color-fg-default, #24292f)",
        },
        onClick: (e, legendItem, legend) => {
          const idx = legendItem.datasetIndex;
          const ci = legend.chart;
          if (ci.isDatasetVisible(idx)) {
            ci.hide(idx);
            legendItem.hidden = true;
          } else {
            ci.show(idx);
            legendItem.hidden = false;
          }
          setHiddenDatasets((prev) => ({
            ...prev,
            [idx]: !ci.isDatasetVisible(idx),
          }));
        },
      },
      tooltip: {
        callbacks: {
          title: (items) => `Week of ${items[0]?.label ?? ""}`,
        },
      },
    },
    scales: {
      x: {
        ticks: {
          maxTicksLimit: 13,
          color: "var(--color-fg-muted, #666)",
          maxRotation: 0,
        },
        grid: { display: false },
      },
      yCommits: {
        type: "linear",
        display: true,
        position: "left",
        title: {
          display: true,
          text: "Commits",
          color: "var(--chart-primary, #2563eb)",
        },
        ticks: { color: "var(--color-fg-muted, #666)" },
        grid: { color: "var(--color-border-muted, rgba(0,0,0,0.08))" },
      },
      yRepos: {
        type: "linear",
        display: true,
        position: "right",
        title: {
          display: true,
          text: "Active Repos",
          color: "var(--chart-secondary, #16a34a)",
        },
        ticks: { color: "var(--color-fg-muted, #666)" },
        grid: { display: false },
      },
    },
  };

  return (
    <div className={`${styles.timeline} ${className ?? ""}`.trim()}>
      <Line data={chartData} options={options} />
    </div>
  );
}

ActivityTimeline.propTypes = {
  weeklyActivity: PropTypes.arrayOf(
    PropTypes.shape({
      week: PropTypes.string.isRequired,
      label: PropTypes.string,
      commits: PropTypes.number,
      active_repos: PropTypes.number,
    }),
  ),
  className: PropTypes.string,
};
