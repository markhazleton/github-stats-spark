import "./TabBar.css";

/**
 * TabBar - Fixed bottom navigation for mobile devices
 *
 * Provides primary section navigation with 3 tabs:
 * - Dashboard: Repository browsing and filtering
 * - Compare: Repository comparison view
 * - Visualizations: Charts and data visualizations
 *
 * Features:
 * - Fixed at bottom with safe area insets
 * - 44x44px minimum touch targets
 * - Active tab highlighting
 * - Badge counts for comparison selection
 * - Only visible on mobile viewports (<768px)
 */
const TabBar = ({
  activeTab = "dashboard",
  onTabChange,
  comparisonCount = 0,
}) => {
  const tabs = [
    {
      id: "dashboard",
      label: "Dashboard",
      icon: (
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
        >
          <rect x="3" y="3" width="7" height="7" />
          <rect x="14" y="3" width="7" height="7" />
          <rect x="3" y="14" width="7" height="7" />
          <rect x="14" y="14" width="7" height="7" />
        </svg>
      ),
    },
    {
      id: "compare",
      label: "Compare",
      icon: (
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
        >
          <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" />
          <polyline points="7.5 4.21 12 6.81 16.5 4.21" />
          <polyline points="7.5 19.79 7.5 14.6 3 12" />
          <polyline points="21 12 16.5 14.6 16.5 19.79" />
          <polyline points="3.27 6.96 12 12.01 20.73 6.96" />
          <line x1="12" y1="22.08" x2="12" y2="12" />
        </svg>
      ),
      badge: comparisonCount > 0 ? comparisonCount : null,
    },
    {
      id: "visualizations",
      label: "Charts",
      icon: (
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
        >
          <line x1="18" y1="20" x2="18" y2="10" />
          <line x1="12" y1="20" x2="12" y2="4" />
          <line x1="6" y1="20" x2="6" y2="14" />
        </svg>
      ),
    },
  ];

  const handleTabClick = (tabId) => {
    if (onTabChange && tabId !== activeTab) {
      onTabChange(tabId);
    }
  };

  return (
    <nav className="tab-bar" role="navigation" aria-label="Primary navigation">
      <div className="tab-bar__container">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            className={`tab-bar__tab ${activeTab === tab.id ? "tab-bar__tab--active" : ""}`}
            onClick={() => handleTabClick(tab.id)}
            aria-label={tab.label}
            aria-current={activeTab === tab.id ? "page" : undefined}
          >
            <span className="tab-bar__icon">
              {tab.icon}
              {tab.badge && (
                <span
                  className="tab-bar__badge"
                  aria-label={`${tab.badge} items selected`}
                >
                  {tab.badge}
                </span>
              )}
            </span>
            <span className="tab-bar__label">{tab.label}</span>
          </button>
        ))}
      </div>
    </nav>
  );
};

export default TabBar;
