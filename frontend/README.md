# GitHub Stats Spark - Dashboard Frontend

This README is an approved contributor-focused exception to the primary `.documentation/` tree. Use `.documentation/README.md` for the main project documentation index, and use this file for frontend workspace setup and build details.

Interactive React dashboard for visualizing and comparing GitHub repository statistics.

## 🚀 Features

- **Repository Table**: Sortable, filterable table with comprehensive metrics
- **Interactive Visualizations**: Bar charts, line graphs, and scatter plots using Chart.js + react-chartjs-2
- **Needs Attention View**: Maintenance ranking using security alerts, PR backlog, dependency health, and staleness
- **Repository Comparison**: Side-by-side comparison of up to 5 repositories with color-coded differences
- **Drill-Down Details**: Comprehensive repository analysis with commit history, dependency coverage, and markdown-rendered summaries
- **Export Functionality**: Export data to CSV or JSON format
- **Responsive Design**: Mobile-friendly with CSS Modules and custom properties

## 📋 Prerequisites

- Node.js 18+
- npm 9+

## 🛠️ Development Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Access at http://localhost:5173/github-stats-spark/
```

## 🏗️ Build for Production

```bash
# Build optimized production bundle
npm run build

# Output will be in /docs directory
# - docs/index.html
# - docs/assets/site-[hash].js
# - docs/assets/site-[hash].css
# - docs/data/ (copied from /data)
```

## 📂 Project Structure

```text
frontend/
├── src/
│   ├── components/
│   │   ├── Common/           # Reusable components (LoadingState, Tooltip, FilterControls, ExportButton, ErrorBoundary, MarkdownContent)
│   │   ├── Attention/        # Maintenance triage views and styles
│   │   ├── RepositoryTable/  # Table components (Table, Header, Row)
│   │   ├── Visualizations/   # Chart components (Bar, Line, Scatter, Controls)
│   │   ├── Comparison/       # Comparison components (Selector, View)
│   │   └── DrillDown/        # Detail view components (RepositoryDetail)
│   ├── hooks/
│   │   ├── useRepositoryData.js  # Data fetching hook
│   │   └── useTableSort.js       # Sort/filter logic
│   ├── services/
│   │   ├── dataService.js        # Data fetching and parsing
│   │   └── metricsCalculator.js  # Chart transformations and formatting
│   ├── styles/
│   │   └── global.css            # Global styles and CSS variables
│   ├── App.jsx                   # Root component with routing
│   └── main.jsx                  # Entry point
├── public/                       # Static assets
├── vite.config.js               # Vite configuration
└── package.json                 # Dependencies and scripts
```

## 🎨 Component Documentation

### App.jsx

Root component managing:

- View state (summary, visualizations, attention)
- Repository selection for comparison
- Modal state for drill-down details
- Data fetching and processing

### AttentionView

Maintenance triage surface showing:

- Attention ranking ordered by `attention_score`
- Security, PR, staleness, and dependency component breakdowns
- Quick triage list for the highest-priority repositories

### RepositoryTable

Displays repository data with:

- Sortable columns (click header to sort)
- Checkbox selection for comparison
- Row click for drill-down details
- Export functionality

### Visualizations

Three chart types:

- **BarChart**: Top N repositories by selected metric
- **LineGraph**: Temporal trends
- **ScatterPlot**: Commits vs. commit size correlation

### ComparisonView

Side-by-side comparison showing:

- Color-coded metric highlighting (green=highest, red=lowest)
- Percentage differences from maximum value
- Remove repository functionality

### RepositoryDetail

Comprehensive repository analysis:

- Commit history timeline (90d, 180d, 365d)
- Language breakdown
- Technology stack, dependency coverage, and latest-version visibility
- AI-generated summaries rendered as GitHub-flavored markdown
- Next/Previous navigation

## 🔧 Configuration

### Vite Config (`vite.config.js`)

- Base path: `/github-stats-spark/` (for GitHub Pages)
- Output directory: `../docs`
- Path aliases: `@/` → `src/`
- Custom middleware for `/data` serving in development

### Build Scripts

- `npm run dev` - Development server with HMR
- `npm run build` - Production build
- `npm run preview` - Preview production build locally
- `npm run lint` - ESLint code quality check

## 📊 Data Format

The dashboard expects `data/repositories.json` with schema version 2.2.0:

```json
{
  "repositories": [
    {
      "name": "repo-name",
      "language": "JavaScript",
      "stars": 42,
      "attention_score": 61.4,
      "attention_rank": 2,
      "attention_metrics": {
        "tier": "elevated",
        "needs_attention": true
      },
      "commit_history": {
        "total_commits": 150,
        "first_commit_date": "2024-01-01T00:00:00Z",
        "last_commit_date": "2024-12-31T23:59:59Z"
      },
      "tech_stack": {
        "version_coverage_percentage": 83.3,
        "latest_version_coverage_percentage": 66.7,
        "dependencies": []
      }
    }
  ],
  "profile": { "username": "...", "total_commits": 1000 },
  "metadata": { "generated_at": "...", "schema_version": "2.2.0" }
}
```

## 🎯 Performance Optimizations

- React.memo for table rows (efficient re-renders)
- useMemo for expensive computations (chart data transformations)
- Code splitting with React.lazy (charts loaded on demand)
- CSS Modules for scoped styling (prevents style conflicts)
- Vite build optimizations (tree-shaking, minification)

## ♿ Accessibility

- ARIA labels on interactive elements
- Keyboard navigation support (Tab, Enter, ESC)
- Screen reader compatible
- Error boundary for graceful error handling
- Focus management in modals

## 🚢 Deployment

The dashboard is designed for GitHub Pages deployment:

1. Data is generated by Python backend → `/data/repositories.json`
2. Frontend builds to `/docs` directory
3. GitHub Pages serves from `/docs` on main branch
4. Automatic updates via GitHub Actions workflow

## 🤝 Contributing

When adding new components:

1. Use functional components with hooks
2. Add PropTypes for type checking
3. Use CSS Modules for styling
4. Add JSDoc comments
5. Follow existing patterns (see component examples)

## 📝 License

Part of the GitHub Stats Spark project. See main README for license information.
