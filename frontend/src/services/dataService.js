/**
 * GitHub Stats Spark Dashboard - Data Service
 *
 * This service handles fetching dashboard JSON data from the generated data files.
 * In production (GitHub Pages), it fetches from the /docs/data/ directory.
 * In development, it uses the configured base path.
 *
 * @module dataService
 */

/**
 * Get the base URL for data fetching based on environment
 * @returns {string} Base URL for data files
 */
const getDataBaseUrl = () => {
  // In development, use relative path
  if (import.meta.env.DEV) {
    return '/data'
  }

  // In production (GitHub Pages), use the configured base path
  return `${import.meta.env.BASE_URL}data`
}

/**
 * Fetch dashboard data from repositories.json with automatic retry
 *
 * @param {number} maxRetries - Maximum number of retry attempts (default: 3)
 * @param {number} retryDelay - Delay between retries in ms (default: 2000)
 * @returns {Promise<Object>} Dashboard data object containing:
 *   - repositories: Array of repository objects with metrics
 *   - profile: User profile information
 *   - metadata: Generation metadata and schema version
 *
 * @throws {Error} If fetch fails after all retries or data is invalid
 *
 * @example
 * const data = await fetchDashboardData()
 * console.log(`Loaded ${data.repositories.length} repositories`)
 */
export async function fetchDashboardData(maxRetries = 3, retryDelay = 2000) {
  const baseUrl = getDataBaseUrl()
  const url = `${baseUrl}/repositories.json`

  let lastError = null;
  
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url)

      if (!response.ok) {
        throw new Error(`Failed to fetch dashboard data: ${response.status} ${response.statusText}`)
      }

      const data = await response.json()

      // Validate data structure
      if (!data || typeof data !== 'object') {
        throw new Error('Invalid dashboard data: expected object')
      }

      if (!Array.isArray(data.repositories)) {
        throw new Error('Invalid dashboard data: repositories must be an array')
      }

      // Success - log if retried
      if (attempt > 0) {
        console.log(`Successfully fetched data after ${attempt} ${attempt === 1 ? 'retry' : 'retries'}`)
      }

      return data
    } catch (error) {
      lastError = error
      console.error(`Error fetching dashboard data (attempt ${attempt + 1}/${maxRetries + 1}):`, error)
      
      // Don't retry on the last attempt
      if (attempt < maxRetries) {
        console.log(`Retrying in ${retryDelay / 1000} seconds...`)
        await new Promise(resolve => setTimeout(resolve, retryDelay))
      }
    }
  }
  
  // All retries exhausted
  console.error('Failed to fetch dashboard data after all retry attempts')
  throw lastError
}

/**
 * Fetch user profile data (if stored separately)
 *
 * @returns {Promise<Object>} User profile object
 * @throws {Error} If fetch fails
 */
export async function fetchUserProfile() {
  const baseUrl = getDataBaseUrl()
  const url = `${baseUrl}/profile.json`

  try {
    const response = await fetch(url)

    if (!response.ok) {
      // Profile data might not exist as separate file
      console.warn('Profile data not found, using data from repositories.json')
      return null
    }

    return await response.json()
  } catch (error) {
    console.warn('Error fetching profile data:', error)
    return null
  }
}

/**
 * Extract unique programming languages from repositories
 *
 * @param {Array} repositories - Array of repository objects
 * @returns {Array<string>} Sorted array of unique language names
 *
 * @example
 * const languages = extractLanguages(data.repositories)
 * // Returns: ['JavaScript', 'Python', 'TypeScript', ...]
 */
export function extractLanguages(repositories) {
  if (!Array.isArray(repositories)) {
    return []
  }

  const languageSet = new Set()

  repositories.forEach((repo) => {
    if (repo.language && repo.language !== 'Unknown') {
      languageSet.add(repo.language)
    }
  })

  return Array.from(languageSet).sort()
}

/**
 * Filter repositories by programming language
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} language - Language to filter by (or null for all)
 * @returns {Array} Filtered repository array
 *
 * @example
 * const pythonRepos = filterByLanguage(data.repositories, 'Python')
 */
export function filterByLanguage(repositories, language) {
  if (!language || language === 'all') {
    return repositories
  }

  return repositories.filter((repo) => repo.language === language)
}

/**
 * Sort repositories by a specific field
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} field - Field name to sort by (e.g., 'stars', 'commit_count')
 * @param {string} direction - Sort direction ('asc' or 'desc')
 * @returns {Array} Sorted repository array (new array, does not mutate original)
 *
 * @example
 * const sorted = sortRepositories(data.repositories, 'stars', 'desc')
 */
export function sortRepositories(repositories, field, direction = 'desc') {
  if (!Array.isArray(repositories)) {
    return []
  }

  // Create a copy to avoid mutating original array
  const sorted = [...repositories]

  sorted.sort((a, b) => {
    let aValue = a[field]
    let bValue = b[field]

    // Handle date fields
    if (field.includes('date') || field.includes('Date')) {
      aValue = new Date(aValue).getTime()
      bValue = new Date(bValue).getTime()
    }

    // Handle null/undefined values
    if (aValue == null) return 1
    if (bValue == null) return -1

    // Numeric or string comparison
    if (direction === 'asc') {
      return aValue < bValue ? -1 : aValue > bValue ? 1 : 0
    } else {
      return aValue > bValue ? -1 : aValue < bValue ? 1 : 0
    }
  })

  return sorted
}

/**
 * Search repositories by name or description
 *
 * @param {Array} repositories - Array of repository objects
 * @param {string} query - Search query string
 * @returns {Array} Filtered repositories matching query
 *
 * @example
 * const results = searchRepositories(data.repositories, 'react')
 */
export function searchRepositories(repositories, query) {
  if (!query || query.trim() === '') {
    return repositories
  }

  const lowerQuery = query.toLowerCase().trim()

  return repositories.filter((repo) => {
    const nameMatch = repo.name?.toLowerCase().includes(lowerQuery)
    const descMatch = repo.description?.toLowerCase().includes(lowerQuery)
    const langMatch = repo.language?.toLowerCase().includes(lowerQuery)

    return nameMatch || descMatch || langMatch
  })
}

/**
 * Calculate aggregate statistics from repository data
 *
 * @param {Array} repositories - Array of repository objects
 * @returns {Object} Aggregate statistics
 *
 * @example
 * const stats = calculateStats(data.repositories)
 * // Returns: { totalCommits: 1234, totalStars: 567, avgCommitSize: 42.5, ... }
 */
export function calculateStats(repositories) {
  if (!Array.isArray(repositories) || repositories.length === 0) {
    return {
      totalCommits: 0,
      totalStars: 0,
      totalForks: 0,
      avgCommitSize: 0,
      languageCount: 0,
    }
  }

  const totalCommits = repositories.reduce((sum, repo) => sum + (repo.commit_count || 0), 0)
  const totalStars = repositories.reduce((sum, repo) => sum + (repo.stars || 0), 0)
  const totalForks = repositories.reduce((sum, repo) => sum + (repo.forks || 0), 0)

  const avgCommitSize = repositories.reduce((sum, repo) => sum + (repo.avg_commit_size || 0), 0) / repositories.length

  const languages = extractLanguages(repositories)

  return {
    totalCommits,
    totalStars,
    totalForks,
    avgCommitSize: Math.round(avgCommitSize * 100) / 100, // Round to 2 decimals
    languageCount: languages.length,
  }
}

export default {
  fetchDashboardData,
  fetchUserProfile,
  extractLanguages,
  filterByLanguage,
  sortRepositories,
  searchRepositories,
  calculateStats,
}
