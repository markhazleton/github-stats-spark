import { useState } from 'react';
import styles from './VisualizationControls.module.css';

const CHART_TYPES = [
  { id: 'bar', label: 'Bar Chart', icon: '📊' },
  { id: 'line', label: 'Line Graph', icon: '📈' },
  { id: 'scatter', label: 'Scatter Plot', icon: '⚫' }
];

const METRICS = [
  { id: 'totalCommits', label: 'Total Commits' },
  { id: 'avgCommitSize', label: 'Average Commit Size' },
  { id: 'largestCommit', label: 'Largest Commit' },
  { id: 'smallestCommit', label: 'Smallest Commit' },
  { id: 'firstCommitDate', label: 'First Commit Date' },
  { id: 'lastCommitDate', label: 'Last Commit Date' }
];

/**
 * VisualizationControls Component
 * Provides controls for selecting chart type and metric to visualize
 * 
 * @param {Object} props
 * @param {string} props.chartType - Currently selected chart type
 * @param {Function} props.onChartTypeChange - Handler for chart type changes
 * @param {string} props.selectedMetric - Currently selected metric
 * @param {Function} props.onMetricChange - Handler for metric selection changes
 */
export default function VisualizationControls({ 
  chartType, 
  onChartTypeChange, 
  selectedMetric, 
  onMetricChange 
}) {
  return (
    <div className={styles.controls}>
      <div className={styles.section}>
        <label className={styles.label}>Chart Type:</label>
        <div className={styles.buttonGroup}>
          {CHART_TYPES.map(type => (
            <button
              key={type.id}
              className={`${styles.button} ${chartType === type.id ? styles.active : ''}`}
              onClick={() => onChartTypeChange(type.id)}
              aria-label={`Select ${type.label}`}
              aria-pressed={chartType === type.id}
            >
              <span className={styles.icon}>{type.icon}</span>
              <span className={styles.buttonLabel}>{type.label}</span>
            </button>
          ))}
        </div>
      </div>

      <div className={styles.section}>
        <label className={styles.label} htmlFor="metric-select">
          Metric:
        </label>
        <select
          id="metric-select"
          className={styles.select}
          value={selectedMetric}
          onChange={(e) => onMetricChange(e.target.value)}
          aria-label="Select metric to visualize"
        >
          {METRICS.map(metric => (
            <option key={metric.id} value={metric.id}>
              {metric.label}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}
