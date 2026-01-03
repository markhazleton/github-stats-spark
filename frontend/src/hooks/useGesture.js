/**
 * useGesture Hook - Touch Gesture Detection
 * 
 * Wraps @use-gesture/react for swipe detection (left, right, up, down)
 * with haptic feedback support via Vibration API.
 * 
 * @module hooks/useGesture
 */

import { useGesture as useGestureLib } from '@use-gesture/react';

/**
 * Haptic feedback patterns for different gesture types
 */
const HAPTIC_PATTERNS = {
  light: 10,      // Quick tap feedback
  medium: 20,     // Swipe feedback
  heavy: 30,      // Delete action feedback
  success: [10, 50, 10], // Pattern for successful action
  error: [10, 100, 10, 100, 10], // Pattern for error
};

/**
 * Trigger haptic feedback if Vibration API is supported
 * 
 * @param {string} type - Haptic pattern type: 'light' | 'medium' | 'heavy' | 'success' | 'error'
 */
export const triggerHapticFeedback = (type = 'light') => {
  if ('vibrate' in navigator) {
    const pattern = HAPTIC_PATTERNS[type];
    navigator.vibrate(pattern);
  }
};

/**
 * Custom hook for gesture detection with haptic feedback
 * 
 * @param {Object} handlers - Gesture event handlers
 * @param {Function} [handlers.onSwipeLeft] - Callback for left swipe
 * @param {Function} [handlers.onSwipeRight] - Callback for right swipe
 * @param {Function} [handlers.onSwipeUp] - Callback for up swipe
 * @param {Function} [handlers.onSwipeDown] - Callback for down swipe
 * @param {Function} [handlers.onTap] - Callback for tap gesture
 * @param {Function} [handlers.onLongPress] - Callback for long press
 * @param {Object} [options] - Configuration options
 * @param {number} [options.swipeThreshold=50] - Minimum distance for swipe (px)
 * @param {number} [options.velocityThreshold=0.5] - Minimum velocity for swipe
 * @param {boolean} [options.enableHaptics=true] - Enable haptic feedback
 * @param {number} [options.longPressDelay=500] - Long press duration (ms)
 * 
 * @returns {Function} - Bind function to attach to element via ref
 * 
 * @example
 * const bind = useGesture({
 *   onSwipeLeft: () => console.log('Swiped left'),
 *   onSwipeRight: () => console.log('Swiped right'),
 *   onTap: () => console.log('Tapped'),
 * });
 * 
 * return <div {...bind()}>Swipeable content</div>;
 */
export const useGesture = (handlers = {}, options = {}) => {
  const {
    onSwipeLeft,
    onSwipeRight,
    onSwipeUp,
    onSwipeDown,
    onTap,
    onLongPress,
  } = handlers;

  const {
    swipeThreshold = 50,
    velocityThreshold = 0.5,
    enableHaptics = true,
    longPressDelay = 500,
  } = options;

  return useGestureLib({
    // Drag gesture for swipe detection
    onDrag: ({ movement: [mx, my], velocity: [vx, vy], down, cancel }) => {
      // Only process when gesture completes (finger lifted)
      if (down) return;

      const absX = Math.abs(mx);
      const absY = Math.abs(my);
      const absVx = Math.abs(vx);
      const absVy = Math.abs(vy);

      // Determine if horizontal or vertical swipe
      if (absX > absY && absX > swipeThreshold && absVx > velocityThreshold) {
        // Horizontal swipe
        if (mx > 0 && onSwipeRight) {
          if (enableHaptics) triggerHapticFeedback('medium');
          onSwipeRight({ distance: mx, velocity: vx });
        } else if (mx < 0 && onSwipeLeft) {
          if (enableHaptics) triggerHapticFeedback('medium');
          onSwipeLeft({ distance: Math.abs(mx), velocity: Math.abs(vx) });
        }
        cancel();
      } else if (absY > absX && absY > swipeThreshold && absVy > velocityThreshold) {
        // Vertical swipe
        if (my > 0 && onSwipeDown) {
          if (enableHaptics) triggerHapticFeedback('medium');
          onSwipeDown({ distance: my, velocity: vy });
        } else if (my < 0 && onSwipeUp) {
          if (enableHaptics) triggerHapticFeedback('medium');
          onSwipeUp({ distance: Math.abs(my), velocity: Math.abs(vy) });
        }
        cancel();
      }
    },

    // Tap gesture
    onPointerDown: ({ event, tap }) => {
      if (tap && onTap) {
        if (enableHaptics) triggerHapticFeedback('light');
        onTap(event);
      }
    },

    // Long press gesture
    onPointerUp: ({ elapsedTime, event }) => {
      if (elapsedTime >= longPressDelay && onLongPress) {
        if (enableHaptics) triggerHapticFeedback('heavy');
        onLongPress(event);
      }
    },
  });
};

