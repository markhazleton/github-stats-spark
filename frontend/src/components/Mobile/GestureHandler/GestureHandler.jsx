/**
 * GestureHandler Component
 *
 * Wraps child elements with swipe gesture detection and visual feedback.
 * Provides haptic feedback and animation for touch interactions.
 *
 * @component
 * @example
 * <GestureHandler
 *   onSwipeLeft={() => console.log('Swiped left')}
 *   onSwipeRight={() => console.log('Swiped right')}
 * >
 *   <div>Swipeable content</div>
 * </GestureHandler>
 */

import React, { useState } from "react";
import { useGesture } from "@/hooks/useGesture";
import "./GestureHandler.css";

export const GestureHandler = ({
  children,
  onSwipeLeft,
  onSwipeRight,
  onSwipeUp,
  onSwipeDown,
  onTap,
  onLongPress,
  swipeThreshold = 50,
  velocityThreshold = 0.5,
  enableHaptics = true,
  showFeedback = true,
  className = "",
  ...props
}) => {
  const [gestureState, setGestureState] = useState({
    isDragging: false,
    direction: null,
    distance: 0,
  });

  const bind = useGesture(
    {
      onSwipeLeft: (data) => {
        if (showFeedback) {
          setGestureState({
            isDragging: false,
            direction: "left",
            distance: data.distance,
          });
          setTimeout(
            () =>
              setGestureState({
                isDragging: false,
                direction: null,
                distance: 0,
              }),
            300,
          );
        }
        onSwipeLeft?.(data);
      },
      onSwipeRight: (data) => {
        if (showFeedback) {
          setGestureState({
            isDragging: false,
            direction: "right",
            distance: data.distance,
          });
          setTimeout(
            () =>
              setGestureState({
                isDragging: false,
                direction: null,
                distance: 0,
              }),
            300,
          );
        }
        onSwipeRight?.(data);
      },
      onSwipeUp: (data) => {
        if (showFeedback) {
          setGestureState({
            isDragging: false,
            direction: "up",
            distance: data.distance,
          });
          setTimeout(
            () =>
              setGestureState({
                isDragging: false,
                direction: null,
                distance: 0,
              }),
            300,
          );
        }
        onSwipeUp?.(data);
      },
      onSwipeDown: (data) => {
        if (showFeedback) {
          setGestureState({
            isDragging: false,
            direction: "down",
            distance: data.distance,
          });
          setTimeout(
            () =>
              setGestureState({
                isDragging: false,
                direction: null,
                distance: 0,
              }),
            300,
          );
        }
        onSwipeDown?.(data);
      },
      onTap: (event) => {
        onTap?.(event);
      },
      onLongPress: (event) => {
        onLongPress?.(event);
      },
    },
    {
      swipeThreshold,
      velocityThreshold,
      enableHaptics,
    },
  );

  return (
    <div
      {...bind()}
      className={`gesture-handler ${className} ${gestureState.direction ? `gesture-feedback-${gestureState.direction}` : ""}`}
      data-gesture-active={gestureState.direction !== null}
      {...props}
    >
      {children}

      {/* Visual feedback indicator */}
      {showFeedback && gestureState.direction && (
        <div
          className={`gesture-indicator gesture-indicator-${gestureState.direction}`}
        >
          {gestureState.direction === "left" && <span>←</span>}
          {gestureState.direction === "right" && <span>→</span>}
          {gestureState.direction === "up" && <span>↑</span>}
          {gestureState.direction === "down" && <span>↓</span>}
        </div>
      )}
    </div>
  );
};

export default GestureHandler;
