import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';
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
function CustomTooltip({ active, payload }) {
  if (!active || !payload || !payload.length) {
    return null;
  }

  const data = payload[0].payload;
  
  return (
    <div className={styles.tooltip}>
      <p className={styles.tooltipTitle}>{data.name}</p>
      <p className={styles.tooltipValue}>
        <strong>Total Commits:</strong> {data.x.toLocaleString()}
      </p>
      <p className={styles.tooltipValue}>
        <strong>Avg Commit Size:</strong> {data.y.toLocaleString()} changes
      </p>
      {data.language && (
        <p className={styles.tooltipLanguage}>Language: {data.language}</p>
      )}
    </div>
  );
}

/**
 * ScatterPlot Component
 * Renders a scatter plot visualization using Recharts
 * Shows relationship between two metrics (default: commits vs commit size)
 * 
 * @param {Object} props
 * @param {Array} props.data - Chart data array with {name, x, y} objects
 * @param {string} props.xAxisLabel - Label for X axis
 * @param {string} props.yAxisLabel - Label for Y axis
 * @param {Function} props.onPointClick - Handler for point click events
 */
export default function ScatterPlot({ 
  data, 
  xAxisLabel = 'Total Commits', 
  yAxisLabel = 'Average Commit Size',
  onPointClick 
}) {
  if (!data || data.length === 0) {
    return (
      <div className={styles.emptyState}>
        <p>No data available for visualization</p>
      </div>
    );
  }

  return (
    <div className={styles.chartContainer}>
      <ResponsiveContainer width="100%" height={400}>
        <ScatterChart
          margin={{ top: 20, right: 30, left: 20, bottom: 60 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border)" />
          <XAxis
            type="number"
            dataKey="x"
            name={xAxisLabel}
            tick={{ fill: 'var(--color-text)', fontSize: 12 }}
            label={{
              value: xAxisLabel,
              position: 'insideBottom',
              offset: -10,
              style: { fill: 'var(--color-text)', fontSize: 14 }
            }}
          />
          <YAxis
            type="number"
            dataKey="y"
            name={yAxisLabel}
            tick={{ fill: 'var(--color-text)', fontSize: 12 }}
            label={{
              value: yAxisLabel,
              angle: -90,
              position: 'insideLeft',
              style: { fill: 'var(--color-text)', fontSize: 14 }
            }}
          />
          <Tooltip content={<CustomTooltip />} cursor={{ strokeDasharray: '3 3' }} />
          <Scatter
            data={data}
            onClick={onPointClick}
            cursor="pointer"
          >
            {data.map((entry, index) => (
              <Cell
                key={`cell-${index}`}
                fill={COLORS[index % COLORS.length]}
              />
            ))}
          </Scatter>
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
}
