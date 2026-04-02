/**
 * ThemeContext.jsx
 *
 * React context for light/dark/system theme preference.
 *
 * - Reads from localStorage on mount (key: "spark-theme")
 * - Applies `data-theme` attribute on <html> for CSS selector-based theming
 * - Falls back to OS prefers-color-scheme when theme === "system"
 * - Provides: theme, resolvedTheme, setTheme, toggleTheme
 */

import React, { createContext, useContext, useEffect, useState } from "react";

const STORAGE_KEY = "spark-theme";
const VALID_THEMES = ["light", "dark", "system"];

const ThemeContext = createContext({
  theme: "system",
  resolvedTheme: "light",
  setTheme: () => {},
  toggleTheme: () => {},
});

function getOsPreference() {
  if (typeof window !== "undefined" && window.matchMedia) {
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }
  return "light";
}

function resolveTheme(theme) {
  if (theme === "system") return getOsPreference();
  return theme;
}

export function ThemeProvider({ children }) {
  const [theme, setThemeState] = useState(() => {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored && VALID_THEMES.includes(stored)) return stored;
    } catch {
      // localStorage may be unavailable in some environments
    }
    return "system";
  });

  const [resolvedTheme, setResolvedTheme] = useState(() => resolveTheme(theme));

  // Apply data-theme to <html> whenever resolved theme changes
  useEffect(() => {
    const resolved = resolveTheme(theme);
    setResolvedTheme(resolved);
    document.documentElement.setAttribute("data-theme", resolved);
  }, [theme]);

  // Listen for OS preference changes when in "system" mode
  useEffect(() => {
    if (theme !== "system") return;
    const mq = window.matchMedia("(prefers-color-scheme: dark)");
    const onChange = () => {
      const resolved = resolveTheme("system");
      setResolvedTheme(resolved);
      document.documentElement.setAttribute("data-theme", resolved);
    };
    mq.addEventListener("change", onChange);
    return () => mq.removeEventListener("change", onChange);
  }, [theme]);

  const setTheme = (newTheme) => {
    if (!VALID_THEMES.includes(newTheme)) return;
    try {
      localStorage.setItem(STORAGE_KEY, newTheme);
    } catch {
      // ignore write failures
    }
    setThemeState(newTheme);
  };

  const toggleTheme = () => {
    const cycle = { light: "dark", dark: "system", system: "light" };
    setTheme(cycle[theme] ?? "system");
  };

  return (
    <ThemeContext.Provider value={{ theme, resolvedTheme, setTheme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}

export default ThemeContext;
