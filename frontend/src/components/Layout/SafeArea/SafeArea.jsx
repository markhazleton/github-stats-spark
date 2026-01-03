import PropTypes from 'prop-types';
import './SafeArea.css';

/**
 * SafeArea Component
 * Applies safe area insets for notched devices (iOS, Android)
 * 
 * @param {Object} props
 * @param {React.ReactNode} props.children - Content to wrap
 * @param {string[]} props.edges - Which edges to apply insets (['top', 'right', 'bottom', 'left'])
 * @param {string} props.className - Additional CSS classes
 */
export function SafeArea({ 
  children, 
  edges = ['all'],
  className = ''
}) {
  const edgeClasses = edges.includes('all') 
    ? 'safe-all'
    : edges.map(edge => `safe-${edge}`).join(' ');

  const classes = [
    'safe-area',
    edgeClasses,
    className
  ].filter(Boolean).join(' ');

  return (
    <div className={classes}>
      {children}
    </div>
  );
}

SafeArea.propTypes = {
  children: PropTypes.node.isRequired,
  edges: PropTypes.arrayOf(PropTypes.oneOf(['top', 'right', 'bottom', 'left', 'all'])),
  className: PropTypes.string
};

export default SafeArea;
