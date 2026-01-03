# Mobile-First Redesign Quickstart Guide

**Feature**: `001-mobile-first-redesign` | **Date**: 2026-01-03

## Overview

This guide provides a quick reference for developers implementing the mobile-first redesign. It covers the essential patterns, components, and best practices to get started quickly.

---

## 🚀 Quick Setup

### 1. Install Dependencies

```bash
cd frontend
npm install

# New mobile-first dependencies (see research.md for details)
npm install @use-gesture/react@^10.3.1
npm install dexie@^4.0.0
npm install chart.js@^4.0.0 react-chartjs-2@^5.0.0
npm install react-modal-sheet@^5.2.1
npm install workbox-window@^7.0.0
```

### 2. Install Dev Dependencies

```bash
npm install --save-dev @lighthouse/cli@^11.0.0
npm install --save-dev vite-plugin-pwa@^0.19.0
```

### 3. Update Vite Config

Add PWA plugin to `frontend/vite.config.js`:

```javascript
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      workbox: {
        globPatterns: ['**/*.{js,css,html,svg,png,json}']
      }
    })
  ]
});
```

---

## 📱 Core Patterns

### Mobile-First CSS

**Always start with mobile styles, enhance for desktop:**

```css
/* ❌ Don't: Desktop-first */
.container {
  width: 1200px;
}

@media (max-width: 768px) {
  .container {
    width: 100%;
  }
}

/* ✅ Do: Mobile-first */
.container {
  width: 100%;
  padding: 1rem;
}

@media (min-width: 768px) {
  .container {
    max-width: 1200px;
    padding: 2rem;
  }
}
```

### Touch Targets

**Ensure all interactive elements are at least 44x44px:**

```jsx
import { TouchTarget } from '@components/Mobile/TouchTarget';

// ❌ Don't: Small touch target
<button className="icon-btn" onClick={handleClick}>
  <Icon size={16} />
</button>

// ✅ Do: Proper touch target
<TouchTarget
  onClick={handleClick}
  ariaLabel="Delete repository"
  config={{ minWidth: 44, minHeight: 44 }}
>
  <Icon size={20} />
</TouchTarget>
```

### Viewport Breakpoints

```javascript
import { useBreakpoint } from '@hooks/useBreakpoint';

function MyComponent() {
  const { current, isMobile } = useBreakpoint();

  return (
    <div>
      {isMobile ? <MobileView /> : <DesktopView />}
    </div>
  );
}
```

**Breakpoint values:**
- `xs`: 0-319px
- `sm`: 320-767px (mobile)
- `md`: 768-1023px (tablet)
- `lg`: 1024-1279px (desktop)
- `xl`: 1280px+ (large desktop)

---

## 🎨 Component Quick Reference

### Bottom Sheet

```jsx
import { useBottomSheet } from '@hooks/useBottomSheet';
import { BottomSheet } from '@components/Mobile/BottomSheet';

function FilterButton() {
  const { isOpen, open, close, sheetRef } = useBottomSheet({
    snapPoints: [0.5, 0.9],
    dismissible: true
  });

  return (
    <>
      <button onClick={() => open()}>Open Filters</button>

      <BottomSheet
        isOpen={isOpen}
        onDismiss={close}
        snapPoints={[0.5, 0.9]}
      >
        <FilterForm onApply={close} />
      </BottomSheet>
    </>
  );
}
```

### Repository Card

```jsx
import { RepositoryCard } from '@components/Mobile/RepositoryCard';

function RepositoryList({ repositories }) {
  const [expandedId, setExpandedId] = useState(null);

  return (
    <div className="repository-list">
      {repositories.map(repo => (
        <RepositoryCard
          key={repo.id}
          repository={repo}
          variant={expandedId === repo.id ? 'expanded' : 'collapsed'}
          onExpand={setExpandedId}
        />
      ))}
    </div>
  );
}
```

### Tab Bar Navigation

```jsx
import { TabBar } from '@components/Mobile/TabBar';
import { DashboardIcon, CompareIcon, ChartIcon } from '@components/Common/Icons';

const tabs = [
  {
    id: 'dashboard',
    label: 'Dashboard',
    icon: DashboardIcon,
    route: '/',
    ariaLabel: 'Navigate to Dashboard'
  },
  {
    id: 'compare',
    label: 'Compare',
    icon: CompareIcon,
    route: '/compare',
    ariaLabel: 'Navigate to Compare'
  },
  {
    id: 'charts',
    label: 'Charts',
    icon: ChartIcon,
    route: '/visualizations',
    ariaLabel: 'Navigate to Visualizations'
  }
];

function Layout() {
  const [activeTab, setActiveTab] = useState('dashboard');

  return (
    <>
      <main>{/* Content */}</main>
      <TabBar
        tabs={tabs}
        activeTab={activeTab}
        onTabChange={setActiveTab}
        position="bottom"
        sticky
      />
    </>
  );
}
```

