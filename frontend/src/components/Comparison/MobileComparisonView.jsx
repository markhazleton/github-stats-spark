/**
 * MobileComparisonView Component
 * 
 * Mobile-optimized vertical stacked layout for repository comparison
 * with swipe navigation between metrics.
 * 
 * @component
 */

import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { useGesture, triggerHapticFeedback } from '@/hooks/useGesture';
import { formatNumber, formatDate } from '@/services/metricsCalculator';
import './MobileComparisonView.css';

export const MobileComparisonView = ({ repositories, onRemoveRepo }) => {
  const [currentMetricIndex, setCurrentMetricIndex] = useState(0);

  const comparisonMetrics = [
    { key: 'stars', label: 'Stars', type: 'number', icon: '⭐' },
    { key: 'forks', label: 'Forks', type: 'number', icon: '🍴' },
    { key: 'watchers', label: 'Watchers', type: 'number', icon: '👁️' },
    { key: 'open_issues', label: 'Open Issues', type: 'number', icon: '🐛' },
    { key: 'total_commits', label: 'Total Commits', type: 'number', icon: '📝' },
    { key: 'contributors', label: 'Contributors', type: 'number', icon: '👥' },
    { key: 'language', label: 'Language', type: 'string', icon: '💻' },
    { key: 'age_days', label: 'Age (days)', type: 'number', icon: '📅' },
  ];

  const currentMetric = comparisonMetrics[currentMetricIndex];

  // Swipe navigation between metrics
  const bind = useGesture({
    onSwipeLeft: () => {
      if (currentMetricIndex < comparisonMetrics.length - 1) {
        setCurrentMetricIndex(prev => prev + 1);
        triggerHapticFeedback('light');
      }
    },
    onSwipeRight: () => {
      if (currentMetricIndex > 0) {
        setCurrentMetricIndex(prev => prev - 1);
        triggerHapticFeedback('light');
      }
    },
  }, {
    swipeThreshold: 30,
    enableHaptics: true,
  });

  const getNestedValue = (obj, path) => {
    return path.split('.').reduce((acc, part) => acc?.[part], obj);
  };

  const formatValue = (value, type) => {
    if (value == null || value === undefined) return 'N/A';

    switch (type) {
      case 'number':
        return formatNumber(value);
      case 'date':
        return formatDate(value);
      case 'boolean':
        return value ? '✅' : '❌';
      default:
        return String(value);
    }
  };

  // Calculate max value for bar chart
  const values = repositories.map(repo => {
    const val = getNestedValue(repo, currentMetric.key);
    return currentMetric.type === 'number' ? Number(val) || 0 : 0;
  });
  const maxValue = Math.max(...values, 1);

  if (repositories.length === 0) {
    return (
      <div className="mobile-comparison-empty">
        <p>Select repositories to compare</p>
      </div>
    );
  }

  return (
    <div className="mobile-comparison-view" {...bind()}>
      {/* Metric Selector */}
      <div className="mobile-comparison-header">
        <h3 className="mobile-comparison-title">
          <span className="mobile-comparison-icon" aria-hidden="true">
            {currentMetric.icon}
          </span>
          {currentMetric.label}
        </h3>
        <div className="mobile-comparison-pagination">
          <span>{currentMetricIndex + 1} of {comparisonMetrics.length}</span>
          <div className="mobile-comparison-dots">
            {comparisonMetrics.map((_, index) => (
              <button
                key={index}
                className={`mobile-comparison-dot ${index === currentMetricIndex ? 'active' : ''}`}
                onClick={() => setCurrentMetricIndex(index)}
                aria-label={`View ${comparisonMetrics[index].label}`}
              />
            ))}
          </div>
        </div>
      </div>

      {/* Swipe hint */}
      <p className="mobile-comparison-hint">
        ← Swipe to navigate metrics →
      </p>

      {/* Repository Cards */}
      <div className="mobile-comparison-cards">
        {repositories.map((repo, index) => {
          const value = getNestedValue(repo, currentMetric.key);
          const numericValue = currentMetric.type === 'number' ? Number(value) || 0 : 0;
          const barWidth = currentMetric.type === 'number' ? (numericValue / maxValue) * 100 : 0;

          return (
            <div key={repo.name} className="mobile-comparison-card">
              <div className="mobile-comparison-card-header">
                <h4 className="mobile-comparison-repo-name">{repo.name}</h4>
                {onRemoveRepo && (
                  <button
                    className="mobile-comparison-remove-button touch-target"
                    onClick={() => {
                      triggerHapticFeedback('medium');
                      onRemoveRepo(repo.name);
                    }}
                    aria-label={`Remove ${repo.name}`}
                  >
                    ✕
                  </button>
                )}
              </div>

              <div className="mobile-comparison-card-body">
                <div className="mobile-comparison-value">
                  {formatValue(value, currentMetric.type)}
                </div>

                {/* Bar chart for numeric values */}
                {currentMetric.type === 'number' && (
                  <div className="mobile-comparison-bar-container">
                    <div 
                      className="mobile-comparison-bar"
                      style={{ width: `${barWidth}%` }}
                      role="progressbar"
                      aria-valuenow={numericValue}
                      aria-valuemin={0}
                      aria-valuemax={maxValue}
                    />
                  </div>
                )}

                {/* Rank indicator */}
                {currentMetric.type === 'number' && (
                  <div className="mobile-comparison-rank">
                    {numericValue === maxValue && <span className="rank-badge rank-highest">🥇 Highest</span>}
                    {numericValue === Math.min(...values.filter(v => v > 0)) && numericValue !== maxValue && (
                      <span className="rank-badge rank-lowest">Lowest</span>
                    )}
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Navigation Buttons */}
      <div className="mobile-comparison-nav">
        <button
          className="mobile-comparison-nav-button touch-target"
          onClick={() => setCurrentMetricIndex(prev => Math.max(0, prev - 1))}
          disabled={currentMetricIndex === 0}
          aria-label="Previous metric"
        >
          ← Previous
        </button>
        <button
          className="mobile-comparison-nav-button touch-target"
          onClick={() => setCurrentMetricIndex(prev => Math.min(comparisonMetrics.length - 1, prev + 1))}
          disabled={currentMetricIndex === comparisonMetrics.length - 1}
          aria-label="Next metric"
        >
          Next →
        </button>
      </div>
    </div>
  );
};

MobileComparisonView.propTypes = {
  repositories: PropTypes.arrayOf(PropTypes.shape({
    name: PropTypes.string.isRequired,
    stars: PropTypes.number,
    forks: PropTypes.number,
    watchers: PropTypes.number,
    open_issues: PropTypes.number,
    total_commits: PropTypes.number,
    contributors: PropTypes.number,
    language: PropTypes.string,
    age_days: PropTypes.number,
  })).isRequired,
  onRemoveRepo: PropTypes.func,
};

export default MobileComparisonView;
