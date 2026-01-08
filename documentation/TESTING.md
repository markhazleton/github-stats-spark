# Testing Guide - GitHub Stats Spark Dashboard

This guide explains how to test the Repository Comparison Dashboard locally and in production.

## Prerequisites

- **Node.js** 18+ and npm 9+ (for frontend)
- **Python** 3.11+ (for backend data generation)
- **GitHub Personal Access Token** (for API access)

## Quick Start Testing

### Option 1: Test with Mock Data (Fastest)

1. **Create sample data file**:
```bash
# Create the data directory
mkdir -p docs/data

# Create a sample repositories.json file
cat > docs/data/repositories.json << 'EOF'
{
  "repositories": [
    {
      "name": "example-repo-1",
      "language": "JavaScript",
      "created_at": "2023-01-15T10:00:00Z",
      "last_commit_date": "2024-12-01T15:30:00Z",
      "first_commit_date": "2023-01-20T08:00:00Z",
      "commit_count": 342,
      "avg_commit_size": 45.2,
      "largest_commit": {
        "sha": "abc1234",
        "date": "2024-06-15T12:00:00Z",
        "size": 1250,
        "files_changed": 15,
        "lines_added": 800,
        "lines_deleted": 435
      },
      "smallest_commit": {
        "sha": "def5678",
        "date": "2023-03-10T09:00:00Z",
        "size": 3,
        "files_changed": 1,
        "lines_added": 2,
        "lines_deleted": 0
      },
      "stars": 42,
      "forks": 8,
      "url": "https://github.com/test/example-repo-1",
      "description": "An example JavaScript repository"
    },
    {
      "name": "python-project",
      "language": "Python",
      "created_at": "2022-06-01T10:00:00Z",
      "last_commit_date": "2024-11-20T15:30:00Z",
      "first_commit_date": "2022-06-05T08:00:00Z",
      "commit_count": 567,
      "avg_commit_size": 62.8,
      "largest_commit": {
        "sha": "ghi9012",
        "date": "2024-05-20T12:00:00Z",
        "size": 2100,
        "files_changed": 25,
        "lines_added": 1200,
        "lines_deleted": 875
      },
      "smallest_commit": {
        "sha": "jkl3456",
        "date": "2022-08-10T09:00:00Z",
        "size": 2,
        "files_changed": 1,
        "lines_added": 1,
        "lines_deleted": 0
      },
      "stars": 128,
      "forks": 23,
      "url": "https://github.com/test/python-project",
      "description": "A Python data analysis project"
    }
  ],
  "profile": {
    "username": "test-user",
    "avatar_url": "https://github.com/identicons/test.png",
    "public_repos_count": 2,
    "profile_url": "https://github.com/test-user",
    "total_stars": 170,
    "total_forks": 31
  },
  "metadata": {
    "generated_at": "2024-12-15T12:00:00Z",
    "schema_version": "1.0.0",
    "repository_count": 2,
    "data_source": "GitHub API"
  }
}
EOF
```

2. **Install frontend dependencies**:
```bash
cd frontend
npm install
```

3. **Start development server**:
```bash
npm run dev
```

4. **Open browser**: Navigate to `http://localhost:5173`

You should see:
- ✅ A table with 2 repositories
- ✅ Sortable columns
- ✅ Language filter dropdown
- ✅ Clickable repository names

---

### Option 2: Test with Real Data (Full Integration)

#### Step 1: Generate Real Dashboard Data

1. **Set GitHub token**:
```bash
# Windows (PowerShell)
$env:GITHUB_TOKEN="your_github_token_here"

# Windows (CMD)
set GITHUB_TOKEN=your_github_token_here

# Linux/Mac
export GITHUB_TOKEN=your_github_token_here
```

2. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

3. **Generate dashboard data**:
```bash
python -m spark.cli generate --user YOUR_GITHUB_USERNAME --dashboard --verbose
```

This will:
- Fetch your public repositories from GitHub
- Calculate commit metrics
- Generate `docs/data/repositories.json`

**Example output**:
```
======================================================================
Dashboard Data Generation
======================================================================
Username: markhazleton
Config: config/spark.yml

Generating dashboard data...
Fetching repositories for markhazleton...
Found 45 repositories
Processing repository 1/45: github-stats-spark
Processing repository 2/45: portfolio-website
...
Writing dashboard data to docs\data\repositories.json...
Dashboard data written successfully (125.34 KB)

======================================================================
✅ Dashboard Generation Complete!
======================================================================
Output: docs\data\repositories.json
Repositories: 45
Username: markhazleton
Schema Version: 1.0.0
Generation Time: 78.3s
======================================================================
```

#### Step 2: Start Frontend Development Server

```bash
cd frontend
npm install  # If not already done
npm run dev
```

Open `http://localhost:5173` in your browser.

---

## What to Test

