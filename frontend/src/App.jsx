import React, { useState, useMemo, Suspense, lazy, useEffect } from "react";
import { ViewportProvider } from "@/contexts/ViewportContext";
import useRepositoryData from "@/hooks/useRepositoryData";
import RepositoryTable from "@/components/RepositoryTable/RepositoryTable";
import LoadingState from "@/components/Common/LoadingState";
import FilterControls from "@/components/Common/FilterControls";
import { useTableSort } from "@/hooks/useTableSort";
import { extractLanguages, setupBackgroundSync } from "@/services/dataService";
import VisualizationControls from "@/components/Visualizations/VisualizationControls";
import { deferExecution, getConnectionType } from "@/utils/performance";
import CompareButton from "@/components/Comparison/CompareButton";
import MobileComparisonView from "@/components/Comparison/MobileComparisonView";
import { useBreakpoint } from "@/hooks/useMediaQuery";
import TabBar from "@/components/Mobile/TabBar/TabBar";
import EmptyState from "@/components/Mobile/EmptyState/EmptyState";
import OfflineIndicator from "@/components/Mobile/OfflineIndicator/OfflineIndicator";
import { ToastContainer } from "@/components/Mobile/Toast/Toast";
import SkipLink from "@/components/Layout/SkipLink/SkipLink";