### Empty State

```jsx
import { EmptyState } from '@components/Mobile/EmptyState';
import { EmptySearchIcon } from '@components/Common/Icons';

function SearchResults({ results, onClearFilters }) {
  if (results.length === 0) {
    return (
      <EmptyState
        icon={EmptySearchIcon}
        title="No repositories found"
        description="Try adjusting your filters or search criteria"
        action={{
          label: 'Clear filters',
          onClick: onClearFilters,
          variant: 'primary'
        }}
      />
    );
  }

  return <RepositoryList repositories={results} />;
}
```

---

## 🎯 Custom Hooks Usage

### useGesture (Swipe)

```jsx
import { useGesture } from '@hooks/useGesture';

function SwipeableCard({ onDelete }) {
  const { bind } = useGesture({
    onSwipeLeft: (e) => {
      onDelete(e.target.dataset.id);
    }
  }, { threshold: 50 });

  return (
    <div {...bind()} data-id="repo-123" className="card">
      Swipe left to delete
    </div>
  );
}
```

### useOfflineCache

```jsx
import { useOfflineCache } from '@hooks/useOfflineCache';

function RepositoryList() {
  const { data, isLoading, isStale, set } = useOfflineCache({
    key: 'repositories-list',
    maxAge: 7 * 24 * 60 * 60 * 1000 // 7 days
  });

  useEffect(() => {
    async function loadData() {
      const repos = await fetchRepositories();
      await set(repos);
    }

    if (!data || isStale) {
      loadData();
    }
  }, []);

  if (isLoading) return <LoadingState type="card" count={5} />;

  return <div>{/* Render data */}</div>;
}
```

### useNetworkStatus

```jsx
import { useNetworkStatus } from '@hooks/useNetworkStatus';

function App() {
  const { isOnline, effectiveType, saveData } = useNetworkStatus();

  // Adapt quality based on connection
  const imageQuality = effectiveType === '4g' ? 'high' : 'low';
  const enableAutoplay = !saveData && effectiveType === '4g';

  return (
    <div>
      {!isOnline && <OfflineBanner />}
      {/* Rest of app */}
    </div>
  );
}
```

### usePullToRefresh

```jsx
import { usePullToRefresh } from '@hooks/usePullToRefresh';

function Dashboard() {
  const { bind, isRefreshing } = usePullToRefresh({
    threshold: 80,
    onRefresh: async () => {
      await fetchLatestData();
    }
  });

  return (
    <div {...bind()} className="dashboard">
      {isRefreshing && <RefreshSpinner />}
      <DashboardContent />
    </div>
  );
}
```

---

## 🎭 Service Layer Usage

### Offline Storage Service

```javascript
import { offlineStorage } from '@services/offlineStorage';

// Initialize on app load
await offlineStorage.init();

// Store data
await offlineStorage.set('repositories', repositoryData);

// Retrieve data
const cachedRepos = await offlineStorage.get('repositories');

// Cleanup old data
await offlineStorage.cleanup();
```

### Data Service

```javascript
import { dataService } from '@services/dataService';

// Load repositories
const repos = await dataService.getRepositories({ cache: true });

// Search
const results = await dataService.searchRepositories('react');

// Filter
const filtered = await dataService.filterRepositories({
  language: ['JavaScript', 'TypeScript'],
  minStars: 100
});

// Sort
const sorted = dataService.sortRepositories(repos, 'stars', 'desc');
```

### Haptic Feedback Service

```javascript
import { haptic } from '@services/haptic';

function DeleteButton({ onDelete }) {
  const handleDelete = () => {
    if (haptic.isSupported()) {
      haptic.medium(); // Tactile feedback
    }
    onDelete();
  };

  return <button onClick={handleDelete}>Delete</button>;
}
```

---

## 📐 Layout Examples

### Mobile-First Container

```jsx
import { Container } from '@components/Layout/Container';

function Page() {
  return (
    <Container maxWidth="lg" padding centered>
      <h1>Page Title</h1>
      <p>Content goes here</p>
    </Container>
  );
}
```

### Stack Layout

```jsx
import { Stack } from '@components/Layout/Stack';

function Form() {
  return (
    <Stack direction="vertical" spacing={16}>
      <input type="text" placeholder="Name" />
      <input type="email" placeholder="Email" />
      <button>Submit</button>
    </Stack>
  );
}
```

### Safe Area Insets

```jsx
import { SafeArea } from '@components/Layout/SafeArea';

function MobileNav() {
  return (
    <SafeArea edges={['bottom']}>
      <nav className="bottom-nav">
        {/* Navigation items */}
      </nav>
    </SafeArea>
  );
}
```

---

## 🎨 Styling Best Practices

### Use CSS Custom Properties

