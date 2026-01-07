/**
 * ScatterPlot Component
 *
 * Renders a scatter plot visualization using Chart.js with touch interactions.
 * Shows relationship between two metrics (default: commits vs commit size).
 *
 * @component
 */

import React from "react";
import PropTypes from "prop-types";
import ChartWrapper from "./ChartWrapper";

const COLORS = [
  "#0366d6",
  "#28a745",
  "#6f42c1",
  "#fd8c73",
  "#ffd33d",
  "#ea4a5a",
  "#1b7cd3",
  "#79589f",
  "#f97583",
  "#ffdf5d",
];

/**
 * ScatterPlot Component
 *
 * @param {Object} props
 * @param {Array} props.data - Chart data array with {name, x, y} objects
 * @param {string} props.xAxisLabel - Label for X axis
 * @param {string} props.yAxisLabel - Label for Y axis
 * @param {Function} props.onPointClick - Handler for point click events
 */
export default function ScatterPlot({
  data,
  xAxisLabel = "Total Commits",
  yAxisLabel = "Average Commit Size",
  onPointClick,
}) {
  if (!data || data.length === 0) {
    return (
      <ChartWrapper
        type="scatter"
        data={{ datasets: [] }}
        emptyMessage="No data available for visualization"
      />
    );
  }

  // Prepare Chart.js data - scatter requires {x, y} format
  const chartData = {
    datasets: [
      {
        label: "Repositories",
        data: data.map((item) => ({
          x: item.x,
          y: item.y,
          name: item.name,
          language: item.language,
        })),
        backgroundColor: data.map((_, index) => COLORS[index % COLORS.length]),
        borderColor: data.map((_, index) => COLORS[index % COLORS.length]),
        borderWidth: 2,
        pointRadius: 8, // T044: Larger touch targets (increased from 6)
        pointHoverRadius: 12, // T044: Larger hover radius for touch
        pointHoverBorderWidth: 3,
      },
    ],
  };

  // Chart options
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      mode: "nearest", // T046: Touch-friendly interaction
      intersect: false,
    },
    onClick: (event, elements) => {
      if (elements.length > 0 && onPointClick) {
        const index = elements[0].index;
        const clickedData = data[index];
        onPointClick({ ...clickedData, fullData: clickedData });
      }
    },
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        enabled: true,
        padding: 12, // T044: Larger touch target area
        titleFont: {
          size: 14, // T047: Minimum 14px for mobile readability
          weight: "bold",
        },
        bodyFont: {
          size: 14, // T047: Minimum 14px for mobile readability
        },
        callbacks: {
          title: (context) => {
            return context[0]?.raw?.name || "";
          },
          label: (context) => {
            return [
              `${xAxisLabel}: ${context.parsed.x.toLocaleString()}`,
              `${yAxisLabel}: ${context.parsed.y.toLocaleString()}`,
            ];
          },
          afterLabel: (context) => {
            const language = context.raw?.language;
            return language ? `Language: ${language}` : "";
          },
        },
      },
    },
    scales: {
      x: {
        type: "linear",
        position: "bottom",
        title: {
          display: true,
          text: xAxisLabel,
          font: {
            size: 14,
            weight: "bold",
          },
          padding: { top: 10 },
        },
        grid: {
          display: true,
          color: "rgba(0, 0, 0, 0.05)",
        },
        ticks: {
          callback: (value) => {
            if (value >= 1000) {
              return `${(value / 1000).toFixed(1)}K`;
            }
            return value;
          },
        },
      },
      y: {
        type: "linear",
        position: "left",
        title: {
          display: true,
          text: yAxisLabel,
          font: {
            size: 14,
            weight: "bold",
          },
          padding: { bottom: 10 },
        },
        grid: {
          display: true,
          color: "rgba(0, 0, 0, 0.05)",
        },
        ticks: {
          callback: (value) => {
            if (value >= 1000) {
              return `${(value / 1000).toFixed(1)}K`;
            }
            return value;
          },
        },
      },
    },
  };

  return (
    <ChartWrapper
      type="scatter"
      data={chartData}
      options={options}
      title={`${xAxisLabel} vs ${yAxisLabel}`}
      enableHorizontalScroll={false}
    />
  );
}

ScatterPlot.propTypes = {
  data: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string,
      x: PropTypes.number,
      y: PropTypes.number,
      language: PropTypes.string,
    }),
  ).isRequired,
  xAxisLabel: PropTypes.string,
  yAxisLabel: PropTypes.string,
  onPointClick: PropTypes.func,
};
