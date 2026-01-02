# GitHub Stats Spark - Dashboard Frontend

Interactive React dashboard for visualizing and comparing GitHub repository statistics.

## 🚀 Features

- **Repository Table**: Sortable, filterable table with comprehensive metrics
- **Interactive Visualizations**: Bar charts, line graphs, and scatter plots using Recharts
- **Repository Comparison**: Side-by-side comparison of up to 5 repositories with color-coded differences
- **Drill-Down Details**: Comprehensive repository analysis with commit history and tech stack
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

```
frontend/
├── src/
│   ├── components/
│   │   ├── Common/           # Reusable components (LoadingState, Tooltip, FilterControls, ExportButton, ErrorBoundary)
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
- View state (table, visualizations, comparison)
- Repository selection for comparison
- Modal state for drill-down details
- Data fetching and processing

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
- Technology stack and dependencies
- AI-generated summaries (when available)
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

The dashboard expects `data/repositories.json` with schema version 2.0.0:

```json
{
  "repositories": [
    {
      "name": "repo-name",
      "language": "JavaScript",
      "stars": 42,
      "commit_history": {
        "total_commits": 150,
        "first_commit_date": "2024-01-01T00:00:00Z",
        "last_commit_date": "2024-12-31T23:59:59Z"
      },
      "commit_metrics": {
        "avg_size": 123.5,
        "largest_commit": { "size": 500, "sha": "abc123" },
        "smallest_commit": { "size": 10, "sha": "def456" }
      }
    }
  ],
  "profile": { "username": "...", "total_commits": 1000 },
  "metadata": { "generated_at": "...", "schema_version": "2.0.0" }
}
```

## 🎯 Performance Optimizations

- React.memo for table rows (efficient re-renders)
- useMemo for expensive computations (chart data transformations)
- useCallback for event handlers
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
