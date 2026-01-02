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

    // Round to 1 decimal place
    return parseFloat(size).toFixed(1)
  }

  /**
   * Format commit metric object (for largest/smallest commits)
   */
  const formatCommitMetric = (commitMetric) => {
    if (!commitMetric || !commitMetric.size) {
      return { display: 'N/A', tooltip: null }
    }

    const display = formatSize(commitMetric.size)
    const tooltip = `${commitMetric.sha?.substring(0, 7) || 'Unknown'} • ${formatDate(commitMetric.date)}`

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
  const largestCommit = formatCommitMetric(repository.largest_commit)
  const smallestCommit = formatCommitMetric(repository.smallest_commit)

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
          <a
            href={repository.url}
            target="_blank"
            rel="noopener noreferrer"
            className={styles.repoLink}
            onClick={(e) => e.stopPropagation()}
          >
            {repository.name}
          </a>
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
        {formatDate(repository.first_commit_date)}
      </td>

      {/* Last Commit Date */}
      <td className={styles.tableCell}>
        {formatDate(repository.last_commit_date)}
      </td>

      {/* Total Commits */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        {repository.commit_count?.toLocaleString() || 0}
      </td>

      {/* Average Commit Size */}
      <td className={`${styles.tableCell} ${styles.tableCellNumeric}`}>
        <Tooltip content="Average size = files changed + lines added + lines deleted">
          {formatSize(repository.avg_commit_size)}
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
