/**
 * useBottomSheet Hook
 *
 * Manages bottom sheet state including open/close status, snap points, and current snap position.
 * Provides a unified interface for controlling bottom sheet behavior across the application.
 *
 * Features:
 * - Open/close state management
 * - Multiple snap points support (e.g., [0.4, 0.9] for partial and full height)
 * - Current snap index tracking
 * - Programmatic snap control
 * - Close callbacks for cleanup
 *
 * @example
 * const { isOpen, open, close, snapTo, currentSnap } = useBottomSheet({
 *   defaultSnap: 0,
 *   onClose: () => console.log('Sheet closed')
 * });
 */

import { useState, useCallback, useRef } from "react";

/**
 * Hook for managing bottom sheet state
 *
 * @param {Object} options - Configuration options
 * @param {number} [options.defaultSnap=0] - Default snap point index (0-based)
 * @param {Function} [options.onClose] - Callback fired when sheet closes
 * @param {Function} [options.onOpen] - Callback fired when sheet opens
 * @param {Function} [options.onSnapChange] - Callback fired when snap point changes
 * @returns {Object} Bottom sheet control interface
 */
export function useBottomSheet({
  defaultSnap = 0,
  onClose,
  onOpen,
  onSnapChange,
} = {}) {
  const [isOpen, setIsOpen] = useState(false);
  const [currentSnap, setCurrentSnap] = useState(defaultSnap);
  const contentRef = useRef(null);

  /**
   * Open the bottom sheet
   * @param {number} [snapIndex] - Optional snap point to open at (defaults to defaultSnap)
   */
  const open = useCallback(
    (snapIndex) => {
      setIsOpen(true);
      if (typeof snapIndex === "number") {
        setCurrentSnap(snapIndex);
      } else {
        setCurrentSnap(defaultSnap);
      }
      onOpen?.();
    },
    [defaultSnap, onOpen],
  );

  /**
   * Close the bottom sheet
   */
  const close = useCallback(() => {
    setIsOpen(false);
    setCurrentSnap(defaultSnap);
    onClose?.();
  }, [defaultSnap, onClose]);

  /**
   * Toggle the bottom sheet open/closed
   */
  const toggle = useCallback(() => {
    if (isOpen) {
      close();
    } else {
      open();
    }
  }, [isOpen, open, close]);

  /**
   * Snap to a specific snap point
   * @param {number} snapIndex - The index of the snap point to snap to
   */
  const snapTo = useCallback(
    (snapIndex) => {
      setCurrentSnap(snapIndex);
      onSnapChange?.(snapIndex);
    },
    [onSnapChange],
  );

  /**
   * Get the content element ref for height calculations
   */
  const setContentRef = useCallback((element) => {
    contentRef.current = element;
  }, []);

  return {
    isOpen,
    open,
    close,
    toggle,
    snapTo,
    currentSnap,
    contentRef,
    setContentRef,
  };
}

/**
 * Hook for managing multiple bottom sheets in the same component
 *
 * This helper intentionally fails fast because creating hooks in dynamic
 * iteration violates React's Rules of Hooks and must not reach runtime silently.
 *
 * @param {Array<string>} sheetIds - Array of sheet identifiers
 * @returns {never}
 *
 * @example
 * // Use individual hook calls instead:
 * const filterSheet = useBottomSheet();
 * const sortSheet = useBottomSheet();
 * const detailSheet = useBottomSheet();
 */
export function useBottomSheets(sheetIds = []) {
  throw new Error(
    `useBottomSheets(${sheetIds.length}) is disabled: call useBottomSheet() individually for each sheet to satisfy the Rules of Hooks.`,
  );
}

export default useBottomSheet;
