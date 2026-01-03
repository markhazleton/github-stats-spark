/**
 * PieChart Component
 * 
 * Renders a pie/doughnut chart visualization using Chart.js with touch interactions.
 * 
 * @component
 */

import React from 'react';
import PropTypes from 'prop-types';
import ChartWrapper from './ChartWrapper';

const COLORS = [
  '#0366d6', // Primary blue
  '#28a745', // Green
  '#6f42c1', // Purple
  '#fd8c73', // Orange
  '#ffd33d', // Yellow
  '#ea4a5a', // Red
  '#1b7cd3', // Light blue
  '#79589f', // Lavender
  '#f97583', // Pink
  '#ffdf5d', // Light yellow
];

/**
 * PieChart Component
 * 
 * @param {Object} props
 * @param {Array} props.data - Chart data array with {name, value} objects
 * @param {string} props.title - Chart title
 * @param {Function} props.onSegmentClick - Handler for segment click events
 * @param {boolean} props.doughnut - Display as doughnut chart (default: false)
 * @param {number} props.cutout - Doughnut cutout percentage (default: 50)
 */
export default function PieChart({ 
  data, 
  title = 'Distribution',
  onSegmentClick,
  doughnut = false,
  cutout = 50
}) {
  if (!data || data.length === 0) {
    return (
      <ChartWrapper
        type="pie"
        data={{ labels: [], datasets: [] }}
        emptyMessage="No data available for visualization"
      />
    );
  }

  // Prepare Chart.js data
  const chartData = {
    labels: data.map(item => item.name || item.label),
    datasets: [
      {
        data: data.map(item => item.value),
        backgroundColor: data.map((_, index) => COLORS[index % COLORS.length]),
        borderColor: '#ffffff',
        borderWidth: 2,
        hoverOffset: 4,
        hoverBorderWidth: 3,
      },
    ],
  };

  // Chart options
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    cutout: doughnut ? `${cutout}%` : 0,
    onClick: (event, elements) => {
      if (elements.length > 0 && onSegmentClick) {
        const index = elements[0].index;
        const clickedData = data[index];
        onSegmentClick({ ...clickedData, fullData: clickedData });
      }
    },
    plugins: {
      legend: {
        display: true,
        position: 'bottom',
        labels: {
          padding: 16,
          font: {
            size: 12,
          },
          usePointStyle: true,
          boxWidth: 12,
          boxHeight: 12,
          generateLabels: (chart) => {
            const datasets = chart.data.datasets;
            const labels = chart.data.labels;
            
            return labels.map((label, i) => {
              const value = datasets[0].data[i];
              const total = datasets[0].data.reduce((sum, val) => sum + val, 0);
              const percentage = ((value / total) * 100).toFixed(1);
              
              return {
                text: `${label} (${percentage}%)`,
                fillStyle: datasets[0].backgroundColor[i],
                hidden: false,
                index: i,
              };
            });
          },
        },
      },
      tooltip: {
        callbacks: {
          label: (context) => {
            const label = context.label || '';
            const value = context.parsed;
            const total = context.dataset.data.reduce((sum, val) => sum + val, 0);
            const percentage = ((value / total) * 100).toFixed(1);
            
            return `${label}: ${value.toLocaleString()} (${percentage}%)`;
          },
        },
      },
    },
    // Touch interactions
    interaction: {
      mode: 'nearest',
    },
  };

  return (
    <ChartWrapper
      type={doughnut ? 'doughnut' : 'pie'}
      data={chartData}
      options={options}
      title={title}
      enableHorizontalScroll={false}
    />
  );
}

PieChart.propTypes = {
  data: PropTypes.arrayOf(PropTypes.shape({
    name: PropTypes.string,
    label: PropTypes.string,
    value: PropTypes.number,
  })).isRequired,
  title: PropTypes.string,
  onSegmentClick: PropTypes.func,
  doughnut: PropTypes.bool,
  cutout: PropTypes.number,
};
