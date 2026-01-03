import { useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
import './TouchTarget.css';

/**
 * TouchTarget Component
 * Ensures 44x44px minimum size with touch feedback
 * 
 * @param {Object} props
 * @param {React.ReactNode} props.children - Content to wrap
 * @param {Function} props.onClick - Click handler
 * @param {Object} props.config - Touch target configuration
 * @param {string} props.ariaLabel - Accessibility label
 * @param {boolean} props.ripple - Enable ripple effect
 * @param {string} props.className - Additional CSS classes
 */
export function TouchTarget({ 
  children, 
  onClick,
  config = {},
  ariaLabel,
  ripple = false,
  disabled = false,
  className = ''
}) {
  const ref = useRef(null);
  const { minWidth = 44, minHeight = 44 } = config;

  const style = {
    '--touch-min-width': `${minWidth}px`,
    '--touch-min-height': `${minHeight}px`
  };

  const classes = [
    'touch-target',
    ripple && 'ripple',
    disabled && 'disabled',
    className
  ].filter(Boolean).join(' ');

  const handleClick = (e) => {
    if (disabled) return;
    onClick?.(e);
  };

  return (
    <button
      ref={ref}
      className={classes}
      style={style}
      onClick={handleClick}
      aria-label={ariaLabel}
      disabled={disabled}
      type="button"
    >
      {children}
    </button>
  );
}

TouchTarget.propTypes = {
  children: PropTypes.node.isRequired,
  onClick: PropTypes.func,
  config: PropTypes.shape({
    minWidth: PropTypes.number,
    minHeight: PropTypes.number
  }),
  ariaLabel: PropTypes.string.isRequired,
  ripple: PropTypes.bool,
  disabled: PropTypes.bool,
  className: PropTypes.string
};

export default TouchTarget;
