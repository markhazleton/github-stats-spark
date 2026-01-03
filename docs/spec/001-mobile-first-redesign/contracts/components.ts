/**
 * Component API Contracts
 * Mobile-First Front-End Redesign
 */

import * as React from 'react';
import {
  TabItem,
  TabPosition,
  Repository,
  RepositoryCardVariant,
  SortConfig,
  GestureType,
  GestureEvent,
  TouchTargetConfig,
  LoadingType,
  LoadingVariant,
  EmptyStateAction,
  BottomSheetSnapPoint,
  SafeAreaInsets,
  ChartConfig,
} from './types';

// ============================================================================
// Layout Components
// ============================================================================

export interface ContainerProps {
  children: React.ReactNode;
  className?: string;
  maxWidth?: 'sm' | 'md' | 'lg' | 'xl' | 'full';
  padding?: boolean;
  centered?: boolean;
}

export interface StackProps {
  children: React.ReactNode;
  direction?: 'vertical' | 'horizontal';
  spacing?: number;
  align?: 'start' | 'center' | 'end' | 'stretch';
  justify?: 'start' | 'center' | 'end' | 'between' | 'around';
  wrap?: boolean;
  className?: string;
}

export interface SafeAreaProps {
  children: React.ReactNode;
  edges?: Array<'top' | 'right' | 'bottom' | 'left'>;
  insets?: SafeAreaInsets;
}

// ============================================================================
// Navigation Components
// ============================================================================

export interface TabBarProps {
  tabs: TabItem[];
  activeTab: string;
  onTabChange: (tabId: string) => void;
  position?: TabPosition;
  sticky?: boolean;
  className?: string;
}

export interface TabBarItemProps {
  tab: TabItem;
  active: boolean;
  onClick: () => void;
}

// ============================================================================
// Mobile Components
// ============================================================================

export interface BottomSheetProps {
  isOpen: boolean;
  onDismiss: () => void;
  snapPoints?: BottomSheetSnapPoint[];
  children: React.ReactNode;
  dismissible?: boolean;
  backdrop?: boolean;
  closeOnBackdropClick?: boolean;
  header?: React.ReactNode;
  footer?: React.ReactNode;
  className?: string;
  ariaLabel?: string;
}

export interface RepositoryCardProps {
  repository: Repository;
  variant?: RepositoryCardVariant;
  selectable?: boolean;
  selected?: boolean;
  onSelect?: (id: string) => void;
  onExpand?: (id: string) => void;
  className?: string;
}

export interface TouchTargetProps {
  children: React.ReactNode;
  onClick?: (event: React.MouseEvent | React.TouchEvent) => void;
  onLongPress?: (event: React.TouchEvent) => void;
  config?: Partial<TouchTargetConfig>;
  disabled?: boolean;
  ariaLabel: string;
  className?: string;
}

export interface GestureHandlerProps {
  children: React.ReactNode;
  gestures: GestureType[];
  onGesture: (event: GestureEvent) => void;
  threshold?: number;
  enabled?: boolean;
  className?: string;
}

export interface EmptyStateProps {
  icon: React.ComponentType<{ size?: number; color?: string }>;
  title: string;
  description?: string;
  action?: EmptyStateAction;
  className?: string;
}

// ============================================================================
// Repository Components
// ============================================================================

export interface RepositoryListProps {
  repositories: Repository[];
  loading?: boolean;
  selectable?: boolean;
  selectedIds?: string[];
  onSelect?: (ids: string[]) => void;
  onRepositoryClick?: (repository: Repository) => void;
  sortConfig?: SortConfig;
  onSortChange?: (config: SortConfig) => void;
  className?: string;
}

export interface RepositoryCardHeaderProps {
  name: string;
  language: string;
  stars: number;
  selectable: boolean;
  selected: boolean;
  onSelect?: () => void;
}

export interface RepositoryCardBodyProps {
  description: string | null;
  technologies: string[];
  commits: number;
  contributors: number;
  forks: number;
  lastCommitDate: string;
}

