import React from 'react'
import Tooltip from '@/components/Common/Tooltip'
import styles from './RepositoryTable.module.css'

/**
 * TableRow Component
 *
 * Renders a single repository row with all metrics.
 * Handles formatting, edge cases (missing data), and user interactions.
 * Optimized with React.memo for performance with 100+ rows.
 *
 * @component
 * @param {Object} props - Component props
 * @param {Object} props.repository - Repository object with metrics
 * @param {boolean} [props.isSelected] - Whether row is selected for comparison
 * @param {Function} [props.onSelect] - Callback when selection checkbox is toggled
 * @param {Function} [props.onClick] - Callback when row is clicked for drill-down
 *
 * @example
 * <TableRow
 *   repository={repo}
 *   isSelected={true}
 *   onSelect={(name) => toggleSelection(name)}
 *   onClick={(repo) => showDetails(repo)}
 * />
 */
const TableRow = React.memo(function TableRow({ repository, isSelected = false, onSelect, onClick }) {
  /**
   * Format date to readable string (MM/DD/YYYY)
   */
  const formatDate = (dateString) => {
    if (!dateString) return 'N/A'

    try {
      const date = new Date(dateString)
      if (isNaN(date.getTime())) return 'N/A'

      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
      })
    } catch (error) {
      return 'N/A'
    }
  }

  /**
   * Format commit size with proper number formatting
   */
  const formatSize = (size) => {
    if (size == null || isNaN(size)) return 'N/A'
    
    // Show 0 if it's actually 0 (valid data)
    if (size === 0) return '0.0'

    // Round to 1 decimal place
    return parseFloat(size).toFixed(1)
  }

  /**
   * Format commit metric object (for largest/smallest commits)
   */
  const formatCommitMetric = (commitMetric) => {
    // Check if the object exists first
    if (!commitMetric) {
      return { display: 'N/A', tooltip: null }
    }

    // If size is explicitly 0, show it (rather than N/A)
    const size = commitMetric.size
    const display = size != null ? formatSize(size) : 'N/A'
    
    // Only create tooltip if we have meaningful data
    const hasData = commitMetric.sha || commitMetric.date
    const tooltip = hasData 
      ? `${commitMetric.sha?.substring(0, 7) || 'Unknown'} • ${formatDate(commitMetric.date)}`
      : null

    return { display, tooltip }
  }

  /**
   * Handle row click (for drill-down)
   */
  const handleRowClick = (e) => {
    // Don't trigger if clicking checkbox or link
    if (e.target.type === 'checkbox' || e.target.tagName === 'A') {
      return
    }

    if (onClick) {
      onClick(repository)
    }
  }

  /**
   * Handle checkbox change
   */
  const handleCheckboxChange = (e) => {
    e.stopPropagation() // Prevent row click

    if (onSelect) {
      onSelect(repository.name)
    }
  }

  const language = repository.language || 'Unknown'
  
  // Extract commit data from nested structure (unified data format)
  const commitHistory = repository.commit_history || {}
  const commitMetrics = repository.commit_metrics || {}
  const totalCommits = commitHistory.total_commits || repository.commit_count || 0
  const firstCommitDate = commitHistory.first_commit_date || repository.first_commit_date
  const lastCommitDate = commitHistory.last_commit_date || repository.last_commit_date
  const avgCommitSize = commitMetrics.avg_size || repository.avg_commit_size
  
  const largestCommit = formatCommitMetric(commitMetrics.largest_commit || repository.largest_commit)
  const smallestCommit = formatCommitMetric(commitMetrics.smallest_commit || repository.smallest_commit)

  return (
    <tr
      className={`${styles.tableRow} ${isSelected ? styles.tableRowSelected : ''}`}
      onClick={handleRowClick}
      role="row"
    >
      {/* Repository Name */}
      <td className={styles.tableCell}>
        <div className={styles.tableCellContent}>
          {onSelect && (
            <input
              type="checkbox"
              checked={isSelected}
              onChange={handleCheckboxChange}
              aria-label={`Select ${repository.name} for comparison`}
              className={styles.checkbox}
            />
          )}
          <button
            className={styles.repoNameButton}
            onClick={() => onClick && onClick(repository)}
            title={`View details for ${repository.name}`}
          >
            {repository.name}
          </button>
        </div>
      </td>

      {/* Language */}
      <td className={styles.tableCell}>
        <span className={`${styles.badge} ${styles[`badge--${language.toLowerCase()}`]}`}>
          {language}
        </span>
      </td>

      {/* Created Date */}
      <td className={styles.tableCell}>
        {formatDate(repository.created_at)}
      </td>

      {/* First Commit Date */}
      <td className={styles.tableCell}>
        {formatDate(firstCommitDate)}
      </td>

      {/* Last Commit Date */}
      <td className={styles.tableCell}>
        {formatDate(lastCommitDate)}
      </td>

      {/* Total Commits */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        {totalCommits.toLocaleString()}
      </td>

      {/* Average Commit Size */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="Average size = files changed + lines added + lines deleted">
          {formatSize(avgCommitSize)}
        </Tooltip>
      </td>

      {/* Largest Commit */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        {largestCommit.tooltip ? (
          <Tooltip content={largestCommit.tooltip}>
            {largestCommit.display}
          </Tooltip>
        ) : (
          largestCommit.display
        )}
      </td>

      {/* Smallest Commit */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        {smallestCommit.tooltip ? (
          <Tooltip content={smallestCommit.tooltip}>
            {smallestCommit.display}
          </Tooltip>
        ) : (
          smallestCommit.display
        )}
      </td>

      {/* Stars */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="GitHub stars">
          {repository.stars?.toLocaleString() || 0}
        </Tooltip>
      </td>
    </tr>
  )
})

export default TableRow
