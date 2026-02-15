import React from "react";
import PropTypes from "prop-types";
import ChartWrapper from "./ChartWrapper";
import { getLanguageColor } from "./StatCards";

export default function ScatterPlot({
  data,
  xAxisLabel = "Total Commits",
  yAxisLabel = "Average Commit Size",
  sizeLabel,
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

  const isBubble = data.some((item) => item.r != null);
  const chartType = isBubble ? "bubble" : "scatter";

  // Group data by language for colored legend
  const languageGroups = {};
  data.forEach((item) => {
    const lang = item.language || "Unknown";
    if (!languageGroups[lang]) languageGroups[lang] = [];
    languageGroups[lang].push(item);
  });

  const datasets = Object.entries(languageGroups).map(([lang, items]) => {
    const color = getLanguageColor(lang);
    return {
      label: lang,
      data: items.map((item) => ({
        x: item.x,
        y: item.y,
        r: isBubble ? Math.max(4, Math.min(25, (item.r || 0) / 4)) : undefined,
        name: item.name,
        language: item.language,
        rawR: item.r,
      })),
      backgroundColor: color + "99",
      borderColor: color,
      borderWidth: 2,
      pointRadius: isBubble ? undefined : 7,
      pointHoverRadius: isBubble ? undefined : 11,
      pointHoverBorderWidth: 3,
    };
  });

  const chartData = { datasets };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      mode: "nearest",
      intersect: false,
    },
    onClick: (event, elements) => {
      if (elements.length > 0 && onPointClick) {
        const { datasetIndex, index } = elements[0];
        const lang = Object.keys(languageGroups)[datasetIndex];
        const repoData = languageGroups[lang][index];
        onPointClick({ ...repoData, fullData: repoData.fullData || repoData });
      }
    },
    plugins: {
      legend: {
        display: Object.keys(languageGroups).length > 1,
        position: "top",
        labels: {
          padding: 12,
          font: { size: 11 },
          usePointStyle: true,
          boxWidth: 10,
        },
      },
      tooltip: {
        enabled: true,
        padding: 12,
        titleFont: { size: 14, weight: "bold" },
        bodyFont: { size: 14 },
        callbacks: {
          title: (context) => context[0]?.raw?.name || "",
          label: (context) => {
            const lines = [
              `${xAxisLabel}: ${context.parsed.x.toLocaleString()}`,
              `${yAxisLabel}: ${context.parsed.y.toLocaleString()}`,
            ];
            if (sizeLabel && context.raw?.rawR != null) {
              lines.push(`${sizeLabel}: ${context.raw.rawR.toFixed(1)}`);
            }
            return lines;
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
          font: { size: 12 },
          padding: { top: 8 },
        },
        grid: { display: true, color: "rgba(0, 0, 0, 0.05)" },
        ticks: {
          callback: (value) =>
            value >= 1000 ? `${(value / 1000).toFixed(1)}K` : value,
        },
      },
      y: {
        type: "linear",
        position: "left",
        title: {
          display: true,
          text: yAxisLabel,
          font: { size: 12 },
          padding: { bottom: 8 },
        },
        grid: { display: true, color: "rgba(0, 0, 0, 0.05)" },
        ticks: {
          callback: (value) =>
            value >= 1000 ? `${(value / 1000).toFixed(1)}K` : value,
        },
      },
    },
  };

  const title = sizeLabel
    ? `${yAxisLabel} vs ${xAxisLabel} (size = ${sizeLabel})`
    : `${yAxisLabel} vs ${xAxisLabel}`;

  return (
    <ChartWrapper
      type={chartType}
      data={chartData}
      options={options}
      title={title}
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
      r: PropTypes.number,
      language: PropTypes.string,
    }),
  ).isRequired,
  xAxisLabel: PropTypes.string,
  yAxisLabel: PropTypes.string,
  sizeLabel: PropTypes.string,
  onPointClick: PropTypes.func,
};
