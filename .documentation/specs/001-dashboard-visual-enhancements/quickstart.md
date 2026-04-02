# Quickstart: Dashboard Visual Enhancements

**Feature**: 001-dashboard-visual-enhancements  
**Branch**: `001-dashboard-visual-enhancements`

## Prerequisites

```bash
# Python backend
pip install -r requirements.txt
pip install -e .

# Frontend
cd frontend && npm install
```

## Development Workflow

### 1. Backend Changes (Python)

Modify three files to add new data to `repositories.json`:

```bash
# Key files to edit:
src/spark/calculator.py          # Bus factor calculation
src/spark/fetcher.py             # Contributor stats + code frequency API calls
src/spark/unified_data_generator.py  # Persist new fields in JSON output

# Run backend to generate data:
spark unified --user markhazleton --verbose

# Verify new fields in output:
python -c "import json; d=json.load(open('data/repositories.json')); print(d['profile'].get('activity_calendar', {}).keys().__len__(), 'days'); print(d['repositories'][0].get('bus_factor'))"
```

### 2. Frontend Changes (React)

```bash
cd frontend

# Start dev server
npm run dev

# Key files to create:
# frontend/src/components/Visualizations/ContributionHeatmap.jsx
# frontend/src/components/Visualizations/ActivityTimeline.jsx
# frontend/src/components/Common/ThemeToggle.jsx
# frontend/src/contexts/ThemeContext.jsx

# Run tests
npm test
```

### 3. Verify End-to-End

```bash
# Generate fresh data
spark unified --user markhazleton --verbose

# Build frontend
cd frontend && npm run build

# Verify output in docs/ directory
# Open docs/index.html in browser
```

## Testing Checklist

- [ ] `pytest tests/unit/test_calculator.py` — bus factor tests pass
- [ ] `cd frontend && npm test` — new component tests pass
- [ ] Heatmap renders with real data from `activity_calendar`
- [ ] Timeline shows 52 weeks of activity with toggleable series
- [ ] Dark mode toggle persists across page reloads
- [ ] Existing SVGs unchanged (compare output/ before and after)
- [ ] ExportButton includes new fields (bus_factor, code_churn)
- [ ] Dashboard loads with a pre-2.3.0 JSON file without errors

## Key Architecture Decisions

1. **No new chart library** — heatmap is a custom CSS Grid component
2. **Chart.js for timeline** — uses existing `react-chartjs-2`
3. **`commits_by_day` already computed** — just needs to be persisted in JSON
4. **ExportButton already exists** — only needs column updates for new fields
5. **Dark mode CSS already written** — refactor `@media` to `[data-theme]` selectors
