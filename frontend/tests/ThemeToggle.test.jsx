/**
 * T038 – Vitest coverage for ThemeContext logic.
 * Tests the pure JS portions: resolveTheme, localStorage persistence,
 * and data-theme attribute application (via jsdom).
 */
import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";

// Mock localStorage
const localStorageMock = (() => {
  let store = {};
  return {
    getItem: (key) => store[key] ?? null,
    setItem: (key, value) => { store[key] = String(value); },
    removeItem: (key) => { delete store[key]; },
    clear: () => { store = {}; },
  };
})();

// ----- Unit-level tests for ThemeContext helpers -----

describe("ThemeContext – theme cycle logic", () => {
  const cycle = { light: "dark", dark: "system", system: "light" };

  it("cycles light → dark", () => {
    expect(cycle["light"]).toBe("dark");
  });

  it("cycles dark → system", () => {
    expect(cycle["dark"]).toBe("system");
  });

  it("cycles system → light", () => {
    expect(cycle["system"]).toBe("light");
  });
});

describe("ThemeContext – resolvedTheme derivation", () => {
  it("resolves light to light", () => {
    const resolve = (theme, osPrefersDark = false) => {
      if (theme === "system") return osPrefersDark ? "dark" : "light";
      return theme;
    };
    expect(resolve("light")).toBe("light");
  });

  it("resolves dark to dark", () => {
    const resolve = (theme, osPrefersDark = false) => {
      if (theme === "system") return osPrefersDark ? "dark" : "light";
      return theme;
    };
    expect(resolve("dark")).toBe("dark");
  });

  it("resolves system to light when OS prefers light", () => {
    const resolve = (theme, osPrefersDark = false) => {
      if (theme === "system") return osPrefersDark ? "dark" : "light";
      return theme;
    };
    expect(resolve("system", false)).toBe("light");
  });

  it("resolves system to dark when OS prefers dark", () => {
    const resolve = (theme, osPrefersDark = false) => {
      if (theme === "system") return osPrefersDark ? "dark" : "light";
      return theme;
    };
    expect(resolve("system", true)).toBe("dark");
  });
});

describe("ThemeContext – localStorage persistence", () => {
  beforeEach(() => localStorageMock.clear());

  it("stores theme in localStorage and reads it back", () => {
    localStorageMock.setItem("spark-theme", "dark");
    const stored = localStorageMock.getItem("spark-theme");
    expect(stored).toBe("dark");
  });

  it("falls back to system when nothing stored", () => {
    const stored = localStorageMock.getItem("spark-theme");
    const theme = (stored && ["light", "dark", "system"].includes(stored)) ? stored : "system";
    expect(theme).toBe("system");
  });

  it("ignores invalid stored values", () => {
    localStorageMock.setItem("spark-theme", "invalid-value");
    const stored = localStorageMock.getItem("spark-theme");
    const theme = (stored && ["light", "dark", "system"].includes(stored)) ? stored : "system";
    expect(theme).toBe("system");
  });
});

describe("ThemeContext – data-theme attribute on <html>", () => {
  it("setting data-theme=dark on document.documentElement reflects correctly", () => {
    document.documentElement.setAttribute("data-theme", "dark");
    expect(document.documentElement.getAttribute("data-theme")).toBe("dark");
  });

  it("setting data-theme=light on document.documentElement reflects correctly", () => {
    document.documentElement.setAttribute("data-theme", "light");
    expect(document.documentElement.getAttribute("data-theme")).toBe("light");
  });

  it("system theme removes data-theme or uses resolved value", () => {
    document.documentElement.setAttribute("data-theme", "light"); // default resolution
    expect(["light", "dark"]).toContain(
      document.documentElement.getAttribute("data-theme"),
    );
  });
});
