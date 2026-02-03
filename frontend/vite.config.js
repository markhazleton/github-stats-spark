import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'
import fs from 'fs'

// Plugin to serve /data and /output directories in dev mode
const serveDataPlugin = () => ({
  name: 'serve-data',
  configureServer(server) {
    server.middlewares.use((req, res, next) => {
      const url = new URL(req.url, 'http://localhost')
      // Strip base path for dev server routing
      const basePath = '/github-stats-spark'
      let pathname = url.pathname
      if (pathname.startsWith(basePath)) {
        pathname = pathname.slice(basePath.length)
      }
      // Serve data directory
      if (pathname.startsWith('/data/')) {
        const filePath = path.resolve(__dirname, '..', pathname.slice(1))
        if (fs.existsSync(filePath)) {
          const content = fs.readFileSync(filePath)
          res.setHeader('Content-Type', 'application/json')
          res.end(content)
          return
        }
      }
      // Serve output/screenshots directory
      if (pathname.startsWith('/output/')) {
        const filePath = path.resolve(__dirname, '..', pathname.slice(1))
        if (fs.existsSync(filePath)) {
          const content = fs.readFileSync(filePath)
          const ext = path.extname(filePath).toLowerCase()
          const mimeTypes = { '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp' }
          res.setHeader('Content-Type', mimeTypes[ext] || 'application/octet-stream')
          res.end(content)
          return
        }
      }
      next()
    })
  }
})

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    serveDataPlugin()
  ],

  // Base URL for GitHub Pages deployment
  base: '/github-stats-spark/',

  // Public directory for static assets (favicon, etc)
  publicDir: 'public',

  // Build configuration
  build: {
    outDir: '../docs',
    emptyOutDir: true, // Clean build - data will be copied after
    
    // Copy public directory manually to handle symlinks gracefully
    copyPublicDir: fs.existsSync(path.join(__dirname, 'public', 'data')),

    // Single bundle output optimization
    rollupOptions: {
      output: {
        // Generate predictable filenames
        entryFileNames: 'assets/site-[hash].js',
        chunkFileNames: 'assets/site-[hash].js',
        assetFileNames: (assetInfo) => {
          if (assetInfo.name.endsWith('.css')) {
            return 'assets/site-[hash].css'
          }
          return 'assets/[name]-[hash][extname]'
        },

        // Optimize chunk splitting
        manualChunks: {
          // Vendor chunks for better caching
          'vendor-react': ['react', 'react-dom'],
          'vendor-charts': ['chart.js', 'react-chartjs-2']
        }
      }
    },

    // Bundle size optimizations
    cssCodeSplit: false, // Single CSS file
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true, // Remove console.log in production
        drop_debugger: true
      }
    },

    // Performance budgets (warnings)
    chunkSizeWarningLimit: 170, // 170KB warning threshold (performance budget)

    // Source maps for debugging (disable for production)
    sourcemap: false
  },

  // Development server configuration
  server: {
    port: 5173,
    open: true,
    hmr: {
      protocol: 'ws',
      host: 'localhost',
      port: 5173,
      clientPort: 5173
    },
    fs: {
      // Allow serving files from parent directory (/data)
      allow: ['..']
    }
  },

  // Optimize deps to prevent React resolution issues
  optimizeDeps: {
    include: ['react', 'react-dom', 'react/jsx-runtime', 'react/jsx-dev-runtime'],
    exclude: []
  },

  // CSS Modules configuration
  css: {
    modules: {
      localsConvention: 'camelCase',
      generateScopedName: '[name]__[local]___[hash:base64:5]'
    }
  },

  // Resolve configuration
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@services': path.resolve(__dirname, './src/services'),
      '@hooks': path.resolve(__dirname, './src/hooks'),
      '@styles': path.resolve(__dirname, './src/styles')
    }
  },

  // Test configuration (for Vitest)
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './tests/setup.js',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        'tests/',
        '**/*.config.js'
      ]
    }
  }
})
