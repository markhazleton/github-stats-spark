/**
 * BottomSheet Component
 *
 * A mobile-native bottom sheet component using react-modal-sheet for iOS/Android-like behavior.
 * Supports multiple snap points, swipe-to-dismiss, backdrop interaction, and accessibility features.
 *
 * Features:
 * - Configurable snap points (default: [0.4, 0.9] for partial/full height)
 * - Swipe-down gesture to dismiss
 * - Tap backdrop to close
 * - Smooth spring animations
 * - Focus trap for keyboard accessibility
 * - Prevents browser pull-to-refresh when active
 * - Header with visual drag indicator
 *
 * @example
 * <BottomSheet
 *   isOpen={isOpen}
 *   onClose={handleClose}
 *   snapPoints={[0.4, 0.9]}
 *   title="Filter Options"
 * >
 *   <FilterForm />
 * </BottomSheet>
 */

import React, { useEffect, useRef } from "react";
import { Sheet } from "react-modal-sheet";
import "./BottomSheet.css";

export function BottomSheet({
  isOpen,
  onClose,
  children,
  title,
  snapPoints = [0.4, 0.9],
  initialSnap = 0,
  disableDrag = false,
  closeOnBackdrop = true,
  showHeader = true,
  className = "",
}) {
  const sheetRef = useRef(null);
  const contentRef = useRef(null);

  /**
   * Prevent browser pull-to-refresh when bottom sheet is active
   * This prevents conflicts between swipe-down-to-dismiss and browser's native pull-to-refresh
   */
  useEffect(() => {
    if (!isOpen) return;

    const preventRefresh = (e) => {
      // Only prevent if the sheet is at the top of its scroll (scrollTop === 0)
      // This allows scrolling within the sheet content
      if (contentRef.current?.scrollTop === 0) {
        e.preventDefault();
      }
    };

    const contentElement = contentRef.current;
    if (contentElement?.addEventListener) {
      contentElement.addEventListener("touchmove", preventRefresh, {
        passive: false,
      });
    }

    return () => {
      if (contentElement?.removeEventListener) {
        contentElement.removeEventListener("touchmove", preventRefresh);
      }
    };
  }, [isOpen]);

  /**
   * Focus trap: Focus the sheet when it opens for keyboard accessibility
   */
  useEffect(() => {
    if (isOpen) {
      const focusRoot = contentRef.current ?? sheetRef.current;
      const focusableElements = focusRoot?.querySelectorAll?.(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])',
      );

      if (focusableElements?.length > 0) {
        // Focus the first focusable element
        focusableElements[0]?.focus();
      }
    }
  }, [isOpen]);

  /**
   * Keyboard handler for ESC key to close
   */
  useEffect(() => {
    if (!isOpen) return;

    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        onClose();
      }
    };

    document.addEventListener("keydown", handleKeyDown);
    return () => document.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  return (
    <Sheet
      ref={sheetRef}
      isOpen={isOpen}
      onClose={onClose}
      snapPoints={snapPoints}
      initialSnap={initialSnap}
      disableDrag={disableDrag}
      className={`bottom-sheet ${className}`}
    >
      <Sheet.Container>
        <Sheet.Header>
          {showHeader && (
            <div className="bottom-sheet-header">
              <div className="bottom-sheet-drag-indicator" aria-hidden="true" />
              {title && <h2 className="bottom-sheet-title">{title}</h2>}
            </div>
          )}
        </Sheet.Header>

        <Sheet.Content ref={contentRef}>
          <div className="bottom-sheet-body">{children}</div>
        </Sheet.Content>
      </Sheet.Container>

      <Sheet.Backdrop
        onTap={closeOnBackdrop ? onClose : undefined}
        className="bottom-sheet-backdrop"
      />
    </Sheet>
  );
}

export default BottomSheet;
