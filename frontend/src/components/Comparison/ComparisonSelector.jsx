import React from "react";
import PropTypes from "prop-types";

/**
 * ComparisonSelector Component
 *
 * Provides UI controls for selecting repositories to compare.
 * Displays selected repository count and clear selection button.
 *
 * @component
 * @param {Object} props
 * @param {string[]} props.selectedRepos - Array of selected repository names
 * @param {Function} props.onClearSelection - Callback to clear all selections
 * @param {number} props.maxSelections - Maximum number of repositories that can be selected
 */
function ComparisonSelector({
  selectedRepos,
  onClearSelection,
  maxSelections = 5,
}) {
  const selectionCount = selectedRepos.length;
  const isAtLimit = selectionCount >= maxSelections;

  return (
    <div className="comparison-selector">
      <div className="flex items-center gap-md">
        <div className="badge badge-primary">
          {selectionCount} / {maxSelections} selected
        </div>

        {selectionCount > 0 && (
          <button
            className="btn btn-secondary btn-sm"
            onClick={onClearSelection}
            aria-label="Clear all selections"
          >
            Clear Selection
          </button>
        )}

        {isAtLimit && (
          <span className="text-warning text-sm">
            Maximum {maxSelections} repositories can be compared
          </span>
        )}
      </div>

      {selectionCount > 0 && (
        <div className="mt-sm">
          <p className="text-muted text-sm">
            Selected: {selectedRepos.join(", ")}
          </p>
        </div>
      )}
    </div>
  );
}

ComparisonSelector.propTypes = {
  selectedRepos: PropTypes.arrayOf(PropTypes.string).isRequired,
  onClearSelection: PropTypes.func.isRequired,
  maxSelections: PropTypes.number,
};

export default ComparisonSelector;
