import { BarChart as RechartsBarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import styles from './Charts.module.css';

const COLORS = [
  'var(--chart-color-1)',
  'var(--chart-color-2)',
  'var(--chart-color-3)',
  'var(--chart-color-4)',
  'var(--chart-color-5)'
];

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
      {data.language && (
        <p className={styles.tooltipLanguage}>Language: {data.language}</p>
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
 * BarChart Component
 * Renders a bar chart visualization using Recharts
 * 
 * @param {Object} props
 * @param {Array} props.data - Chart data array with {name, value} objects
 * @param {string} props.metricLabel - Label for the metric being displayed
 * @param {Function} props.onBarClick - Handler for bar click events
 */
export default function BarChart({ data, metricLabel, onBarClick }) {
  if (!data || data.length === 0) {
    return (
      <div className={styles.emptyState}>
        <p>No data available for visualization</p>
      </div>
    );
  }

  // Calculate dynamic height based on number of items (minimum 400px, 40px per bar)
  const chartHeight = Math.max(400, data.length * 40);

  return (
    <div className={styles.chartContainer}>
      <ResponsiveContainer width="100%" height={chartHeight}>
        <RechartsBarChart
          data={data}
          layout="vertical"
          margin={{ top: 20, right: 30, left: 150, bottom: 20 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border)" />
          <XAxis
            type="number"
            tick={{ fill: 'var(--color-text)', fontSize: 12 }}
          />
          <YAxis
            type="category"
            dataKey="name"
            tick={{ fill: 'var(--color-text)', fontSize: 11 }}
            width={140}
          />
          <Tooltip content={<CustomTooltip metricLabel={metricLabel} />} />
          <Bar
            dataKey="value"
            cursor="pointer"
            onClick={onBarClick}
            radius={[0, 4, 4, 0]}
          >
            {data.map((entry, index) => (
              <Cell
                key={`cell-${index}`}
                fill={COLORS[index % COLORS.length]}
              />
            ))}
          </Bar>
        </RechartsBarChart>
      </ResponsiveContainer>
    </div>
  );
}
