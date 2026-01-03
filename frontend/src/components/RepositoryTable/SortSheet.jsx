/**
 * SortSheet Component
 *
 * Bottom sheet for sorting repository list with:
 * - Multiple sort fields (name, stars, commits, last updated, language)
 * - Ascending/descending direction toggle
 * - Visual indicators for current sort
 * - Touch-friendly radio buttons
 *
 * Features:
 * - Touch-optimized controls (44x44px minimum)
 * - Clear visual feedback for selected option
 * - Apply/Cancel actions
 * - Persistent sort state
 *
 * @example
 * <SortSheet
 *   isOpen={isOpen}
 *   onClose={handleClose}
 *   sortField={sortField}
 *   sortDirection={sortDirection}
 *   onApplySort={handleApply}
 * />
 */

import React, { useState } from "react";
import BottomSheet from "../Mobile/BottomSheet/BottomSheet";
import "./SortSheet.css";

const SORT_OPTIONS = [
  { value: "name", label: "Name", icon: "🔤" },
  { value: "stars", label: "Stars", icon: "⭐" },
  { value: "commits", label: "Commits", icon: "📝" },
  { value: "updated", label: "Last Updated", icon: "📅" },
  { value: "language", label: "Language", icon: "💻" },
];

export function SortSheet({
  isOpen,
  onClose,
  sortField = "stars",
  sortDirection = "desc",
  onApplySort,
}) {
  // Local state for sort values (committed on Apply)
  const [field, setField] = useState(sortField);
  const [direction, setDirection] = useState(sortDirection);

  const handleApply = () => {
    onApplySort({
      field,
      direction,
    });
    onClose();
  };

  const handleCancel = () => {
    // Reset to original sort
    setField(sortField);
    setDirection(sortDirection);
    onClose();
  };

  const toggleDirection = () => {
    setDirection(direction === "asc" ? "desc" : "asc");
  };

  return (
    <BottomSheet
      isOpen={isOpen}
      onClose={handleCancel}
      title="Sort Repositories"
      snapPoints={[0.5, 0.9]}
      initialSnap={0}
    >
      <div className="sort-sheet">
        {/* Sort field options */}
        <div className="sort-section">
          <div className="sort-label">Sort by</div>
          <div className="sort-options">
            {SORT_OPTIONS.map((option) => (
              <button
                key={option.value}
                onClick={() => setField(option.value)}
                className={`sort-option ${field === option.value ? "sort-option-active" : ""}`}
                role="radio"
                aria-checked={field === option.value}
              >
                <span className="sort-option-icon" aria-hidden="true">
                  {option.icon}
                </span>
                <span className="sort-option-label">{option.label}</span>
                {field === option.value && (
                  <span className="sort-option-checkmark" aria-hidden="true">
                    ✓
                  </span>
                )}
              </button>
            ))}
          </div>
        </div>

        {/* Sort direction toggle */}
        <div className="sort-section">
          <div className="sort-label">Order</div>
          <button
            onClick={toggleDirection}
            className="sort-direction-toggle"
            aria-label={`Sort direction: ${direction === "asc" ? "Ascending" : "Descending"}`}
          >
            <span className="sort-direction-icon" aria-hidden="true">
              {direction === "asc" ? "↑" : "↓"}
            </span>
            <span className="sort-direction-label">
              {direction === "asc" ? "Ascending" : "Descending"}
            </span>
            <span className="sort-direction-subtext">
              {direction === "asc"
                ? "(A → Z, Low → High)"
                : "(Z → A, High → Low)"}
            </span>
          </button>
        </div>

        {/* Actions */}
        <div className="sort-actions">
          <button
            onClick={handleCancel}
            className="sort-button sort-button-text"
          >
            Cancel
          </button>
          <button
            onClick={handleApply}
            className="sort-button sort-button-primary"
          >
            Apply Sort
          </button>
        </div>
      </div>
    </BottomSheet>
  );
}

export default SortSheet;
