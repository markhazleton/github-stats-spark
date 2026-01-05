import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import ErrorBoundary from "@/components/ErrorBoundary/ErrorBoundary";
import { OfflineCacheProvider } from "@/contexts/OfflineCacheContext";
import "@/styles/global.css";

/**
 * GitHub Stats Spark Dashboard - Main Entry Point
 *
 * This is the root entry point for the React application.
 * It renders the main App component into the DOM.
 *
 * Features:
 * - React 18+ with StrictMode for development checks
 * - ErrorBoundary for graceful error handling
 * - Global CSS styles loaded
 * - Service Worker registration for offline support
 * - App component as the root of the component tree
 */

/**
 * Register Service Worker for offline functionality
 */
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register(import.meta.env.BASE_URL + "sw.js", {
        scope: import.meta.env.BASE_URL,
      })
      .then((registration) => {
        console.log(
          "[Service Worker] Registered successfully:",
          registration.scope,
        );

        // Check for updates every hour
        setInterval(
          () => {
            registration.update();
          },
          60 * 60 * 1000,
        );

        // Listen for updates
        registration.addEventListener("updatefound", () => {
          const newWorker = registration.installing;

          if (newWorker) {
            newWorker.addEventListener("statechange", () => {
              if (
                newWorker.state === "installed" &&
                navigator.serviceWorker.controller
              ) {
                // New version available
                console.log("[Service Worker] New version available");

                // Show update notification
                if (
                  window.confirm("New version available! Reload to update?")
                ) {
                  newWorker.postMessage({ type: "SKIP_WAITING" });
                  window.location.reload();
                }
              }
            });
          }
        });
      })
      .catch((error) => {
        console.error("[Service Worker] Registration failed:", error);
      });

    // Listen for controller change (SW activated)
    navigator.serviceWorker.addEventListener("controllerchange", () => {
      console.log("[Service Worker] Controller changed, reloading page");
      window.location.reload();
    });
  });
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ErrorBoundary>
      <OfflineCacheProvider>
        <App />
      </OfflineCacheProvider>
    </ErrorBoundary>
  </React.StrictMode>,
);
