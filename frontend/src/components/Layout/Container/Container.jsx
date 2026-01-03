import { Children } from 'react';
import PropTypes from 'prop-types';
import './Container.css';

/**
 * Container Component
 * Mobile-first responsive container with proper padding and max-width
 * 
 * @param {Object} props
 * @param {React.ReactNode} props.children - Content to wrap
 * @param {string} props.maxWidth - Maximum width breakpoint ('sm'|'md'|'lg'|'xl'|'full')
 * @param {boolean} props.centered - Center content horizontally
 * @param {boolean} props.padding - Apply responsive padding
 * @param {string} props.className - Additional CSS classes
 */
export function Container({ 
  children, 
  maxWidth = 'lg', 
  centered = false, 
  padding = true,
  className = ''
}) {
  const classes = [
    'container',
    `container-${maxWidth}`,
    centered && 'container-centered',
    padding && 'container-padding',
    className
  ].filter(Boolean).join(' ');

  return (
    <div className={classes}>
      {children}
    </div>
  );
}

Container.propTypes = {
  children: PropTypes.node.isRequired,
  maxWidth: PropTypes.oneOf(['sm', 'md', 'lg', 'xl', 'full']),
  centered: PropTypes.bool,
  padding: PropTypes.bool,
  className: PropTypes.string
};

export default Container;
