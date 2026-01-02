import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import '@/styles/global.css'

/**
 * GitHub Stats Spark Dashboard - Main Entry Point
 *
 * This is the root entry point for the React application.
 * It renders the main App component into the DOM.
 *
 * Features:
 * - React 18+ with StrictMode for development checks
 * - Global CSS styles loaded
 * - App component as the root of the component tree
 */

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