### ✅ Basic Functionality

1. **Data Loading**:
   - [ ] Dashboard loads without errors
   - [ ] Loading spinner appears briefly
   - [ ] Table displays all repositories

2. **Table Display**:
   - [ ] All columns are visible (Name, Language, Dates, Commits, Sizes, Stars)
   - [ ] Data is formatted correctly (dates, numbers)
   - [ ] Repository links open in new tab

3. **Sorting**:
   - [ ] Click column headers to sort
   - [ ] Arrow indicators show sort direction
   - [ ] Numeric columns sort correctly (Stars, Commits)
   - [ ] Date columns sort chronologically

4. **Filtering**:
   - [ ] Language filter dropdown appears
   - [ ] Selecting a language filters table
   - [ ] "All Languages" shows all repositories
   - [ ] Count updates correctly

5. **Tooltips**:
   - [ ] Hover over commit sizes shows tooltip
   - [ ] Hover over largest/smallest commits shows SHA and date
   - [ ] Tooltips disappear on mouse out

6. **Responsive Design**:
   - [ ] Resize browser window
   - [ ] Table adapts to smaller screens
   - [ ] Horizontal scroll appears on mobile

### ⚠️ Edge Cases to Test

1. **Missing Data**:
   - Check repositories with:
     - Missing language → Shows "Unknown"
     - Zero commits → Shows "N/A" or "0"
     - Missing dates → Shows "N/A"

2. **Large Datasets**:
   - Test with 100+ repositories
   - Verify sorting/filtering performance (<1 second)

3. **Error Handling**:
   - Rename `repositories.json` temporarily
   - Verify error message appears
   - Restore file and reload

---

## Testing Commands Reference

```bash
# Frontend Development
cd frontend
npm install           # Install dependencies
npm run dev          # Start dev server (http://localhost:5173)
npm run build        # Build for production
npm run preview      # Preview production build

# Backend Data Generation
python -m spark.cli generate --user USERNAME --dashboard --verbose

# Run with cache refresh
python -m spark.cli generate --user USERNAME --dashboard --force-refresh --verbose

# View help
python -m spark.cli generate --help
```

---

## Troubleshooting

### Frontend won't start

**Error**: `Cannot find module 'vite'`
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Data file not found

**Error**: `Failed to fetch dashboard data: 404`
- Check `docs/data/repositories.json` exists
- Run backend generation first
- Verify file is valid JSON: `cat docs/data/repositories.json | python -m json.tool`

### GitHub API Rate Limit

**Error**: `Rate limit exceeded`
- Use authenticated token (5000 requests/hour)
- Wait for rate limit reset
- Check status: `curl https://api.github.com/rate_limit`

### CORS Errors in Development

If you see CORS errors:
1. Check `vite.config.js` proxy configuration
2. Ensure `docs/data/` is accessible
3. Try `npm run preview` instead of `npm run dev`

---

## Production Testing (GitHub Pages)

After deploying to GitHub Pages:

1. **Verify URL**: `https://YOUR_USERNAME.github.io/github-stats-spark/`

2. **Check console**: Open browser DevTools (F12) → Console tab
   - Should be error-free
   - Look for successful data fetch logs

3. **Verify assets**:
   - Check `https://YOUR_USERNAME.github.io/github-stats-spark/data/repositories.json`
   - Should return valid JSON

4. **Test all features**: Run through checklist above

---

## Performance Testing

### Load Time
- Open DevTools → Network tab
- Hard refresh (Ctrl+Shift+R)
- Check:
  - Initial load: <3 seconds
  - `repositories.json`: <2 seconds
  - Total page size: <600KB

### Interaction Speed
- Sort column: Should be instant (<100ms)
- Filter by language: Should be instant (<100ms)
- Row hover: Smooth, no lag

### Lighthouse Audit
```bash
# Install Lighthouse
npm install -g lighthouse

# Run audit on local dev server
lighthouse http://localhost:5173 --view

# Or use Chrome DevTools → Lighthouse tab
```

Target scores:
- Performance: >90
- Accessibility: >90
- Best Practices: >90
- SEO: >80

---

## Next Steps After Testing

Once everything works:

1. **Commit your changes**:
```bash
git add .
git commit -m "feat: Complete MVP - Repository comparison dashboard with table view"
git push origin 001-repo-comparison-dashboard
```

2. **Create Pull Request** (if working with branches)

3. **Deploy to GitHub Pages**:
   - Push to `main` branch
   - GitHub Actions will auto-deploy

4. **Continue development**:
   - User Story 2: Enhanced sorting/filtering
   - User Story 4: Repository comparison
   - User Story 5: Drill-down details

---

## Questions or Issues?

If you encounter problems:
1. Check browser console (F12) for errors
2. Review this testing guide
3. Verify all prerequisites are met
4. Check GitHub Issues for similar problems
