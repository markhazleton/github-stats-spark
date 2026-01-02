import React, { useState } from 'react'
import PropTypes from 'prop-types'

/**
 * ExportButton Component
 *
 * Provides export functionality for repository data in CSV or JSON format.
 * Uses client-side generation with FileSaver.js pattern.
 *
 * @component
 * @param {Object} props
 * @param {Array} props.data - Array of repository objects to export
 * @param {string} [props.filename='repositories'] - Base filename for export
 * @param {string} [props.label='Export'] - Button label
 * @param {boolean} [props.disabled=false] - Whether button is disabled
 */
function ExportButton({ data, filename = 'repositories', label = 'Export', disabled = false }) {
  const [isExporting, setIsExporting] = useState(false)
  const [showMenu, setShowMenu] = useState(false)

  /**
   * Convert repositories to CSV format
   */
  const convertToCSV = (repositories) => {
    if (!Array.isArray(repositories) || repositories.length === 0) {
      return ''
    }

    // Define CSV columns
    const columns = [
      { key: 'name', label: 'Repository Name' },
      { key: 'language', label: 'Language' },
      { key: 'stars', label: 'Stars' },
      { key: 'forks', label: 'Forks' },
      { key: 'watchers', label: 'Watchers' },
      { key: 'open_issues', label: 'Open Issues' },
      { key: 'created_at', label: 'Created At' },
      { key: 'updated_at', label: 'Last Updated' },
      { key: 'commit_history.total_commits', label: 'Total Commits' },
      { key: 'commit_history.recent_90d', label: 'Commits (90d)' },
      { key: 'commit_history.recent_180d', label: 'Commits (180d)' },
      { key: 'commit_history.recent_365d', label: 'Commits (365d)' },
      { key: 'commit_history.first_commit_date', label: 'First Commit' },
      { key: 'commit_history.last_commit_date', label: 'Last Commit' },
      { key: 'commit_metrics.avg_size', label: 'Avg Commit Size' },
      { key: 'commit_metrics.largest_commit.size', label: 'Largest Commit' },
      { key: 'commit_metrics.smallest_commit.size', label: 'Smallest Commit' },
      { key: 'commit_velocity', label: 'Commit Velocity' },
      { key: 'age_days', label: 'Age (days)' },
      { key: 'days_since_last_push', label: 'Days Since Push' },
      { key: 'has_readme', label: 'Has README' },
      { key: 'has_license', label: 'Has License' },
      { key: 'has_ci_cd', label: 'Has CI/CD' },
      { key: 'has_tests', label: 'Has Tests' },
    ]

    // Helper to get nested value
    const getNestedValue = (obj, path) => {
      return path.split('.').reduce((acc, part) => acc?.[part], obj)
    }

    // Create CSV header
    const header = columns.map(col => `"${col.label}"`).join(',')

    // Create CSV rows
    const rows = repositories.map(repo => {
      return columns.map(col => {
        const value = getNestedValue(repo, col.key)

        // Handle null/undefined
        if (value === null || value === undefined) return '""'

        // Handle booleans
        if (typeof value === 'boolean') return value ? 'Yes' : 'No'

        // Handle numbers
        if (typeof value === 'number') return value

        // Handle strings (escape quotes)
        return `"${String(value).replace(/"/g, '""')}"`
      }).join(',')
    })

    return [header, ...rows].join('\n')
  }

  /**
   * Download file with given content
   */
  const downloadFile = (content, filename, mimeType) => {
    const blob = new Blob([content], { type: mimeType })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = filename
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    URL.revokeObjectURL(url)
  }

  /**
   * Export as CSV
   */
  const handleExportCSV = async () => {
    setIsExporting(true)
    setShowMenu(false)

    try {
      const csv = convertToCSV(data)

      if (!csv) {
        alert('No data to export')
        return
      }

      const timestamp = new Date().toISOString().split('T')[0]
      const fullFilename = `${filename}-${timestamp}.csv`

      downloadFile(csv, fullFilename, 'text/csv;charset=utf-8;')
    } catch (error) {
      console.error('CSV export failed:', error)
      alert('Export failed. Please try again.')
    } finally {
      setIsExporting(false)
    }
  }

  /**
   * Export as JSON
   */
  const handleExportJSON = async () => {
    setIsExporting(true)
    setShowMenu(false)

    try {
      if (!data || data.length === 0) {
        alert('No data to export')
        return
      }

      const json = JSON.stringify(data, null, 2)
      const timestamp = new Date().toISOString().split('T')[0]
      const fullFilename = `${filename}-${timestamp}.json`

      downloadFile(json, fullFilename, 'application/json;charset=utf-8;')
    } catch (error) {
      console.error('JSON export failed:', error)
      alert('Export failed. Please try again.')
    } finally {
      setIsExporting(false)
    }
  }

  return (
    <div className="export-button-wrapper" style={{ position: 'relative', display: 'inline-block' }}>
      <button
        className="btn btn-secondary"
        onClick={() => setShowMenu(!showMenu)}
        disabled={disabled || isExporting || !data || data.length === 0}
        aria-label="Export data"
        aria-expanded={showMenu}
        aria-haspopup="true"
      >
        {isExporting ? 'Exporting...' : label}
        <span style={{ marginLeft: '0.5rem' }}>▼</span>
      </button>

      {showMenu && (
        <div
          className="export-menu"
          style={{
            position: 'absolute',
            top: '100%',
            right: 0,
            marginTop: '0.5rem',
            backgroundColor: 'var(--color-bg-primary)',
            border: '1px solid var(--color-border)',
            borderRadius: 'var(--border-radius)',
            boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
            zIndex: 1000,
            minWidth: '150px',
          }}
        >
          <button
            className="export-menu-item"
            onClick={handleExportCSV}
            style={{
              display: 'block',
              width: '100%',
              padding: 'var(--spacing-sm) var(--spacing-md)',
              textAlign: 'left',
              border: 'none',
              background: 'none',
              cursor: 'pointer',
              fontSize: 'var(--font-size-base)',
            }}
            onMouseEnter={(e) => {
              e.target.style.backgroundColor = 'var(--color-bg-secondary)'
            }}
            onMouseLeave={(e) => {
              e.target.style.backgroundColor = 'transparent'
            }}
          >
            Export as CSV
          </button>
          <button
            className="export-menu-item"
            onClick={handleExportJSON}
            style={{
              display: 'block',
              width: '100%',
              padding: 'var(--spacing-sm) var(--spacing-md)',
              textAlign: 'left',
              border: 'none',
              background: 'none',
              cursor: 'pointer',
              fontSize: 'var(--font-size-base)',
            }}
            onMouseEnter={(e) => {
              e.target.style.backgroundColor = 'var(--color-bg-secondary)'
            }}
            onMouseLeave={(e) => {
              e.target.style.backgroundColor = 'transparent'
            }}
          >
            Export as JSON
          </button>
        </div>
      )}

      {/* Clickout handler */}
      {showMenu && (
        <div
          style={{
            position: 'fixed',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            zIndex: 999,
          }}
          onClick={() => setShowMenu(false)}
        />
      )}
    </div>
  )
}

ExportButton.propTypes = {
  data: PropTypes.array.isRequired,
  filename: PropTypes.string,
  label: PropTypes.string,
  disabled: PropTypes.bool,
}

export default ExportButton
