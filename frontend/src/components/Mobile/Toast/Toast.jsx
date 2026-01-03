/**
 * Toast Component
 * Transient feedback notifications positioned at bottom above TabBar
 * Supports success, error, warning, and info variants
 */

import React, { useEffect, useState, useCallback } from "react";
import "./Toast.css";

export function Toast({
  message,
  variant = "info", // 'success' | 'error' | 'warning' | 'info'
  duration = 3000,
  onClose,
  icon = null,
}) {
  const [isVisible, setIsVisible] = useState(true);
  const [isLeaving, setIsLeaving] = useState(false);

  const handleClose = useCallback(() => {
    setIsLeaving(true);
    setTimeout(() => {
      setIsVisible(false);
      if (onClose) onClose();
    }, 300); // Match CSS transition duration
  }, [onClose]);

  useEffect(() => {
    if (duration <= 0) return;

    const timer = setTimeout(() => {
      handleClose();
    }, duration);

    return () => clearTimeout(timer);
  }, [duration, handleClose]);

  if (!isVisible) return null;

  const getIcon = () => {
    if (icon) return icon;

    switch (variant) {
      case "success":
        return (
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path
              d="M10 0C4.48 0 0 4.48 0 10s4.48 10 10 10 10-4.48 10-10S15.52 0 10 0zm-2 15l-5-5 1.41-1.41L8 12.17l7.59-7.59L17 6l-9 9z"
              fill="currentColor"
            />
          </svg>
        );
      case "error":
        return (
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path
              d="M10 0C4.48 0 0 4.48 0 10s4.48 10 10 10 10-4.48 10-10S15.52 0 10 0zm1 15H9v-2h2v2zm0-4H9V5h2v6z"
              fill="currentColor"
            />
          </svg>
        );
      case "warning":
        return (
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path
              d="M1 17h18L10 2 1 17zm10-2H9v-2h2v2zm0-4H9V9h2v2z"
              fill="currentColor"
            />
          </svg>
        );
      default:
        return (
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path
              d="M10 0C4.48 0 0 4.48 0 10s4.48 10 10 10 10-4.48 10-10S15.52 0 10 0zm1 15H9v-2h2v2zm0-4H9V5h2v6z"
              fill="currentColor"
            />
          </svg>
        );
    }
  };

  return (
    <div
      className={`toast toast--${variant} ${isLeaving ? "toast--leaving" : ""}`}
      role="alert"
      aria-live="polite"
    >
      <div className="toast__icon" aria-hidden="true">
        {getIcon()}
      </div>

      <div className="toast__message">{message}</div>

      <button
        className="toast__close"
        onClick={handleClose}
        aria-label="Close notification"
        type="button"
      >
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path
            d="M12.5 3.5L3.5 12.5M3.5 3.5l9 9"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
          />
        </svg>
      </button>
    </div>
  );
}

/**
 * ToastContainer - Manages multiple toast notifications
 */
export function ToastContainer({ toasts = [], onRemove }) {
  if (toasts.length === 0) return null;

  return (
    <div className="toast-container" aria-live="polite" aria-atomic="false">
      {toasts.map((toast) => (
        <Toast
          key={toast.id}
          message={toast.message}
          variant={toast.variant}
          duration={toast.duration}
          icon={toast.icon}
          onClose={() => onRemove(toast.id)}
        />
      ))}
    </div>
  );
}

export default Toast;
