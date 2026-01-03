import React, { useState, useRef, useEffect } from "react";
import styles from "./Tooltip.module.css";

/**
 * Tooltip Component
 *
 * Displays contextual information on hover with smooth animations.
 * Automatically positions itself to avoid viewport edges.
 *
 * @component
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Trigger element that shows tooltip on hover
 * @param {string} props.content - Tooltip text content
 * @param {string} [props.position='top'] - Preferred tooltip position ('top', 'bottom', 'left', 'right')
 * @param {number} [props.delay=300] - Show delay in milliseconds
 *
 * @example
 * <Tooltip content="Total commits across all repositories" position="top">
 *   <span>1,234 commits</span>
 * </Tooltip>
 */
export default function Tooltip({
  children,
  content,
  position = "top",
  delay = 300,
}) {
  const [isVisible, setIsVisible] = useState(false);
  const [showTimeout, setShowTimeout] = useState(null);
  const tooltipRef = useRef(null);
  const triggerRef = useRef(null);

  /**
   * Show tooltip after delay
   */
  const handleMouseEnter = () => {
    const timeout = setTimeout(() => {
      setIsVisible(true);
    }, delay);
    setShowTimeout(timeout);
  };

  /**
   * Hide tooltip and clear delay timeout
   */
  const handleMouseLeave = () => {
    if (showTimeout) {
      clearTimeout(showTimeout);
      setShowTimeout(null);
    }
    setIsVisible(false);
  };

  /**
   * Cleanup timeout on unmount
   */
  useEffect(() => {
    return () => {
      if (showTimeout) {
        clearTimeout(showTimeout);
      }
    };
  }, [showTimeout]);

  // Don't render if no content
  if (!content) {
    return <>{children}</>;
  }

  return (
    <div
      className={styles.tooltipWrapper}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      onFocus={handleMouseEnter}
      onBlur={handleMouseLeave}
      ref={triggerRef}
    >
      {children}
      {isVisible && (
        <div
          ref={tooltipRef}
          className={`${styles.tooltip} ${styles[`tooltip--${position}`]}`}
          role="tooltip"
          aria-live="polite"
        >
          <div className={styles.tooltipContent}>{content}</div>
          <div className={styles.tooltipArrow}></div>
        </div>
      )}
    </div>
  );
}
