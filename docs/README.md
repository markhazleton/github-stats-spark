# Frontend Public Assets

This directory contains static assets served directly by Vite during development and copied to the build output.

## Directory Structure

- **favicon.svg** - Site favicon
- **manifest.json** - PWA manifest
- **robots.txt** - Search engine directives
- **sitemap.xml** - Site map for SEO
- **sw.js** - Service worker for PWA features
- **404.html** - Custom 404 page for GitHub Pages
- **CNAME** - Custom domain configuration
- **.nojekyll** - Disables Jekyll processing on GitHub Pages
- **data/** - Symlink to project root data directory (created during build)

## Data Directory Setup

The `data` directory is a symlink to `../../data` that provides access to `repositories.json` during builds.

### GitHub Actions (Linux)
The workflow automatically creates the symlink:
```bash
ln -s ../../data frontend/public/data
```

### Local Development (Windows)
For local testing, you don't need the symlink. The Vite dev server serves data from the root directory via the `serveDataPlugin` in `vite.config.js`.

If you encounter build issues on Windows, you can manually create a directory junction:
```powershell
# Remove existing file/link
Remove-Item frontend\public\data -Force -ErrorAction SilentlyContinue

# Create directory junction (requires admin on older Windows versions)
New-Item -ItemType Junction -Path frontend\public\data -Target ..\..\data
```

Or use mklink (requires admin):
```cmd
mklink /J frontend\public\data ..\..\data
```

### Local Development (macOS/Linux)
```bash
ln -s ../../data frontend/public/data
```

## Build Process

During the build:
1. Vite copies public assets to `docs/` (build output)
2. The workflow copies `data/repositories.json` to `docs/data/`
3. GitHub Pages serves from `docs/`

## Notes

- The `data` symlink is git-ignored to prevent cross-platform issues
- Build-time checks ensure data exists before deployment
- Dev server middleware handles data serving without requiring symlinks
