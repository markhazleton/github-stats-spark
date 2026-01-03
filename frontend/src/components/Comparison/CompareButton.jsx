/**
 * CompareButton Component
 * 
 * Floating action button that appears when 2-5 repositories are selected.
 * Shows selection count badge and triggers comparison view.
 * 
 * @component
 * @example
 * <CompareButton
 *   count={3}
 *   onClick={() => navigate('/comparison')}
 *   disabled={count < 2}
 * />
 */

import React from 'react';
import PropTypes from 'prop-types';
import { triggerHapticFeedback } from '@/hooks/useGesture';
import './CompareButton.css';

export const CompareButton = ({ 
  count = 0, 
  onClick,
  disabled = false,
  maxSelections = 5
}) => {
  const handleClick = () => {
    triggerHapticFeedback('medium');
    if (onClick && !disabled) {
      onClick();
    }
  };

  // Don't render if no selections
  if (count === 0) return null;

  const isDisabled = disabled || count < 2;
  const isMaxReached = count >= maxSelections;

  return (
    <button
      className={`compare-button touch-target ${isDisabled ? 'compare-button-disabled' : ''} ${isMaxReached ? 'compare-button-max' : ''}`}
      onClick={handleClick}
      disabled={isDisabled}
      aria-label={`Compare ${count} selected ${count === 1 ? 'repository' : 'repositories'}`}
      aria-disabled={isDisabled}
    >
      <div className="compare-button-content">
        <span className="compare-button-icon" aria-hidden="true">📊</span>
        <span className="compare-button-text">
          {isDisabled ? 'Select 2+' : 'Compare'}
        </span>
        <span className="compare-button-badge" aria-label={`${count} selected`}>
          {count}
        </span>
      </div>
      
      {isMaxReached && (
        <span className="compare-button-hint">Max {maxSelections} repos</span>
      )}
    </button>
  );
};

CompareButton.propTypes = {
  count: PropTypes.number,
  onClick: PropTypes.func.isRequired,
  disabled: PropTypes.bool,
  maxSelections: PropTypes.number,
};

export default CompareButton;
