import React, { useState, useMemo } from 'react'
import useRepositoryData from '@/hooks/useRepositoryData'
import RepositoryTable from '@/components/RepositoryTable/RepositoryTable'
import LoadingState from '@/components/Common/LoadingState'
import { sortRepositories, filterByLanguage, extractLanguages } from '@/services/dataService'

/**
 * GitHub Stats Spark Dashboard - Root App Component
 *
 * This is the main application component that orchestrates the dashboard layout,
 * state management, and routing between different views (table, charts, comparison, drill-down).
 *
 * Features:
 * - Data fetching via useRepositoryData custom hook
 * - View state management (table, visualizations, comparison)
 * - Modal state for drill-down details
 * - Loading and error state handling
 *
 * @component
 */
function App() {
  // Data fetching with custom hook
  const { data, loading, error } = useRepositoryData()

  // View state management
  const [currentView, setCurrentView] = useState('table') // 'table', 'visualizations', 'comparison'
  const [selectedRepos, setSelectedRepos] = useState([]) // For comparison view
  const [detailModalRepo, setDetailModalRepo] = useState(null) // For drill-down

  // Table state management
  const [sortField, setSortField] = useState('stars')
  const [sortDirection, setSortDirection] = useState('desc')
  const [languageFilter, setLanguageFilter] = useState('all')

  /**
   * Handle repository selection for comparison
   * @param {string} repoName - Repository name to toggle
   */
  const handleRepoSelect = (repoName) => {
    setSelectedRepos((prev) => {
      if (prev.includes(repoName)) {
        return prev.filter((name) => name !== repoName)
      } else if (prev.length < 5) {
        // Max 5 repositories for comparison
        return [...prev, repoName]
      } else {
        // Show warning if trying to select more than 5
        console.warn('Maximum 5 repositories can be compared')
        return prev
      }
    })
  }

  /**
   * Handle repository drill-down
   * @param {Object} repository - Repository object to display details for
   */
  const handleRepoClick = (repository) => {
    setDetailModalRepo(repository)
  }

  /**
   * Close detail modal
   */
  const closeDetailModal = () => {
    setDetailModalRepo(null)
  }

  /**
   * Handle table sorting
   * @param {string} field - Field name to sort by
   * @param {string} direction - Sort direction ('asc' or 'desc')
   */
  const handleSort = (field, direction) => {
    setSortField(field)
    setSortDirection(direction)
  }

  /**
   * Handle language filter change
   * @param {string} language - Language to filter by (or 'all')
   */
  const handleLanguageFilter = (language) => {
    setLanguageFilter(language)
  }

  /**
   * Get filtered and sorted repositories
   * Uses useMemo for performance optimization
   */
  const processedRepositories = useMemo(() => {
    if (!data?.repositories) return []

    // Apply language filter
    let filtered = filterByLanguage(data.repositories, languageFilter)

    // Apply sorting
    filtered = sortRepositories(filtered, sortField, sortDirection)

    return filtered
  }, [data?.repositories, languageFilter, sortField, sortDirection])

  /**
   * Get available languages for filter dropdown
   */
  const availableLanguages = useMemo(() => {
    if (!data?.repositories) return []
    return extractLanguages(data.repositories)
  }, [data?.repositories])

  return (
    <div className="app">
      {/* Header */}
      <header className="header">
        <div className="container">
          <div className="flex items-center justify-between" style={{ height: 'var(--header-height)' }}>
            <div className="flex items-center gap-md">
              <h1 style={{ marginBottom: 0 }}>GitHub Stats Spark</h1>
              {data?.profile && (
                <div className="badge">
                  {data.profile.username}
                </div>
              )}
            </div>

            {/* View Toggle Buttons */}
            <nav className="flex gap-sm">
              <button
                className={`btn ${currentView === 'table' ? 'btn-primary' : ''}`}
                onClick={() => setCurrentView('table')}
                aria-pressed={currentView === 'table'}
              >
                Table View
              </button>
              <button
                className={`btn ${currentView === 'visualizations' ? 'btn-primary' : ''}`}
                onClick={() => setCurrentView('visualizations')}
                aria-pressed={currentView === 'visualizations'}
              >
                Visualizations
              </button>
              <button
                className={`btn ${currentView === 'comparison' ? 'btn-primary' : ''}`}
                onClick={() => setCurrentView('comparison')}
                aria-pressed={currentView === 'comparison'}
                disabled={selectedRepos.length < 2}
              >
                Comparison ({selectedRepos.length})
              </button>
            </nav>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="main">
        <div className="container">
          <div className="mt-xl mb-xl">
            {/* Loading State */}
            {loading && <LoadingState message="Loading repository data..." size="large" />}

            {/* Error State */}
            {error && !loading && (
              <div className="card" style={{ backgroundColor: 'var(--color-error)', color: 'white' }}>
                <h3>Error Loading Data</h3>
                <p>{error.message || 'Failed to load repository data'}</p>
                <p className="text-sm">Please check your network connection and try again.</p>
              </div>
            )}

            {/* Data Loaded - Render Current View */}
            {!loading && !error && data && (
              <>
                {currentView === 'table' && (
                  <div>
                    <div className="flex justify-between items-center mb-lg">
                      <div>
                        <h2>Repository Overview</h2>
                        <p className="text-muted">
                          Showing {processedRepositories.length} of {data.repositories?.length || 0} repositories
                        </p>
                      </div>

                      {/* Language Filter */}
                      {availableLanguages.length > 0 && (
                        <div>
                          <label htmlFor="language-filter" className="text-sm text-muted" style={{ marginRight: 'var(--spacing-sm)' }}>
                            Filter by language:
                          </label>
                          <select
                            id="language-filter"
                            className="btn"
                            value={languageFilter}
                            onChange={(e) => handleLanguageFilter(e.target.value)}
                            aria-label="Filter repositories by programming language"
                          >
                            <option value="all">All Languages</option>
                            {availableLanguages.map((lang) => (
                              <option key={lang} value={lang}>
                                {lang}
                              </option>
                            ))}
                          </select>
                        </div>
                      )}
                    </div>

                    {/* Repository Table */}
                    <RepositoryTable
                      repositories={processedRepositories}
                      onSort={handleSort}
                      onSelectRepo={handleRepoSelect}
                      onRowClick={handleRepoClick}
                      selectedRepos={selectedRepos}
                      sortField={sortField}
                      sortDirection={sortDirection}
                    />
                  </div>
                )}

                {currentView === 'visualizations' && (
                  <div>
                    <h2>Data Visualizations</h2>
                    <p className="text-muted">Interactive charts and graphs</p>
                    {/* Visualization components will be rendered here in US3 */}
                    <div className="card mt-lg">
                      <p className="text-center text-muted">
                        Visualization components will be implemented in User Story 3
                      </p>
                    </div>
                  </div>
                )}

                {currentView === 'comparison' && (
                  <div>
                    <h2>Repository Comparison</h2>
                    <p className="text-muted">
                      Comparing {selectedRepos.length} repositories
                    </p>
                    {/* ComparisonView component will be rendered here in US4 */}
                    <div className="card mt-lg">
                      <p className="text-center text-muted">
                        Comparison view will be implemented in User Story 4
                      </p>
                    </div>
                  </div>
                )}
              </>
            )}
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="footer" style={{ borderTop: '1px solid var(--color-border)', padding: 'var(--spacing-lg) 0' }}>
        <div className="container">
          <div className="flex justify-between items-center">
            <p className="text-sm text-muted">
              Generated with{' '}
              <a href="https://github.com/markhazleton/github-stats-spark" target="_blank" rel="noopener noreferrer">
                GitHub Stats Spark
              </a>
            </p>
            {data?.metadata && (
              <p className="text-xs text-muted">
                Last updated: {new Date(data.metadata.generated_at).toLocaleDateString()}
                {' • '}
                Schema v{data.metadata.schema_version}
              </p>
            )}
          </div>
        </div>
      </footer>

      {/* Detail Modal (for drill-down - will be implemented in US5) */}
      {detailModalRepo && (
        <div className="modal-backdrop" onClick={closeDetailModal}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <div className="card">
              <h3>Repository Details</h3>
              <p>Detail modal for {detailModalRepo.name} will be implemented in User Story 5</p>
              <button className="btn mt-md" onClick={closeDetailModal}>
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
