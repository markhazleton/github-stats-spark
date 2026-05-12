# GitHub Stats Spark Dashboard

## Project Overview
An interactive GitHub analytics and visualization dashboard. It displays GitHub profile statistics, repository comparisons, and AI-powered repository analysis in a mobile-first React interface.

## Tech Stack
- **Frontend**: React 19, Vite 8, Chart.js, Dexie (IndexedDB)
- **Python Backend/CLI**: Fetches GitHub data and generates SVG visualizations
- **Dev Server**: Runs on port 5000

## Project Structure
- `frontend/` — React + Vite dashboard source code
- `src/spark/` — Python CLI for data fetching and SVG generation
- `data/` — Raw and processed JSON data files
- `output/` — Generated SVG and screenshot assets
- `config/` — YAML config files for themes and spark engine
- `docs/` — Production build output (GitHub Pages target)

## Running the App
The frontend dev server runs via the "Start application" workflow:
```
cd frontend && npm run dev
```
Runs on `0.0.0.0:5000`.

## User Preferences
- Keep frontend on port 5000
- Use `npm` for frontend package management