// Lazy load chart components for better performance
const BarChart = lazy(() => import("@/components/Visualizations/BarChart"));
const LineGraph = lazy(() => import("@/components/Visualizations/LineGraph"));
const ScatterPlot = lazy(
  () => import("@/components/Visualizations/ScatterPlot"),
);
const RepositoryDetail = lazy(
  () => import("@/components/DrillDown/RepositoryDetail"),
);
const ComparisonSelector = lazy(
  () => import("@/components/Comparison/ComparisonSelector"),
);
const ComparisonView = lazy(
  () => import("@/components/Comparison/ComparisonView"),
);
import {
  transformForBarChart,
  transformForLineGraph,
  transformForScatterPlot,
  getMetricLabel,
} from "@/services/metricsCalculator";

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
  const { data, loading, error } = useRepositoryData();
  const { isMobile } = useBreakpoint();

  // Toast notifications state
  const [toasts, setToasts] = useState([]);

  /**
   * Add a toast notification
   */
  const addToast = (message, variant = "info", duration = 3000) => {
    const id = Date.now();
    setToasts((prev) => [...prev, { id, message, variant, duration }]);
  };

  /**
   * Remove a toast notification
   */
  const removeToast = (id) => {
    setToasts((prev) => prev.filter((toast) => toast.id !== id));
  };

  // Performance optimization on mount
  useEffect(() => {
    // Check connection type for adaptive loading
    const connectionType = getConnectionType();

    // Log connection info in development
    if (import.meta.env.DEV) {
      console.log("[Performance] Connection type:", connectionType);
    }

    // Defer non-critical operations based on connection quality
    if (connectionType !== "2g" && connectionType !== "slow-2g") {
      deferExecution(() => {
        // Preload comparison view for faster navigation
        // Will be loaded when browser is idle
      }, 3000);
    }
  }, []);

  // Setup background sync for offline/online transitions
  useEffect(() => {
    const cleanup = setupBackgroundSync(() => {
      console.log("[App] Data refreshed after coming online");
      addToast("Data refreshed successfully", "success", 3000);

      // The useRepositoryData hook should handle this automatically
      // No need to manually update state as the hook will refetch
    });

    return cleanup;
  }, []);

  // View state management
  const [currentView, setCurrentView] = useState("table"); // 'table', 'visualizations', 'comparison'
  const [selectedRepos, setSelectedRepos] = useState([]); // For comparison view
  const [detailModalRepo, setDetailModalRepo] = useState(null); // For drill-down

  // Visualization state
  const [chartType, setChartType] = useState("bar"); // 'bar', 'line', 'scatter'
  const [selectedMetric, setSelectedMetric] = useState("totalCommits");

  // Table sorting and filtering using useTableSort hook
  const {
    sortedData: processedRepositories,
    sortKey,
    sortOrder,
    filterLanguage,
    handleSort,
    handleFilterChange,
    clearFilter,
  } = useTableSort(data?.repositories || [], "stars", "desc");

  /**
   * Handle repository selection for comparison
   * @param {string} repoName - Repository name to toggle
   */
  const handleRepoSelect = (repoName) => {
    setSelectedRepos((prev) => {
      if (prev.includes(repoName)) {
        return prev.filter((name) => name !== repoName);
      } else if (prev.length < 5) {
        // Max 5 repositories for comparison
        return [...prev, repoName];
      } else {
        // Show warning if trying to select more than 5
        console.warn("Maximum 5 repositories can be compared");
        alert(
          "Maximum 5 repositories can be compared. Please deselect one first.",
        );
        return prev;
      }
    });
  };

  /**
   * Clear all repository selections
   */
  const handleClearSelection = () => {
    setSelectedRepos([]);
  };

  /**
   * Remove a specific repository from comparison
   * @param {string} repoName - Repository name to remove
   */
  const handleRemoveRepo = (repoName) => {
    setSelectedRepos((prev) => prev.filter((name) => name !== repoName));
  };

  /**
   * Get full repository objects for selected repositories
   */
  const selectedRepositoryObjects = useMemo(() => {
    if (!processedRepositories || selectedRepos.length === 0) return [];
    return processedRepositories.filter((repo) =>
      selectedRepos.includes(repo.name),
    );
  }, [processedRepositories, selectedRepos]);

  /**
   * Handle repository drill-down
   * @param {Object} repository - Repository object to display details for
   */
  const handleRepoClick = (repository) => {
    setDetailModalRepo(repository);
  };

  /**
   * Close detail modal
   */
  const closeDetailModal = () => {
    setDetailModalRepo(null);
  };

  /**
   * Handle chart data point click for drill-down
   * @param {Object} data - Chart data point
   */
  const handleChartClick = (data) => {
    if (data?.fullData) {
      setDetailModalRepo(data.fullData);
    }
  };

  /**
   * Get available languages for filter dropdown
   */
  const availableLanguages = useMemo(() => {
    if (!data?.repositories) return [];
    return extractLanguages(data.repositories);
  }, [data]);

  /**
   * Prepare chart data based on selected chart type and metric
   */
  const chartData = useMemo(() => {
    if (!processedRepositories || processedRepositories.length === 0) return [];

    switch (chartType) {
      case "bar":
        return transformForBarChart(processedRepositories, selectedMetric);
      case "line":
        return transformForLineGraph(processedRepositories, selectedMetric);
      case "scatter":
        return transformForScatterPlot(processedRepositories);
      default:
        return [];
    }
  }, [processedRepositories, chartType, selectedMetric]);

  /**
   * Get human-readable metric label
   */
  const metricLabel = useMemo(() => {
    return getMetricLabel(selectedMetric);
  }, [selectedMetric]);

  /**
   * Navigate to next repository in detail view
   */
  const handleNextRepo = () => {
    if (!detailModalRepo || !processedRepositories) return;
    const currentIndex = processedRepositories.findIndex(
      (r) => r.name === detailModalRepo.name,
    );
    if (currentIndex < processedRepositories.length - 1) {
      setDetailModalRepo(processedRepositories[currentIndex + 1]);
    }
  };

  /**
   * Navigate to previous repository in detail view
   */
  const handlePreviousRepo = () => {
    if (!detailModalRepo || !processedRepositories) return;
    const currentIndex = processedRepositories.findIndex(
      (r) => r.name === detailModalRepo.name,
    );
    if (currentIndex > 0) {
      setDetailModalRepo(processedRepositories[currentIndex - 1]);
    }
  };

  return (
    <ViewportProvider>
      <div className="app">
        {/* Skip Links for Keyboard Navigation */}
        <SkipLink href="#main-content">Skip to main content</SkipLink>
        <SkipLink href="#navigation">Skip to navigation</SkipLink>

        {/* Header */}
        <header className="header" role="banner">
          <div className="container">
            {/* Offline Indicator */}
            <OfflineIndicator />

            <div
              className="flex items-center justify-between"
              style={{ height: "var(--header-height)" }}
            >
              <div className="flex items-center gap-md">
                <h1 style={{ marginBottom: 0 }}>GitHub Stats Spark</h1>
                {data?.profile && (
                  <div className="badge">{data.profile.username}</div>
                )}
              </div>

              {/* View Toggle Buttons */}
              <nav
                className="flex gap-sm"
                id="navigation"
                aria-label="Main navigation"
              >
                <button
                  className={`btn ${currentView === "table" ? "btn-primary" : ""}`}
                  onClick={() => setCurrentView("table")}
                  aria-pressed={currentView === "table"}
                  aria-label="Switch to table view"
                >
                  Table View
                </button>
                <button
                  className={`btn ${currentView === "visualizations" ? "btn-primary" : ""}`}
                  onClick={() => setCurrentView("visualizations")}
                  aria-pressed={currentView === "visualizations"}
                  aria-label="Switch to visualizations view"
                >
                  Visualizations
                </button>
                <button
                  className={`btn ${currentView === "comparison" ? "btn-primary" : ""}`}
                  onClick={() => setCurrentView("comparison")}
                  aria-pressed={currentView === "comparison"}
                  aria-label={`Switch to comparison view (${selectedRepos.length} repositories selected)`}
                  disabled={selectedRepos.length < 2}
                >
                  Comparison ({selectedRepos.length})
                </button>
              </nav>
            </div>
          </div>
        </header>

        {/* Main Content */}
        <main
          className="main"
          id="main-content"
          role="main"
          aria-label="Main content"
        >
          <div className="container">
            <div className="mt-xl mb-xl">
              {/* Loading State */}
              {loading && (
                <LoadingState
                  message="Loading repository data..."
                  size="large"
                />
              )}

              {/* Error State */}
              {error && !loading && (
                <div
                  className="card"
                  style={{
                    backgroundColor: "var(--color-error)",
                    color: "white",
                  }}
                >
                  <h3>Error Loading Data</h3>
                  <p>{error.message || "Failed to load repository data"}</p>
                  <p className="text-sm">
                    {navigator.onLine
                      ? "Please check your network connection and try again."
                      : "You are offline. Cached data may be available when you reconnect."}
                  </p>
                  <button
                    className="btn btn-primary mt-md"
                    onClick={() => window.location.reload()}
                  >
                    Retry
                  </button>
                </div>
              )}

              {/* Data Loaded - Render Current View */}
              {!loading && !error && data && (
                <>
                  {currentView === "table" && (
                    <section aria-labelledby="repository-overview-heading">
                      <div className="mb-lg">
                        <h2 id="repository-overview-heading">
                          Repository Overview
                        </h2>
                        <p
                          className="text-muted"
                          role="status"
                          aria-live="polite"
                        >
                          Showing {processedRepositories.length} of{" "}
                          {data.repositories?.length || 0} repositories
                        </p>
                      </div>

                      {/* Filter Controls */}
                      {availableLanguages.length > 0 && (
                        <FilterControls
                          languages={availableLanguages}
                          selectedLanguage={filterLanguage}
                          onFilterChange={handleFilterChange}
                          onClearFilter={clearFilter}
                        />
                      )}

                      {/* Repository Table */}
                      {processedRepositories.length === 0 ? (
                        <EmptyState
                          icon="🔍"
                          title="No repositories found"
                          description={
                            filterLanguage
                              ? `No repositories match the selected language filter: ${filterLanguage}`
                              : "No repositories available"
                          }
                          actionLabel={filterLanguage ? "Clear filters" : ""}
                          onAction={filterLanguage ? clearFilter : null}
                        />
                      ) : (
                        <RepositoryTable
                          repositories={processedRepositories}
                          onSort={handleSort}
                          onSelectRepo={handleRepoSelect}
                          onRowClick={handleRepoClick}
                          selectedRepos={selectedRepos}
                          sortField={sortKey}
                          sortDirection={sortOrder}
                        />
                      )}
                    </section>
                  )}

                  {currentView === "visualizations" && (
                    <section
                      className="view-transition"
                      aria-labelledby="visualizations-heading"
                    >
                      <div className="mb-lg">
                        <h2 id="visualizations-heading">Data Visualizations</h2>
                        <p
                          className="text-muted"
                          role="status"
                          aria-live="polite"
                        >
                          Showing {processedRepositories.length} repositories
                          {filterLanguage && ` filtered by ${filterLanguage}`}
                        </p>
                      </div>

                      {/* Filter Controls - synchronize with table view */}
                      {availableLanguages.length > 0 && (
                        <FilterControls
                          languages={availableLanguages}
                          selectedLanguage={filterLanguage}
                          onFilterChange={handleFilterChange}
                          onClearFilter={clearFilter}
                        />
                      )}

                      {/* Visualization Controls */}
                      <VisualizationControls
                        chartType={chartType}
                        onChartTypeChange={setChartType}
                        selectedMetric={selectedMetric}
                        onMetricChange={setSelectedMetric}
                      />

                      {/* Chart Rendering */}
                      <div className="chart-wrapper">
                        <Suspense
                          fallback={<LoadingState message="Loading chart..." />}
                        >
                          {chartType === "bar" && (
                            <BarChart
                              data={chartData}
                              metricLabel={metricLabel}
                              onBarClick={handleChartClick}
                            />
                          )}

                          {chartType === "line" && (
                            <LineGraph
                              data={chartData}
                              metricLabel={metricLabel}
                              onPointClick={handleChartClick}
                            />
                          )}

                          {chartType === "scatter" && (
                            <ScatterPlot
                              data={chartData}
                              xAxisLabel="Total Commits"
                              yAxisLabel="Average Commit Size"
                              onPointClick={handleChartClick}
                            />
                          )}
                        </Suspense>
                      </div>
                    </section>
                  )}

                  {currentView === "comparison" && (
                    <section aria-labelledby="comparison-heading">
                      <div className="mb-lg">
                        <h2 id="comparison-heading">Repository Comparison</h2>
                        <p
                          className="text-muted"
                          role="status"
                          aria-live="polite"
                        >
                          {selectedRepos.length > 0
                            ? `Comparing ${selectedRepos.length} ${selectedRepos.length === 1 ? "repository" : "repositories"}`
                            : "Select repositories to compare"}
                        </p>
                      </div>

                      {/* Mobile vs Desktop Comparison Views */}
                      {selectedRepos.length === 0 ? (
                        <EmptyState
                          icon="📊"
                          title="No repositories selected"
                          description="Select 2-5 repositories from the dashboard to start comparing"
                          actionLabel="Browse repositories"
                          onAction={() => setCurrentView("table")}
                        />
                      ) : (
                        <Suspense
                          fallback={
                            <LoadingState message="Loading comparison..." />
                          }
                        >
                          {isMobile ? (
                            /* Mobile: Vertical stacked layout with swipe navigation */
                            <MobileComparisonView
                              repositories={selectedRepositoryObjects}
                              onRemoveRepo={handleRemoveRepo}
                            />
                          ) : (
                            /* Desktop: Side-by-side table comparison */
                            <>
                              <ComparisonSelector
                                selectedRepos={selectedRepos}
                                onClearSelection={handleClearSelection}
                                maxSelections={5}
                              />
                              <div className="mt-lg">
                                <ComparisonView
                                  repositories={selectedRepositoryObjects}
                                  onRemoveRepo={handleRemoveRepo}
                                />
                              </div>
                            </>
                          )}
                        </Suspense>
                      )}
                    </section>
                  )}
                </>
              )}
            </div>
          </div>
        </main>

        {/* Mobile TabBar Navigation */}
        <TabBar
          activeTab={currentView}
          onTabChange={setCurrentView}
          comparisonCount={selectedRepos.length}
        />

        {/* Footer */}
        <footer
          className="footer"
          style={{
            borderTop: "1px solid var(--color-border)",
            padding: "var(--spacing-lg) 0",
          }}
        >
          <div className="container">
            <div className="flex justify-between items-center">
              <p className="text-sm text-muted">
                Generated with{" "}
                <a
                  href="https://github.com/markhazleton/github-stats-spark"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  GitHub Stats Spark
                </a>
              </p>
              {data?.metadata && (
                <p className="text-xs text-muted">
                  Last updated:{" "}
                  {new Date(data.metadata.generated_at).toLocaleDateString()}
                  {" • "}
                  Schema v{data.metadata.schema_version}
                </p>
              )}
            </div>
          </div>
        </footer>

        {/* Floating Compare Button (mobile only) */}
        {isMobile && currentView === "table" && (
          <CompareButton
            count={selectedRepos.length}
            onClick={() => setCurrentView("comparison")}
            maxSelections={5}
          />
        )}

        {/* Detail Modal (for drill-down) */}
        {detailModalRepo && (
          <Suspense fallback={<LoadingState message="Loading details..." />}>
            <RepositoryDetail
              repository={detailModalRepo}
              onClose={closeDetailModal}
              onNext={handleNextRepo}
              onPrevious={handlePreviousRepo}
            />
          </Suspense>
        )}

        {/* Toast Notifications */}
        <ToastContainer toasts={toasts} onRemove={removeToast} />
      </div>
    </ViewportProvider>
  );
}

export default App;
