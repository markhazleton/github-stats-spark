import React, { useState, useMemo, Suspense, lazy, useEffect } from "react";
import { ViewportProvider } from "@/contexts/ViewportContext";
import useRepositoryData from "@/hooks/useRepositoryData";
import RepositoryTable from "@/components/RepositoryTable/RepositoryTable";
import LoadingState from "@/components/Common/LoadingState";
import FilterControls from "@/components/Common/FilterControls";
import { useTableSort } from "@/hooks/useTableSort";
import {
  extractLanguages,
  setupBackgroundSync,
  clearCache,
} from "@/services/dataService";
import { deferExecution, getConnectionType } from "@/utils/performance";
import TabBar from "@/components/Mobile/TabBar/TabBar";
import EmptyState from "@/components/Mobile/EmptyState/EmptyState";
import { ToastContainer } from "@/components/Mobile/Toast/Toast";

const DashboardView = lazy(
  () => import("@/components/Visualizations/DashboardView"),
);
const RepositoryDetail = lazy(
  () => import("@/components/DrillDown/RepositoryDetail"),
);

/**
 * GitHub Stats Spark Dashboard - Root App Component
 *
 * This is the main application component that orchestrates the dashboard layout,
 * state management, and routing between 2 views: Dashboard (table) and Visualizations (charts).
 *
 * Features:
 * - Data fetching via useRepositoryData custom hook
 * - View state management: Dashboard (table) and Visualizations
 * - URL hash routing for navigation
 * - Modal state for repository drill-down details
 * - Loading and error state handling
 *
 * @component
 */
function App() {
  // Data fetching with custom hook
  const { data, loading, error, refetch } = useRepositoryData();

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
        // Preload visualization components for faster navigation
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

  // View state management - initialize from URL hash or default to table
  const getInitialView = () => {
    const hash = window.location.hash.slice(1); // Remove the # character
    if (hash === "visualizations") return "visualizations";
    return "table"; // Default to table/dashboard view
  };

  const [currentView, setCurrentView] = useState(getInitialView());
  const [detailModalRepo, setDetailModalRepo] = useState(null); // For drill-down

  // Sync view with URL hash
  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash.slice(1);
      if (hash === "visualizations") {
        setCurrentView("visualizations");
      } else if (hash === "table" || hash === "dashboard" || hash === "") {
        setCurrentView("table");
      }
      // Ignore other hashes like #main-content (skip links)
    };

    window.addEventListener("hashchange", handleHashChange);
    return () => window.removeEventListener("hashchange", handleHashChange);
  }, []);

  // Update URL hash when view changes
  const handleViewChange = (view) => {
    setCurrentView(view);
    window.location.hash = view === "visualizations" ? "visualizations" : "";
  };

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
   * Get available languages for filter dropdown
   */
  const availableLanguages = useMemo(() => {
    if (!data?.repositories) return [];
    return extractLanguages(data.repositories);
  }, [data]);

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

  const formatGeneratedAt = (timestamp) => {
    if (!timestamp) return "Unknown";
    const parsed = new Date(timestamp);
    if (Number.isNaN(parsed.getTime())) return "Unknown";
    return parsed.toLocaleString();
  };

  const handleForceRefresh = async () => {
    try {
      await clearCache();
      await refetch({ forceRefresh: true, cacheBust: true });
      addToast("Data refreshed and cache cleared", "success", 3000);
    } catch {
      addToast("Refresh failed. Check the console for details.", "error", 4000);
    }
  };

  return (
    <ViewportProvider>
      <div className="app">
        {/* Header */}
        <header className="header" role="banner">
          <div className="container">
            <div
              className="flex items-center justify-between"
              style={{ height: "var(--header-height)" }}
            >
              <h1 style={{ marginBottom: 0 }}>
                <span className="header-title-line1">GitHub</span>
                <span className="header-title-line2">StatsSpark</span>
              </h1>

              {/* Navigation Menu */}
              <nav
                className="nav-menu"
                id="navigation"
                aria-label="Main navigation"
              >
                <button
                  className={`nav-menu-item ${currentView === "table" ? "nav-menu-item--active" : ""}`}
                  onClick={() => handleViewChange("table")}
                  aria-current={currentView === "table" ? "page" : undefined}
                  aria-label="Switch to dashboard view"
                >
                  Dashboard
                </button>
                <button
                  className={`nav-menu-item ${currentView === "visualizations" ? "nav-menu-item--active" : ""}`}
                  onClick={() => handleViewChange("visualizations")}
                  aria-current={
                    currentView === "visualizations" ? "page" : undefined
                  }
                  aria-label="Switch to visualizations view"
                >
                  Visualizations
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
                          {data?.profile?.username || "User"} Repositories
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
                          onRowClick={handleRepoClick}
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
                        <h2 id="visualizations-heading">Repository Insights</h2>
                        <p
                          className="text-muted"
                          role="status"
                          aria-live="polite"
                        >
                          Showing {processedRepositories.length} repositories
                          {filterLanguage && ` filtered by ${filterLanguage}`}
                        </p>
                      </div>

                      {availableLanguages.length > 0 && (
                        <FilterControls
                          languages={availableLanguages}
                          selectedLanguage={filterLanguage}
                          onFilterChange={handleFilterChange}
                          onClearFilter={clearFilter}
                        />
                      )}

                      <Suspense
                        fallback={
                          <LoadingState message="Loading visualizations..." />
                        }
                      >
                        <DashboardView
                          repositories={processedRepositories}
                          profile={data?.profile}
                          onRepoClick={handleRepoClick}
                        />
                      </Suspense>
                    </section>
                  )}
                </>
              )}
            </div>
          </div>
        </main>

        {/* Mobile TabBar Navigation */}
        <TabBar activeTab={currentView} onTabChange={handleViewChange} />

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
              <div className="flex items-center gap-md">
                {data?.metadata && (
                  <p className="text-xs text-muted">
                    repositories.json:{" "}
                    {formatGeneratedAt(data.metadata.generated_at)} {" | "}
                    Schema v{data.metadata.schema_version}
                  </p>
                )}
                <button
                  className="btn btn-secondary"
                  onClick={handleForceRefresh}
                  disabled={loading}
                  aria-label="Force refresh repositories data"
                >
                  {loading ? "Refreshing..." : "Force Refresh"}
                </button>
              </div>
            </div>
          </div>
        </footer>

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
