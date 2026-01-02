/**
 * Metrics Calculator - Utility Functions
 *
 * Provides formatting and calculation utilities for dashboard metrics.
 * Used across components for consistent data display.
 *
 * @module metricsCalculator
 */

/**
 * Format ISO date string to readable format
 *
 * @param {string} isoDateString - ISO 8601 date string
 * @param {string} [format='short'] - Format type ('short', 'long', 'relative')
 * @returns {string} Formatted date string
 *
 * @example
 * formatDate('2024-01-15T10:30:00Z') // "Jan 15, 2024"
 * formatDate('2024-01-15T10:30:00Z', 'long') // "January 15, 2024"
 */
export function formatDate(isoDateString, format = 'short') {
  if (!isoDateString) return 'N/A'

  try {
    const date = new Date(isoDateString)
    if (isNaN(date.getTime())) return 'N/A'

    if (format === 'short') {
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
      })
    } else if (format === 'long') {
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      })
    } else if (format === 'relative') {
      return formatRelativeDate(date)
    }

    return date.toLocaleDateString()
  } catch (error) {
    console.error('Error formatting date:', error)
    return 'N/A'
  }
}

/**
 * Format date as relative time (e.g., "2 days ago", "3 months ago")
 *
 * @param {Date} date - Date object
 * @returns {string} Relative time string
 */