```css
/* Define in :root */
:root {
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;

  --touch-target-min: 44px;

  --safe-area-top: env(safe-area-inset-top);
  --safe-area-bottom: env(safe-area-inset-bottom);
}

/* Use in components */
.card {
  padding: var(--spacing-md);
  margin-bottom: var(--spacing-sm);
}

.button {
  min-width: var(--touch-target-min);
  min-height: var(--touch-target-min);
}
```

### Container Queries (Progressive Enhancement)

```css
/* Modern browsers with container query support */
@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}

/* Fallback for older browsers */
@supports not (container-type: inline-size) {
  @media (min-width: 400px) {
    .card {
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
  }
}
```

### Reduced Motion

```css
/* Default: animations enabled */
.card {
  transition: transform 0.3s ease;
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .card {
    transition: none;
  }
}
```

---

## 🧪 Testing Examples

### Component Test (Vitest)

```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { RepositoryCard } from '@components/Mobile/RepositoryCard';

describe('RepositoryCard', () => {
  it('renders collapsed state by default', () => {
    const repo = {
      id: '1',
      name: 'test-repo',
      language: 'JavaScript',
      stars: 100,
      lastCommitDate: '2026-01-01'
    };

    render(<RepositoryCard repository={repo} variant="collapsed" />);

    expect(screen.getByText('test-repo')).toBeInTheDocument();
    expect(screen.getByText('JavaScript')).toBeInTheDocument();
    expect(screen.queryByText('Description')).not.toBeInTheDocument();
  });

  it('expands on click', () => {
    const onExpand = vi.fn();
    const repo = { id: '1', name: 'test-repo', /* ... */ };

    render(
      <RepositoryCard
        repository={repo}
        variant="collapsed"
        onExpand={onExpand}
      />
    );

    fireEvent.click(screen.getByRole('article'));
    expect(onExpand).toHaveBeenCalledWith('1');
  });
});
```

### Hook Test

```jsx
import { renderHook, act } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { useToggle } from '@hooks/useToggle';

describe('useToggle', () => {
  it('toggles boolean value', () => {
    const { result } = renderHook(() => useToggle(false));

    expect(result.current.value).toBe(false);

    act(() => {
      result.current.toggle();
    });

    expect(result.current.value).toBe(true);
  });
});
```

---

## 🚦 Performance Checklist

### Before Committing

- [ ] Run Lighthouse audit: `npm run lighthouse`
- [ ] Bundle size check: `npm run build && npm run size`
- [ ] Test on real devices (iOS Safari, Android Chrome)
- [ ] Verify touch targets (min 44x44px)
- [ ] Test offline functionality
- [ ] Check console for errors/warnings
- [ ] Verify reduced motion support
- [ ] Test with screen reader

### Performance Budgets

| Metric | Target | Limit | Command |
|--------|--------|-------|---------|
| JS Bundle | 150KB | 170KB | `npm run build` |
| CSS Bundle | 40KB | 50KB | `npm run build` |
| FCP | 1.5s | 2s | `npm run lighthouse` |
| TTI | 4s | 5s | `npm run lighthouse` |
| CLS | 0.05 | 0.1 | `npm run lighthouse` |

---

## 📚 Further Reading

- [Full Specification](./spec.md) - Complete requirements and user stories
- [Implementation Plan](./plan.md) - Technical architecture and structure
- [Research](./research.md) - Technology decisions and rationale
- [Data Model](./data-model.md) - Entity definitions and state management
- [API Contracts](./contracts/) - Component and hook interfaces

---

## 🆘 Common Issues

### Issue: Bottom sheet doesn't dismiss on backdrop click

**Solution**: Ensure `closeOnBackdropClick={true}` prop is set:

```jsx
<BottomSheet
  isOpen={isOpen}
  onDismiss={close}
  closeOnBackdropClick={true}
>
  {/* Content */}
</BottomSheet>
```

### Issue: Pull-to-refresh conflicts with browser refresh

**Solution**: Use `overscroll-behavior-y: contain` on scroll container:

```css
.scroll-container {
  overscroll-behavior-y: contain;
}
```

### Issue: Touch targets too small on iOS

**Solution**: Ensure minimum 44x44px and use TouchTarget wrapper:

```jsx
<TouchTarget
  config={{ minWidth: 44, minHeight: 44 }}
  ariaLabel="Action"
>
  <IconButton icon={Icon} />
</TouchTarget>
```

### Issue: Offline cache not working

**Solution**: Verify IndexedDB initialization in App.jsx:

```jsx
useEffect(() => {
  offlineStorage.init().catch(console.error);
}, []);
```

---

## 🎯 Next Steps

1. Review the [Implementation Plan](./plan.md) for full architecture
2. Check [tasks.md](./tasks.md) for ordered implementation tasks
3. Start with Phase 1: Core mobile components (BottomSheet, TabBar, RepositoryCard)
4. Test on real mobile devices throughout development
5. Run Lighthouse CI before each commit to verify performance budgets

---

**Questions?** Refer to the full specification or reach out to the team.
