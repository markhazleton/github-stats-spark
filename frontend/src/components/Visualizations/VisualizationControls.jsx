import { useState } from 'react';
import ChartTypeSelector from './ChartTypeSelector';
import { useBreakpoint } from '@/hooks/useMediaQuery';
import styles from './VisualizationControls.module.css';

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
 * Uses ChartTypeSelector for touch-friendly chart type selection
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
  const { isMobile } = useBreakpoint();

  return (
    <div className={styles.controls}>
      {/* Chart Type Selector - Touch-optimized on mobile */}
      <ChartTypeSelector
        selectedType={chartType}
        onTypeChange={onChartTypeChange}
        availableTypes={['bar', 'line', 'pie', 'scatter']}
      />

      {/* Metric Selector */}
      <div className={styles.section}>
        <label className={styles.label} htmlFor="metric-select">
          Metric:
        </label>
        <select
          id="metric-select"
          className={`${styles.select} ${isMobile ? styles.selectMobile : ''}`}
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

