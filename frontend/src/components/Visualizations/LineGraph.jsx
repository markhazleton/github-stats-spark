/**
 * LineGraph Component
 * 
 * Renders a line graph visualization using Chart.js with touch-optimized tooltips.
 * 
 * @component
 */

import React from 'react';
import PropTypes from 'prop-types';
import ChartWrapper from './ChartWrapper';

/**
 * Format values based on metric type
 */
function formatValue(value, metricLabel) {
  if (!value && value !== 0) return 'N/A';
  
  if (metricLabel?.includes('Date')) {
    return new Date(value).toLocaleDateString();
  }
  if (metricLabel?.includes('Size')) {
    return `${value.toLocaleString()} changes`;
  }
  if (typeof value === 'number') {
    if (value >= 1000000) {
      return `${(value / 1000000).toFixed(1)}M`;
    } else if (value >= 1000) {
      return `${(value / 1000).toFixed(1)}K`;
    }
    return value.toLocaleString();
  }
  return value;
}

/**
 * LineGraph Component
 * 
 * @param {Object} props
 * @param {Array} props.data - Chart data array with {name, value, date} objects
 * @param {string} props.metricLabel - Label for the metric being displayed
 * @param {Function} props.onPointClick - Handler for point click events
 * @param {string} props.lineColor - Line color (default: primary blue)
 * @param {boolean} props.fill - Fill area under line (default: true)
 */
export default function LineGraph({ 
  data, 
  metricLabel = 'Value',
  onPointClick,
  lineColor = '#0366d6',
  fill = true
}) {
  if (!data || data.length === 0) {
    return (
      <ChartWrapper
        type="line"
        data={{ labels: [], datasets: [] }}
        emptyMessage="No data available for visualization"
      />
    );
  }

  // Sort data by date if available, otherwise by name
  const sortedData = [...data].sort((a, b) => {
    if (a.date && b.date) {
      return new Date(a.date) - new Date(b.date);
    }
    return (a.name || '').localeCompare(b.name || '');
  });

  // Prepare Chart.js data
  const chartData = {
    labels: sortedData.map(item => item.name || item.label || ''),
    datasets: [
      {
        label: metricLabel,
        data: sortedData.map(item => item.value),
        borderColor: lineColor,
        backgroundColor: fill ? `${lineColor}33` : 'transparent', // 20% opacity for fill
        borderWidth: 3,
        fill: fill,
        tension: 0.4, // Curved lines
        pointRadius: 4,
        pointHoverRadius: 6,
        pointBackgroundColor: lineColor,
        pointBorderColor: '#ffffff',
        pointBorderWidth: 2,
        pointHoverBackgroundColor: lineColor,
        pointHoverBorderColor: '#ffffff',
        pointHoverBorderWidth: 2,
      },
    ],
  };

  // Chart options
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    onClick: (event, elements) => {
      if (elements.length > 0 && onPointClick) {
        const index = elements[0].index;
        const clickedData = sortedData[index];
        onPointClick({ ...clickedData, fullData: clickedData });
      }
    },
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        callbacks: {
          label: (context) => {
            const value = context.parsed.y;
            return `${metricLabel}: ${formatValue(value, metricLabel)}`;
          },
          afterLabel: (context) => {
            const item = sortedData[context.dataIndex];
            if (item.date) {
              return `Date: ${new Date(item.date).toLocaleDateString()}`;
            }
            return '';
          },
        },
      },
    },
    scales: {
      x: {
        grid: {
          display: false,
        },
        ticks: {
          maxRotation: 45,
          minRotation: 0,
          font: {
            size: 11,
          },
          autoSkip: true,
          maxTicksLimit: 12,
        },
      },
      y: {
        beginAtZero: true,
        grid: {
          display: true,
          color: 'rgba(0, 0, 0, 0.05)',
        },
        ticks: {
          callback: (value) => formatValue(value, metricLabel),
        },
      },
    },
    interaction: {
      mode: 'nearest',
      axis: 'x',
      intersect: false,
    },
  };

  return (
    <ChartWrapper
      type="line"
      data={chartData}
      options={options}
      title={`${metricLabel} Over Time`}
      enableHorizontalScroll={data.length > 15}
      maxDataPoints={15}
    />
  );
}

LineGraph.propTypes = {
  data: PropTypes.arrayOf(PropTypes.shape({
    name: PropTypes.string,
    label: PropTypes.string,
    value: PropTypes.number,
    date: PropTypes.string,
  })).isRequired,
  metricLabel: PropTypes.string,
  onPointClick: PropTypes.func,
  lineColor: PropTypes.string,
  fill: PropTypes.bool,
};

            tick={{ fill: 'var(--color-text)', fontSize: 12 }}
          />
          <YAxis
            tick={{ fill: 'var(--color-text)', fontSize: 12 }}
            label={{
              value: metricLabel,
              angle: -90,
              position: 'insideLeft',
              style: { fill: 'var(--color-text)', fontSize: 14 }
            }}
          />
          <Tooltip content={<CustomTooltip metricLabel={metricLabel} />} />
          <Line
            type="monotone"
            dataKey="value"
            stroke="var(--chart-color-1)"
            strokeWidth={2}
            dot={{
              fill: 'var(--chart-color-1)',
              r: 4,
              cursor: 'pointer'
            }}
            activeDot={{
              r: 6,
              onClick: onPointClick
            }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
