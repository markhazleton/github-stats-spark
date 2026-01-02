import React from 'react';
import styles from './FilterControls.module.css';

/**
 * FilterControls component for filtering repository data
 * @param {Array} languages - List of available languages
 * @param {string} selectedLanguage - Currently selected language filter
 * @param {Function} onFilterChange - Handler for filter change
 * @param {Function} onClearFilter - Handler to clear filter
 */
function FilterControls({ languages, selectedLanguage, onFilterChange, onClearFilter }) {
  const handleChange = (e) => {
    onFilterChange(e.target.value);
  };

  const handleClear = () => {
    onClearFilter();
  };

  return (
    <div className={styles.filterControls}>
      <div className={styles.filterGroup}>
        <label htmlFor="language-filter" className={styles.label}>
          Filter by Language:
        </label>
        <select
          id="language-filter"
          className={styles.select}
          value={selectedLanguage}
          onChange={handleChange}
        >
          <option value="">All Languages</option>
          {languages.map((lang) => (
            <option key={lang} value={lang}>
              {lang}
            </option>
          ))}
        </select>
      </div>
      
      {selectedLanguage && (
        <button
          type="button"
          className={styles.clearButton}
          onClick={handleClear}
          aria-label="Clear language filter"
        >
          Clear Filter
        </button>
      )}
    </div>
  );
}

export default FilterControls;
