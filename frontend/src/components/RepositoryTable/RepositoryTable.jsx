import React, { useState } from 'react'
import TableHeader from './TableHeader'
import TableRow from './TableRow'
import styles from './RepositoryTable.module.css'

/**
 * RepositoryTable Component
 *
 * Main table component that displays repository data with comprehensive metrics.
 * Supports sorting, filtering, and row selection for comparison.
 *
 * @component
 * @param {Object} props - Component props
 * @param {Array} props.repositories - Array of repository objects to display
 * @param {Function} [props.onSort] - Callback when column header is clicked for sorting
 * @param {Function} [props.onFilter] - Callback when filter is applied
 * @param {Function} [props.onSelectRepo] - Callback when repository is selected for comparison
 * @param {Function} [props.onRowClick] - Callback when row is clicked for drill-down
 * @param {Array} [props.selectedRepos] - Array of selected repository names
 * @param {string} [props.sortField] - Current sort field name
 * @param {string} [props.sortDirection] - Current sort direction ('asc' or 'desc')
 *
 * @example
 * <RepositoryTable
 *   repositories={data.repositories}
 *   onSort={(field, direction) => console.log('Sort by', field, direction)}
 *   onRowClick={(repo) => showDetails(repo)}
 * />
 */
export default function RepositoryTable({
  repositories = [],
  onSort,
  onFilter,
  onSelectRepo,
  onRowClick,
  selectedRepos = [],
  sortField = null,
  sortDirection = 'desc',
}) {
  const [localSortField, setLocalSortField] = useState(sortField || 'stars')
  const [localSortDirection, setLocalSortDirection] = useState(sortDirection)

  /**
   * Handle column header click for sorting
   */
  const handleSort = (field) => {
    let newDirection = 'desc'

    // If clicking the same field, toggle direction
    if (field === localSortField) {
      newDirection = localSortDirection === 'desc' ? 'asc' : 'desc'
    }

    setLocalSortField(field)
    setLocalSortDirection(newDirection)

    // Call parent callback if provided
    if (onSort) {
      onSort(field, newDirection)
    }
  }

  /**
   * Check if repository is selected
   */
  const isRepoSelected = (repoName) => {
    return selectedRepos.includes(repoName)
  }

  // Show empty state if no repositories
  if (!repositories || repositories.length === 0) {
    return (
      <div className={styles.emptyState}>
        <p className="text-muted">No repositories to display</p>
      </div>
    )
  }

  return (
    <div className={styles.tableWrapper}>
      <div className={styles.tableContainer}>
        <table className={styles.table} role="table" aria-label="Repository comparison table">
          <TableHeader
            onSort={handleSort}
            sortField={localSortField}
            sortDirection={localSortDirection}
          />
          <tbody>
            {repositories.map((repo) => (
              <TableRow
                key={repo.name}
                repository={repo}
                isSelected={isRepoSelected(repo.name)}
                onSelect={onSelectRepo}
                onClick={onRowClick}
              />
            ))}
          </tbody>
        </table>
      </div>

      {/* Table Footer with Summary */}
      <div className={styles.tableFooter}>
        <p className="text-sm text-muted">
          Showing {repositories.length} {repositories.length === 1 ? 'repository' : 'repositories'}
          {selectedRepos.length > 0 && (
            <> • {selectedRepos.length} selected for comparison</>
          )}
        </p>
      </div>
    </div>
  )
}