/**
 * Hook for swipe-to-delete pattern
 * Returns state and handlers for swipe-to-reveal delete action
 * 
 * @param {Function} onDelete - Callback when delete is confirmed
 * @param {Object} [options] - Configuration options
 * @param {number} [options.revealThreshold=100] - Distance to reveal delete button (px)
 * @param {number} [options.confirmThreshold=200] - Distance to auto-confirm delete (px)
 * @param {boolean} [options.enableHaptics=true] - Enable haptic feedback
 * 
 * @returns {Object} - State and handlers
 * @returns {number} returns.swipeDistance - Current swipe distance
 * @returns {boolean} returns.isRevealed - Whether delete button is revealed
 * @returns {Function} returns.bind - Gesture bind function
 * @returns {Function} returns.reset - Reset swipe state
 * 
 * @example
 * const { swipeDistance, isRevealed, bind, reset } = useSwipeToDelete(handleDelete);
 * 
 * return (
 *   <div {...bind()} style={{ transform: `translateX(${swipeDistance}px)` }}>
 *     <div>Content</div>
 *     {isRevealed && <button onClick={() => { handleDelete(); reset(); }}>Delete</button>}
 *   </div>
 * );
 */
export const useSwipeToDelete = (onDelete, options = {}) => {
  const {
    revealThreshold = 100,
    confirmThreshold = 200,
    enableHaptics = true,
  } = options;

  const [swipeDistance, setSwipeDistance] = React.useState(0);
  const [isRevealed, setIsRevealed] = React.useState(false);

  const bind = useGestureLib({
    onDrag: ({ movement: [mx], down, velocity: [vx] }) => {
      // Only allow left swipe (negative mx)
      const distance = Math.min(0, mx);
      setSwipeDistance(distance);

      // Check if delete button should be revealed
      if (Math.abs(distance) > revealThreshold) {
        if (!isRevealed) {
          setIsRevealed(true);
          if (enableHaptics) triggerHapticFeedback('medium');
        }

        // Auto-confirm delete if swiped far enough with velocity
        if (Math.abs(distance) > confirmThreshold && Math.abs(vx) > 0.5 && !down) {
          if (enableHaptics) triggerHapticFeedback('heavy');
          onDelete();
        }
      } else {
        setIsRevealed(false);
      }

      // Reset on release
      if (!down) {
        setSwipeDistance(0);
        setIsRevealed(false);
      }
    },
  });

  const reset = () => {
    setSwipeDistance(0);
    setIsRevealed(false);
  };

  return {
    swipeDistance,
    isRevealed,
    bind,
    reset,
  };
};

/**
 * Hook for pull-to-refresh pattern
 * 
 * @param {Function} onRefresh - Callback when refresh is triggered
 * @param {Object} [options] - Configuration options
 * @param {number} [options.threshold=80] - Pull distance to trigger refresh (px)
 * @param {boolean} [options.enableHaptics=true] - Enable haptic feedback
 * 
 * @returns {Object} - State and handlers
 * @returns {number} returns.pullDistance - Current pull distance
 * @returns {boolean} returns.isRefreshing - Whether refresh is in progress
 * @returns {Function} returns.bind - Gesture bind function
 * 
 * @example
 * const { pullDistance, isRefreshing, bind } = usePullToRefresh(handleRefresh);
 * 
 * return (
 *   <div {...bind()}>
 *     {pullDistance > 0 && <div>Pull to refresh...</div>}
 *     {isRefreshing && <LoadingSpinner />}
 *     <RepositoryList />
 *   </div>
 * );
 */
export const usePullToRefresh = (onRefresh, options = {}) => {
  const {
    threshold = 80,
    enableHaptics = true,
  } = options;

  const [pullDistance, setPullDistance] = React.useState(0);
  const [isRefreshing, setIsRefreshing] = React.useState(false);

  const bind = useGestureLib({
    onDrag: ({ movement: [, my], down, first }) => {
      // Only allow pull down when scrolled to top
      if (first && window.scrollY > 0) return;

      // Only allow down direction (positive my)
      const distance = Math.max(0, my);
      setPullDistance(distance);

      // Trigger refresh when threshold is reached and released
      if (!down && distance > threshold) {
        setIsRefreshing(true);
        if (enableHaptics) triggerHapticFeedback('success');
        
        Promise.resolve(onRefresh()).finally(() => {
          setIsRefreshing(false);
          setPullDistance(0);
        });
      } else if (!down) {
        setPullDistance(0);
      }
    },
  });

  return {
    pullDistance,
    isRefreshing,
    bind,
  };
};

// Re-export React for useSwipeToDelete and usePullToRefresh
import React from 'react';

export default useGesture;
