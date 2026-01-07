import React, { useState } from "react";
import { useBreakpoint } from "@/hooks/useMediaQuery";
import { RepositoryCard } from "@/components/Mobile/RepositoryCard/RepositoryCard";
import { LoadingState } from "@/components/Mobile/LoadingState/LoadingState";
import FilterSheet from "./FilterSheet";
import SortSheet from "./SortSheet";
import TableHeader from "./TableHeader";
import TableRow from "./TableRow";
import ExportButton from "@/components/Common/ExportButton";
import styles from "./RepositoryTable.module.css";

/**
 * RepositoryTable Component
 *
 * Main table component that displays repository data with comprehensive metrics.
 * Supports sorting, filtering, and responsive layouts.
 *
 * @component
 * @param {Object} props - Component props
 * @param {Array} props.repositories - Array of repository objects to display
 * @param {Function} [props.onSort] - Callback when column header is clicked for sorting
 * @param {Function} [props.onFilter] - Callback when filter is applied
 * @param {Function} [props.onRowClick] - Callback when row is clicked for drill-down
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
  onRowClick,
  sortField = "stars",
  sortDirection = "desc",
  loading = false,
}) {
  const { isMobile } = useBreakpoint();

  // Bottom sheet state for mobile
  const [filterSheetOpen, setFilterSheetOpen] = useState(false);
  const [sortSheetOpen, setSortSheetOpen] = useState(false);
  const [filters, setFilters] = useState({
    language: null,
    minStars: null,
    dateRange: null,
  });

  /**
   * Get unique languages from repositories for filter options
   */
  const availableLanguages = React.useMemo(() => {
    const languages = repositories.map((repo) => repo.language).filter(Boolean);
    return [...new Set(languages)].sort();
  }, [repositories]);

  /**
   * Handle filter application
   */
  const handleApplyFilters = (newFilters) => {
    setFilters(newFilters);
    if (onFilter) {
      onFilter(newFilters);
    }
  };

  /**
   * Handle sort application
   */
  const handleApplySort = ({ field, direction }) => {
    if (onSort) {
      onSort(field, direction);
    }
  };

  /**
   * Handle column header click for sorting
   */
  const handleSort = (field) => {
    // Call parent callback if provided
    if (onSort) {
      onSort(field);
    }
  };

  // Show loading state
  if (loading) {
    return (
      <div className={styles.loadingWrapper}>
        <LoadingState type={isMobile ? "card" : "list"} count={5} />
      </div>
    );
  }

  // Show empty state if no repositories
  if (!repositories || repositories.length === 0) {
    return (
      <div className={styles.emptyState}>
        <p className="text-muted">No repositories to display</p>
      </div>
    );
  }

  // Mobile view: Card layout
  if (isMobile) {
    return (
      <>
        <div className={styles.mobileContainer}>
          {/* Mobile header with filter and sort buttons */}
          <div className={styles.mobileHeader}>
            <button
              onClick={() => setFilterSheetOpen(true)}
              className={styles.mobileHeaderButton}
              aria-label="Filter repositories"
            >
              <span className={styles.mobileHeaderIcon}>🔍</span>
              <span>Filter</span>
              {(filters.language || filters.minStars || filters.dateRange) && (
                <span
                  className={styles.filterBadge}
                  aria-label="Active filters"
                >
                  ●
                </span>
              )}
            </button>

            <button
              onClick={() => setSortSheetOpen(true)}
              className={styles.mobileHeaderButton}
              aria-label="Sort repositories"
            >
              <span className={styles.mobileHeaderIcon}>↕️</span>
              <span>Sort</span>
            </button>
          </div>

          <div className={styles.mobileCardGrid}>
            {repositories.map((repo) => (
              <RepositoryCard
                key={repo.name}
                repository={repo}
                onClick={onRowClick}
              />
            ))}
          </div>

          {/* Mobile Footer */}
          <div className={styles.mobileFooter}>
            <p className="text-sm text-muted">
              {repositories.length}{" "}
              {repositories.length === 1 ? "repository" : "repositories"}
            </p>
            <ExportButton
              data={repositories}
              filename="repositories"
              label="Export"
            />
          </div>
        </div>

        {/* Bottom sheets */}
        <FilterSheet
          isOpen={filterSheetOpen}
          onClose={() => setFilterSheetOpen(false)}
          filters={filters}
          onApplyFilters={handleApplyFilters}
          availableLanguages={availableLanguages}
        />

        <SortSheet
          isOpen={sortSheetOpen}
          onClose={() => setSortSheetOpen(false)}
          sortField={sortField}
          sortDirection={sortDirection}
          onApplySort={handleApplySort}
        />
      </>
    );
  }

  // Desktop view: Table layout
  return (
    <div className={styles.tableWrapper}>
      <div className={styles.tableContainer}>
        <table
          className={styles.table}
          role="table"
          aria-label="Repository comparison table"
        >
          <TableHeader
            onSort={handleSort}
            sortField={sortField}
            sortDirection={sortDirection}
          />
          <tbody>
            {repositories.map((repo) => (
              <TableRow
                key={repo.name}
                repository={repo}
                onClick={onRowClick}
              />
            ))}
          </tbody>
        </table>
      </div>

      {/* Table Footer with Summary and Export */}
      <div className={styles.tableFooter}>
        <p className="text-sm text-muted">
          Showing {repositories.length}{" "}
          {repositories.length === 1 ? "repository" : "repositories"}
        </p>
        <ExportButton
          data={repositories}
          filename="repositories"
          label="Export"
        />
      </div>
    </div>
  );
}