function formatRelativeDate(date) {
  const now = new Date()
  const diffMs = now - date
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))

  if (diffDays === 0) return 'Today'
  if (diffDays === 1) return 'Yesterday'
  if (diffDays < 7) return `${diffDays} days ago`
  if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`
  if (diffDays < 365) return `${Math.floor(diffDays / 30)} months ago`

  return `${Math.floor(diffDays / 365)} years ago`
}

/**
 * Format commit size with proper number display
 *
 * @param {number} size - Commit size (files + lines changed)
 * @param {number} [decimals=1] - Number of decimal places
 * @returns {string} Formatted size string
 *
 * @example
 * formatCommitSize(42.567) // "42.6"
 * formatCommitSize(1234.5, 0) // "1,235"
 */
export function formatCommitSize(size, decimals = 1) {
  if (size == null || isNaN(size)) return 'N/A'

  const formatted = parseFloat(size).toFixed(decimals)

  // Add thousands separator if needed
  if (size >= 1000) {
    return parseFloat(formatted).toLocaleString('en-US', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals,
    })
  }

  return formatted
}

/**
 * Format large numbers with K/M suffixes
 *
 * @param {number} num - Number to format
 * @param {number} [decimals=1] - Decimal places for abbreviated numbers
 * @returns {string} Formatted number string
 *
 * @example
 * formatNumber(1234) // "1.2K"
 * formatNumber(1234567) // "1.2M"
 * formatNumber(500) // "500"
 */
export function formatNumber(num, decimals = 1) {
  if (num == null || isNaN(num)) return '0'

  if (num >= 1000000) {
    return (num / 1000000).toFixed(decimals) + 'M'
  } else if (num >= 1000) {
    return (num / 1000).toFixed(decimals) + 'K'
  }

  return num.toString()
}

/**
 * Transform repository data for chart visualization
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} xField - Field name for x-axis
 * @param {string} yField - Field name for y-axis
 * @returns {Array} Chart data array
 *
 * @example
 * const chartData = transformForChart(repos, 'name', 'commit_count')
 * // Returns: [{ x: 'repo1', y: 123 }, { x: 'repo2', y: 456 }]
 */
export function transformForChart(repositories, xField, yField) {
  if (!Array.isArray(repositories)) return []

  return repositories.map((repo) => ({
    x: repo[xField],
    y: repo[yField] || 0,
    label: repo.name,
    ...repo, // Include full repo data for tooltips
  }))
}

/**
 * Calculate percentile value from array
 *
 * @param {Array<number>} values - Array of numeric values
 * @param {number} percentile - Percentile (0-100)
 * @returns {number} Percentile value
 *
 * @example
 * calculatePercentile([1, 2, 3, 4, 5], 50) // 3 (median)
 */
export function calculatePercentile(values, percentile) {
  if (!Array.isArray(values) || values.length === 0) return 0

  const sorted = [...values].sort((a, b) => a - b)
  const index = (percentile / 100) * (sorted.length - 1)
  const lower = Math.floor(index)
  const upper = Math.ceil(index)
  const weight = index % 1

  if (lower === upper) {
    return sorted[lower]
  }

  return sorted[lower] * (1 - weight) + sorted[upper] * weight
}

/**
 * Group repositories by language
 *
 * @param {Array} repositories - Array of repository objects
 * @returns {Object} Language groups with counts
 *
 * @example
 * groupByLanguage(repos)
 * // Returns: { 'JavaScript': 15, 'Python': 10, 'TypeScript': 8 }
 */
export function groupByLanguage(repositories) {
  if (!Array.isArray(repositories)) return {}

  return repositories.reduce((acc, repo) => {
    const lang = repo.language || 'Unknown'
    acc[lang] = (acc[lang] || 0) + 1
    return acc
  }, {})
}

/**
 * Calculate average metric value
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} field - Field name to average
 * @returns {number} Average value
 *
 * @example
 * calculateAverage(repos, 'commit_count') // 42.5
 */
export function calculateAverage(repositories, field) {
  if (!Array.isArray(repositories) || repositories.length === 0) return 0

  const sum = repositories.reduce((acc, repo) => acc + (repo[field] || 0), 0)
  return sum / repositories.length
}

/**
 * Find repository with max/min value for a field
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} field - Field name to compare
 * @param {string} type - 'max' or 'min'
 * @returns {Object|null} Repository with max/min value
 *
 * @example
 * findExtreme(repos, 'stars', 'max') // Repository with most stars
 */
export function findExtreme(repositories, field, type = 'max') {
  if (!Array.isArray(repositories) || repositories.length === 0) return null

  return repositories.reduce((extreme, repo) => {
    if (!extreme) return repo

    const currentValue = repo[field] || 0
    const extremeValue = extreme[field] || 0

    if (type === 'max') {
      return currentValue > extremeValue ? repo : extreme
    } else {
      return currentValue < extremeValue ? repo : extreme
    }
  }, null)
}

/**
 * Transform repository data for bar chart visualization
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} metricId - Metric to display (e.g., 'totalCommits', 'avgCommitSize')
 * @returns {Array} Chart data array with {name, value, language} objects
 *
 * @example
 * transformForBarChart(repos, 'totalCommits')
 * // Returns: [{ name: 'repo1', value: 123, language: 'JavaScript' }, ...]
 */
export function transformForBarChart(repositories, metricId) {
  if (!Array.isArray(repositories)) return []

  return repositories
    .map((repo) => ({
      name: repo.name || 'Unknown',
      value: getMetricValue(repo, metricId),
      language: repo.language || 'Unknown',
      fullData: repo,
    }))
    .filter((item) => item.value != null)
    .sort((a, b) => b.value - a.value) // Sort descending by value
    .slice(0, 50) // Limit to top 50 for horizontal bar chart
}

/**
 * Transform repository data for line graph visualization
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} metricId - Metric to display
 * @returns {Array} Chart data array with {name, value, date} objects
 *
 * @example
 * transformForLineGraph(repos, 'lastCommitDate')
 * // Returns: [{ name: 'repo1', value: timestamp, date: '2024-01-15' }, ...]
 */
export function transformForLineGraph(repositories, metricId) {
  if (!Array.isArray(repositories)) return []

  const data = repositories
    .map((repo) => {
      const value = getMetricValue(repo, metricId)
      const date = metricId.includes('Date') ? value : repo.lastCommitDate || repo.firstCommitDate

      return {
        name: repo.name || 'Unknown',
        value: value,
        date: date,
        language: repo.language || 'Unknown',
        fullData: repo,
      }
    })
    .filter((item) => item.value != null && item.date != null)

  // Sort by date
  return data.sort((a, b) => {
    const dateA = new Date(a.date)
    const dateB = new Date(b.date)
    return dateA - dateB
  })
}

/**
 * Transform repository data for scatter plot visualization
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} xMetric - Metric for x-axis (default: 'totalCommits')
 * @param {string} yMetric - Metric for y-axis (default: 'avgCommitSize')
 * @returns {Array} Chart data array with {name, x, y, language} objects
 *
 * @example
 * transformForScatterPlot(repos, 'totalCommits', 'avgCommitSize')
 * // Returns: [{ name: 'repo1', x: 123, y: 45.6, language: 'JS' }, ...]
 */
export function transformForScatterPlot(repositories, xMetric = 'totalCommits', yMetric = 'avgCommitSize') {
  if (!Array.isArray(repositories)) return []

  return repositories
    .map((repo) => ({
      name: repo.name || 'Unknown',
      x: getMetricValue(repo, xMetric),
      y: getMetricValue(repo, yMetric),
      language: repo.language || 'Unknown',
      fullData: repo,
    }))
    .filter((item) => item.x != null && item.y != null && !isNaN(item.x) && !isNaN(item.y))
}

/**
 * Get metric value from repository object by metric ID
 *
 * @param {Object} repo - Repository object
 * @param {string} metricId - Metric identifier
 * @returns {number|string|null} Metric value
 */
function getMetricValue(repo, metricId) {
  const metricMap = {
    totalCommits: repo.totalCommits || repo.commit_count || 0,
    avgCommitSize: repo.avgCommitSize || repo.avg_commit_size || 0,
    largestCommit: repo.largestCommit || repo.largest_commit || 0,
    smallestCommit: repo.smallestCommit || repo.smallest_commit || 0,
    firstCommitDate: repo.firstCommitDate || repo.first_commit_date,
    lastCommitDate: repo.lastCommitDate || repo.last_commit_date,
  }

  const value = metricMap[metricId]
  
  // For date metrics, return timestamp for chart calculations
  if (metricId.includes('Date') && value) {
    return new Date(value).getTime()
  }
  
  return value
}

/**
 * Get human-readable label for metric ID
 *
 * @param {string} metricId - Metric identifier
 * @returns {string} Human-readable label
 */
export function getMetricLabel(metricId) {
  const labels = {
    totalCommits: 'Total Commits',
    avgCommitSize: 'Average Commit Size',
    largestCommit: 'Largest Commit',
    smallestCommit: 'Smallest Commit',
    firstCommitDate: 'First Commit Date',
    lastCommitDate: 'Last Commit Date',
  }

  return labels[metricId] || metricId
}

/**
 * Calculate percentage difference between two values
 *
 * @param {number} value - Current value
 * @param {number} reference - Reference value (baseline)
 * @returns {number} Percentage difference (positive or negative)
 *
 * @example
 * calculatePercentageDifference(150, 100) // 50
 * calculatePercentageDifference(75, 100) // -25
 */
export function calculatePercentageDifference(value, reference) {
  if (reference === 0 || reference == null || value == null) return 0

  const diff = ((value - reference) / Math.abs(reference)) * 100
  return Math.round(diff)
}

/**
 * Compare two repository objects and calculate metric differences
 *
 * @param {Object} repo1 - First repository
 * @param {Object} repo2 - Second repository
 * @param {Array} metrics - Array of metric keys to compare
 * @returns {Object} Comparison result with differences
 *
 * @example
 * compareRepositories(repoA, repoB, ['stars', 'forks'])
 * // Returns: { stars: { diff: 50, percent: 25 }, ... }
 */
export function compareRepositories(repo1, repo2, metrics) {
  const comparison = {}

  metrics.forEach(metric => {
    const value1 = repo1[metric]
    const value2 = repo2[metric]

    if (typeof value1 === 'number' && typeof value2 === 'number') {
      comparison[metric] = {
        value1,
        value2,
        diff: value1 - value2,
        percent: calculatePercentageDifference(value1, value2),
      }
    } else {
      comparison[metric] = {
        value1,
        value2,
        diff: null,
        percent: null,
      }
    }
  })

  return comparison
}

/**
 * Rank repositories by a specific metric
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} metric - Metric to rank by
 * @param {string} [order='desc'] - Sort order ('asc' or 'desc')
 * @returns {Array} Ranked repositories with rank property
 */
export function rankRepositories(repositories, metric, order = 'desc') {
  if (!Array.isArray(repositories)) return []

  const sorted = [...repositories].sort((a, b) => {
    const aVal = a[metric] ?? 0
    const bVal = b[metric] ?? 0
    return order === 'desc' ? bVal - aVal : aVal - bVal
  })

  return sorted.map((repo, index) => ({
    ...repo,
    rank: index + 1,
  }))
}

export default {
  formatDate,
  formatCommitSize,
  formatNumber,
  transformForChart,
  calculatePercentile,
  groupByLanguage,
  calculateAverage,
  findExtreme,
  transformForBarChart,
  transformForLineGraph,
  transformForScatterPlot,
  getMetricLabel,
  calculatePercentageDifference,
  compareRepositories,
  rankRepositories,
}
