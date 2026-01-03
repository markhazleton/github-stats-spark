import { useState, useMemo } from 'react';

/**
 * Custom hook for table sorting and filtering
 * @param {Array} data - The data to sort and filter
 * @param {string} initialSortKey - Initial column to sort by
 * @param {string} initialSortOrder - Initial sort order ('asc' or 'desc')
 * @returns {Object} - Sorted/filtered data and control functions
 */
export function useTableSort(data, initialSortKey = 'name', initialSortOrder = 'asc') {
  const [sortKey, setSortKey] = useState(initialSortKey);
  const [sortOrder, setSortOrder] = useState(initialSortOrder);
  const [filterLanguage, setFilterLanguage] = useState('');

  /**
   * Handle column sort - toggle order if same column, otherwise set new column
   */
  const handleSort = (key) => {
    if (sortKey === key) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortKey(key);
      setSortOrder('asc');
    }
  };

  /**
   * Handle language filter change
   */
  const handleFilterChange = (language) => {
    setFilterLanguage(language);
  };

  /**
   * Clear all filters
   */
  const clearFilter = () => {
    setFilterLanguage('');
  };

  /**
   * Sort comparator function
   */
  const sortComparator = (a, b) => {
    let aVal = a[sortKey];
    let bVal = b[sortKey];

    // Handle commit_count from nested structure
    if (sortKey === 'commit_count') {
      aVal = a.commit_history?.total_commits || a.commit_count || 0;
      bVal = b.commit_history?.total_commits || b.commit_count || 0;
    }

    // Handle avg_commit_size from nested structure
    if (sortKey === 'avg_commit_size') {
      aVal = a.commit_metrics?.avg_size || a.avg_commit_size || 0;
      bVal = b.commit_metrics?.avg_size || b.avg_commit_size || 0;
    }

    // Handle nested commit objects (largest_commit, smallest_commit)
    if (sortKey === 'largest_commit' || sortKey === 'smallest_commit') {
      aVal = (a.commit_metrics?.[sortKey]?.size) || (a[sortKey]?.size) || 0;
      bVal = (b.commit_metrics?.[sortKey]?.size) || (b[sortKey]?.size) || 0;
    }

    // Handle null/undefined values
    if (aVal == null) return sortOrder === 'asc' ? 1 : -1;
    if (bVal == null) return sortOrder === 'asc' ? -1 : 1;

    // Handle numeric values (commits, sizes, stars, etc.)
    // Convert string numbers to actual numbers for numeric fields
    const numericFields = ['commit_count', 'stars', 'avg_commit_size', 'largest_commit', 'smallest_commit'];
    if (numericFields.includes(sortKey)) {
      aVal = parseFloat(aVal) || 0;
      bVal = parseFloat(bVal) || 0;
      return sortOrder === 'asc' ? aVal - bVal : bVal - aVal;
    }
    
    if (typeof aVal === 'number' && typeof bVal === 'number') {
      return sortOrder === 'asc' ? aVal - bVal : bVal - aVal;
    }

    // Handle date strings (ISO format)
    if (sortKey.includes('date') || sortKey.includes('Date')) {
      const dateA = new Date(aVal);
      const dateB = new Date(bVal);
      return sortOrder === 'asc' ? dateA - dateB : dateB - dateA;
    }

    // Handle string values (name, language)
    const strA = String(aVal).toLowerCase();
    const strB = String(bVal).toLowerCase();
    
    if (strA < strB) return sortOrder === 'asc' ? -1 : 1;
    if (strA > strB) return sortOrder === 'asc' ? 1 : -1;
    return 0;
  };

  /**
   * Apply sorting and filtering to data
   */
  const processedData = useMemo(() => {
    if (!data || !Array.isArray(data)) return [];

    // Apply language filter first
    let filtered = data;
    if (filterLanguage) {
      filtered = data.filter(repo => 
        repo.language?.toLowerCase() === filterLanguage.toLowerCase()
      );
    }

    // Apply sorting
    return [...filtered].sort(sortComparator);
  }, [data, sortKey, sortOrder, filterLanguage]);

  return {
    sortedData: processedData,
    sortKey,
    sortOrder,
    filterLanguage,
    handleSort,
    handleFilterChange,
    clearFilter,
  };
}
