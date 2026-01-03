/**
 * FilterSheet Component
 *
 * Bottom sheet containing filter options for repositories:
 * - Language filter (all languages from dataset)
 * - Stars filter (minimum star count slider)
 * - Date range filter (last updated range)
 *
 * Features:
 * - Touch-friendly controls (44x44px minimum)
 * - Clear all filters button
 * - Apply/Cancel actions
 * - Filter count badge
 * - Persistent filter state
 *
 * @example
 * <FilterSheet
 *   isOpen={isOpen}
 *   onClose={handleClose}
 *   filters={filters}
 *   onApplyFilters={handleApply}
 *   availableLanguages={languages}
 * />
 */

import React, { useState } from "react";
import BottomSheet from "../Mobile/BottomSheet/BottomSheet";
import "./FilterSheet.css";

export function FilterSheet({
  isOpen,
  onClose,
  filters = {},
  onApplyFilters,
  availableLanguages = [],
}) {
  // Local state for filter values (committed on Apply)
  const [language, setLanguage] = useState(filters.language || "all");
  const [minStars, setMinStars] = useState(filters.minStars || 0);
  const [dateRange, setDateRange] = useState(filters.dateRange || "all");

  const handleApply = () => {
    onApplyFilters({
      language: language === "all" ? null : language,
      minStars: minStars > 0 ? minStars : null,
      dateRange: dateRange === "all" ? null : dateRange,
    });
    onClose();
  };

  const handleClear = () => {
    setLanguage("all");
    setMinStars(0);
    setDateRange("all");
    onApplyFilters({
      language: null,
      minStars: null,
      dateRange: null,
    });
  };

  const handleCancel = () => {
    // Reset to original filters
    setLanguage(filters.language || "all");
    setMinStars(filters.minStars || 0);
    setDateRange(filters.dateRange || "all");
    onClose();
  };

  // Count active filters
  const activeFilterCount = [
    language !== "all",
    minStars > 0,
    dateRange !== "all",
  ].filter(Boolean).length;

  return (
    <BottomSheet
      isOpen={isOpen}
      onClose={handleCancel}
      title="Filter Repositories"
      snapPoints={[0.6, 0.9]}
      initialSnap={0}
    >
      <div className="filter-sheet">
        {/* Language filter */}
        <div className="filter-section">
          <label htmlFor="language-filter" className="filter-label">
            Language
          </label>
          <select
            id="language-filter"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="filter-select"
          >
            <option value="all">All Languages</option>
            {availableLanguages.map((lang) => (
              <option key={lang} value={lang}>
                {lang}
              </option>
            ))}
          </select>
        </div>

        {/* Stars filter */}
        <div className="filter-section">
          <label htmlFor="stars-filter" className="filter-label">
            Minimum Stars: {minStars}
          </label>
          <input
            id="stars-filter"
            type="range"
            min="0"
            max="1000"
            step="10"
            value={minStars}
            onChange={(e) => setMinStars(Number(e.target.value))}
            className="filter-range"
          />
          <div className="filter-range-labels">
            <span>0</span>
            <span>1000+</span>
          </div>
        </div>

        {/* Date range filter */}
        <div className="filter-section">
          <label htmlFor="date-filter" className="filter-label">
            Last Updated
          </label>
          <select
            id="date-filter"
            value={dateRange}
            onChange={(e) => setDateRange(e.target.value)}
            className="filter-select"
          >
            <option value="all">All Time</option>
            <option value="week">Past Week</option>
            <option value="month">Past Month</option>
            <option value="quarter">Past 3 Months</option>
            <option value="year">Past Year</option>
          </select>
        </div>

        {/* Actions */}
        <div className="filter-actions">
          <button
            onClick={handleClear}
            className="filter-button filter-button-secondary"
            disabled={activeFilterCount === 0}
          >
            Clear All {activeFilterCount > 0 && `(${activeFilterCount})`}
          </button>
          <div className="filter-actions-right">
            <button
              onClick={handleCancel}
              className="filter-button filter-button-text"
            >
              Cancel
            </button>
            <button
              onClick={handleApply}
              className="filter-button filter-button-primary"
            >
              Apply Filters
            </button>
          </div>
        </div>
      </div>
    </BottomSheet>
  );
}

export default FilterSheet;
