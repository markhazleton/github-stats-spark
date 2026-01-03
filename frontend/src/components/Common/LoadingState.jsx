import React from "react";

/**
 * LoadingState Component
 *
 * Displays a loading spinner with optional message.
 * Used throughout the application to indicate data fetching or processing.
 *
 * @component
 * @param {Object} props - Component props
 * @param {string} [props.message='Loading...'] - Custom loading message
 * @param {string} [props.size='medium'] - Spinner size ('small', 'medium', 'large')
 *
 * @example
 * <LoadingState message="Fetching repositories..." size="large" />
 */
export default function LoadingState({
  message = "Loading...",
  size = "medium",
}) {
  const sizes = {
    small: { width: "20px", height: "20px", borderWidth: "2px" },
    medium: { width: "32px", height: "32px", borderWidth: "3px" },
    large: { width: "48px", height: "48px", borderWidth: "4px" },
  };

  const spinnerStyle = sizes[size] || sizes.medium;

  return (
    <div
      className="loading-state flex flex-col items-center justify-center"
      style={{ padding: "var(--spacing-xl)", minHeight: "200px" }}
      role="status"
      aria-live="polite"
    >
      <div className="loading" style={spinnerStyle} aria-label="Loading"></div>
      {message && (
        <p
          className="text-muted mt-md"
          style={{ marginTop: "var(--spacing-md)" }}
        >
          {message}
        </p>
      )}
      <span className="sr-only">{message}</span>
    </div>
  );
}
