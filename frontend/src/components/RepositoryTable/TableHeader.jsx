import React from "react";
import styles from "./RepositoryTable.module.css";

/**
 * TableHeader Component
 *
 * Renders table column headers with sorting indicators and click handlers.
 * Supports ascending/descending sort with visual arrow indicators.
 *
 * @component
 * @param {Object} props - Component props
 * @param {Function} props.onSort - Callback when column is clicked for sorting
 * @param {string} props.sortField - Currently sorted field name
 * @param {string} props.sortDirection - Current sort direction ('asc' or 'desc')
 *
 * @example
 * <TableHeader
 *   onSort={(field) => handleSort(field)}
 *   sortField="stars"
 *   sortDirection="desc"
 * />
 */
export default function TableHeader({ onSort, sortField, sortDirection }) {
  /**
   * Column definitions with display names and sortable fields
   */
  const columns = [
    { key: "name", label: "Repository", sortable: true },
    { key: "language", label: "Language", sortable: true },
    { key: "created_at", label: "Created", sortable: true },
    { key: "first_commit_date", label: "First Commit", sortable: true },
    { key: "last_commit_date", label: "Last Commit", sortable: true },
    { key: "commit_count", label: "Total Commits", sortable: true },
    { key: "avg_commit_size", label: "Avg Size", sortable: true },
    { key: "largest_commit", label: "Largest", sortable: true },
    { key: "smallest_commit", label: "Smallest", sortable: true },
    { key: "stars", label: "Stars", sortable: true },
  ];

  /**
   * Render sort indicator arrow
   */
  const renderSortIndicator = (columnKey) => {
    if (sortField !== columnKey) {
      return <span className={styles.sortIndicator}>⇅</span>;
    }

    return (
      <span className={styles.sortIndicatorActive}>
        {sortDirection === "asc" ? "↑" : "↓"}
      </span>
    );
  };

  /**
   * Handle column click
   */
  const handleColumnClick = (columnKey, sortable) => {
    if (sortable && onSort) {
      onSort(columnKey);
    }
  };

  return (
    <thead className={styles.tableHead}>
      <tr>
        {columns.map((column) => (
          <th
            key={column.key}
            className={`${styles.tableHeader} ${
              column.sortable ? styles.tableHeaderSortable : ""
            } ${sortField === column.key ? styles.tableHeaderActive : ""}`}
            onClick={() => handleColumnClick(column.key, column.sortable)}
            aria-sort={
              sortField === column.key
                ? sortDirection === "asc"
                  ? "ascending"
                  : "descending"
                : "none"
            }
            role="columnheader"
            tabIndex={column.sortable ? 0 : -1}
            onKeyDown={(e) => {
              if (column.sortable && (e.key === "Enter" || e.key === " ")) {
                e.preventDefault();
                handleColumnClick(column.key, column.sortable);
              }
            }}
          >
            <div className={styles.tableHeaderContent}>
              <span>{column.label}</span>
              {column.sortable && renderSortIndicator(column.key)}
            </div>
          </th>
        ))}
      </tr>
    </thead>
  );
}
