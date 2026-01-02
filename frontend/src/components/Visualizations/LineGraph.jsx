import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';
import styles from './Charts.module.css';

/**
 * CustomTooltip Component
 * Displays formatted values on hover
 */
function CustomTooltip({ active, payload, metricLabel }) {
  if (!active || !payload || !payload.length) {
    return null;
  }

  const data = payload[0].payload;
  
  return (
    <div className={styles.tooltip}>
      <p className={styles.tooltipTitle}>{data.name}</p>
      <p className={styles.tooltipValue}>
        <strong>{metricLabel}:</strong> {formatValue(data.value, metricLabel)}
      </p>
      {data.date && (
        <p className={styles.tooltipDate}>
          Date: {new Date(data.date).toLocaleDateString()}
        </p>
      )}
    </div>
  );
}

/**
 * Format values based on metric type
 */
function formatValue(value, metricLabel) {
  if (metricLabel.includes('Date')) {
    return new Date(value).toLocaleDateString();
  }
  if (metricLabel.includes('Size')) {
    return `${value.toLocaleString()} changes`;
  }
  return value.toLocaleString();
}

/**
 * LineGraph Component
 * Renders a line graph visualization using Recharts
 * 
 * @param {Object} props
 * @param {Array} props.data - Chart data array with {name, value, date} objects
 * @param {string} props.metricLabel - Label for the metric being displayed
 * @param {Function} props.onPointClick - Handler for point click events
 */
export default function LineGraph({ data, metricLabel, onPointClick }) {
  if (!data || data.length === 0) {
    return (
      <div className={styles.emptyState}>
        <p>No data available for visualization</p>
      </div>
    );
  }

  // Sort data by date if available, otherwise by name
  const sortedData = [...data].sort((a, b) => {
    if (a.date && b.date) {
      return new Date(a.date) - new Date(b.date);
    }
    return a.name.localeCompare(b.name);
  });

  return (
    <div className={styles.chartContainer}>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart
          data={sortedData}
          margin={{ top: 20, right: 30, left: 20, bottom: 60 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border)" />
          <XAxis
            dataKey="name"
            angle={-45}
            textAnchor="end"
            height={100}
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
