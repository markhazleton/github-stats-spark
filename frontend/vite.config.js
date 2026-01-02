import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],

  // Base URL for GitHub Pages deployment
  base: '/github-stats-spark/',

  // Build configuration
  build: {
    outDir: '../docs',
    emptyOutDir: true,

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
          'vendor-charts': ['recharts']
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
    chunkSizeWarningLimit: 500, // 500KB warning threshold

    // Source maps for debugging (disable for production)
    sourcemap: false
  },

  // Development server configuration
  server: {
    port: 5173,
    open: true,
    proxy: {
      // Proxy API requests to avoid CORS during development
      '/data': {
        target: 'http://localhost:5173',
        changeOrigin: true
      }
    }
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
