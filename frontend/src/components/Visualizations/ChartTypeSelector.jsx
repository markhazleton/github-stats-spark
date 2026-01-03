/**
 * ChartTypeSelector Component
 * 
 * Large touch-friendly buttons for switching between chart types.
 * Optimized for mobile with 44x44px minimum touch targets.
 * 
 * @component
 */

import React from 'react';
import PropTypes from 'prop-types';
import { triggerHapticFeedback } from '@/hooks/useGesture';
import './ChartTypeSelector.css';

const CHART_TYPES = [
  { id: 'bar', label: 'Bar', icon: '📊', description: 'Compare values' },
  { id: 'line', label: 'Line', icon: '📈', description: 'Trends over time' },
  { id: 'pie', label: 'Pie', icon: '🥧', description: 'Distribution' },
  { id: 'scatter', label: 'Scatter', icon: '⚫', description: 'Relationships' },
];

export const ChartTypeSelector = ({ 
  selectedType = 'bar',
  onTypeChange,
  availableTypes = ['bar', 'line', 'pie', 'scatter'],
  className = ''
}) => {
  const handleTypeChange = (type) => {
    if (type !== selectedType) {
      triggerHapticFeedback('light');
      onTypeChange(type);
    }
  };

  const filteredTypes = CHART_TYPES.filter(type => availableTypes.includes(type.id));

  return (
    <div className={`chart-type-selector ${className}`}>
      <h4 className="chart-type-selector-title">Chart Type</h4>
      <div className="chart-type-buttons">
        {filteredTypes.map(type => (
          <button
            key={type.id}
            className={`chart-type-button touch-target ${selectedType === type.id ? 'active' : ''}`}
            onClick={() => handleTypeChange(type.id)}
            aria-pressed={selectedType === type.id}
            aria-label={`${type.label} chart - ${type.description}`}
          >
            <span className="chart-type-icon" aria-hidden="true">{type.icon}</span>
            <span className="chart-type-label">{type.label}</span>
            <span className="chart-type-description">{type.description}</span>
          </button>
        ))}
      </div>
    </div>
  );
};

ChartTypeSelector.propTypes = {
  selectedType: PropTypes.oneOf(['bar', 'line', 'pie', 'scatter']),
  onTypeChange: PropTypes.func.isRequired,
  availableTypes: PropTypes.arrayOf(PropTypes.oneOf(['bar', 'line', 'pie', 'scatter'])),
  className: PropTypes.string,
};

export default ChartTypeSelector;
