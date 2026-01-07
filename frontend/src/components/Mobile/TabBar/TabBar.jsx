import "./TabBar.css";

/**
 * TabBar - Fixed bottom navigation for mobile devices
 *
 * Provides primary section navigation with 2 tabs:
 * - Dashboard: Repository browsing and filtering
 * - Visualizations: Charts and data visualizations
 *
 * Features:
 * - Fixed at bottom with safe area insets
 * - 44x44px minimum touch targets
 * - Active tab highlighting
 * - Only visible on mobile viewports (<768px)
 */
const TabBar = ({ activeTab = "table", onTabChange }) => {
  const tabs = [
    {
      id: "table",
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
            <span className="tab-bar__icon">{tab.icon}</span>
            <span className="tab-bar__label">{tab.label}</span>
          </button>
        ))}
      </div>
    </nav>
  );
};

export default TabBar;