export interface LanguageBadgeProps {
  language: string;
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

export interface TechnologyStackProps {
  technologies: string[];
  maxVisible?: number;
  size?: 'sm' | 'md';
  className?: string;
}

// ============================================================================
// Comparison Components
// ============================================================================

export interface ComparisonViewProps {
  repositories: Repository[];
  onRemove?: (id: string) => void;
  onClear?: () => void;
  className?: string;
}

export interface ComparisonCardProps {
  repository: Repository;
  onRemove?: () => void;
  swipeable?: boolean;
}

export interface ComparisonMetricsProps {
  repositories: Repository[];
  metric: 'stars' | 'commits' | 'contributors' | 'forks';
  className?: string;
}

// ============================================================================
// Loading Components
// ============================================================================

export interface LoadingStateProps {
  type: LoadingType;
  variant?: LoadingVariant;
  count?: number;
  duration?: number;
  className?: string;
}

export interface SkeletonProps {
  width?: string | number;
  height?: string | number;
  variant?: 'text' | 'rectangular' | 'circular';
  animation?: boolean;
  className?: string;
}

export interface SpinnerProps {
  size?: 'sm' | 'md' | 'lg';
  color?: string;
  className?: string;
  ariaLabel?: string;
}

// ============================================================================
// Feedback Components
// ============================================================================

export interface ToastProps {
  message: string;
  variant?: 'success' | 'error' | 'warning' | 'info';
  duration?: number;
  onClose?: () => void;
  position?: 'top' | 'bottom';
  icon?: React.ComponentType<{ size?: number }>;
}

export interface ErrorBoundaryProps {
  children: React.ReactNode;
  fallback?: React.ComponentType<ErrorBoundaryFallbackProps>;
  onError?: (error: Error, errorInfo: React.ErrorInfo) => void;
}

export interface ErrorBoundaryFallbackProps {
  error: Error;
  resetError: () => void;
}

export interface RetryButtonProps {
  onRetry: () => void;
  loading?: boolean;
  disabled?: boolean;
  label?: string;
  className?: string;
}

// ============================================================================
// Filter & Sort Components
// ============================================================================

export interface FilterSheetProps {
  isOpen: boolean;
  onClose: () => void;
  filters: FilterConfig;
  onFilterChange: (filters: FilterConfig) => void;
  onReset: () => void;
}

export interface FilterConfig {
  language?: string[];
  minStars?: number;
  maxStars?: number;
  hasDescription?: boolean;
  technologies?: string[];
}

export interface SortSheetProps {
  isOpen: boolean;
  onClose: () => void;
  sortConfig: SortConfig;
  onSortChange: (config: SortConfig) => void;
}

export interface SortOptionProps {
  field: SortConfig['field'];
  direction: SortConfig['direction'];
  label: string;
  active: boolean;
  onClick: () => void;
}

// ============================================================================
// Visualization Components
// ============================================================================

export interface MobileChartProps {
  data: any[];
  config: ChartConfig;
  title?: string;
  onDataPointClick?: (dataPoint: any) => void;
  className?: string;
}

export interface ChartTooltipProps {
  active?: boolean;
  payload?: any[];
  label?: string;
  position?: { x: number; y: number };
}

export interface ChartLegendProps {
  items: Array<{ label: string; color: string; value?: number }>;
  position?: 'top' | 'bottom' | 'left' | 'right';
  onClick?: (item: string) => void;
}

// ============================================================================
// Common Components
// ============================================================================

export interface ButtonProps {
  children: React.ReactNode;
  onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void;
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  fullWidth?: boolean;
  icon?: React.ComponentType<{ size?: number }>;
  iconPosition?: 'left' | 'right';
  ariaLabel?: string;
  className?: string;
  type?: 'button' | 'submit' | 'reset';
}

export interface IconButtonProps {
  icon: React.ComponentType<{ size?: number; color?: string }>;
  onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void;
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  ariaLabel: string;
  className?: string;
}

export interface CheckboxProps {
  checked: boolean;
  onChange: (checked: boolean) => void;
  label?: string;
  disabled?: boolean;
  indeterminate?: boolean;
  ariaLabel?: string;
  className?: string;
}

export interface SearchInputProps {
  value: string;
  onChange: (value: string) => void;
  onClear?: () => void;
  placeholder?: string;
  disabled?: boolean;
  autoFocus?: boolean;
  ariaLabel?: string;
  className?: string;
}

// ============================================================================
// Pull-to-Refresh
// ============================================================================

export interface PullToRefreshProps {
  children: React.ReactNode;
  onRefresh: () => Promise<void>;
  threshold?: number;
  refreshing?: boolean;
  disabled?: boolean;
  className?: string;
}

export interface PullToRefreshIndicatorProps {
  progress: number; // 0-1
  refreshing: boolean;
  threshold: number;
}

// ============================================================================
// Accessibility Components
// ============================================================================

export interface SkipLinkProps {
  targetId: string;
  label: string;
}

export interface ScreenReaderOnlyProps {
  children: React.ReactNode;
  as?: React.ElementType;
}

export interface FocusTrapProps {
  children: React.ReactNode;
  active: boolean;
  onEscape?: () => void;
}
