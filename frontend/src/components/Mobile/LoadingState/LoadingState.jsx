import PropTypes from 'prop-types';
import './LoadingState.css';

/**
 * LoadingState Component
 * Skeleton screens for progressive loading
 * 
 * @param {Object} props
 * @param {string} props.type - Type of loading indicator ('card'|'list'|'chart'|'text')
 * @param {string} props.variant - Visual style ('skeleton'|'spinner')
 * @param {number} props.count - Number of skeleton items
 * @param {string} props.className - Additional CSS classes
 */
export function LoadingState({ 
  type = 'card',
  variant = 'skeleton',
  count = 1,
  className = ''
}) {
  const classes = [
    'loading-state',
    `loading-${type}`,
    `loading-${variant}`,
    className
  ].filter(Boolean).join(' ');

  if (variant === 'spinner') {
    return (
      <div className="loading-spinner-container">
        <div className="loading-spinner" aria-label="Loading" />
      </div>
    );
  }

  const items = Array.from({ length: count }, (_, i) => (
    <div key={i} className={classes}>
      {type === 'card' && (
        <>
          <div className="skeleton-title" />
          <div className="skeleton-badge" />
          <div className="skeleton-meta" />
        </>
      )}
      {type === 'list' && (
        <>
          <div className="skeleton-line skeleton-line-full" />
          <div className="skeleton-line skeleton-line-medium" />
        </>
      )}
      {type === 'chart' && (
        <div className="skeleton-chart" />
      )}
      {type === 'text' && (
        <>
          <div className="skeleton-line skeleton-line-full" />
          <div className="skeleton-line skeleton-line-long" />
          <div className="skeleton-line skeleton-line-medium" />
        </>
      )}
    </div>
  ));

  return <div className="loading-state-container">{items}</div>;
}

LoadingState.propTypes = {
  type: PropTypes.oneOf(['card', 'list', 'chart', 'text']),
  variant: PropTypes.oneOf(['skeleton', 'spinner']),
  count: PropTypes.number,
  className: PropTypes.string
};

export default LoadingState;
