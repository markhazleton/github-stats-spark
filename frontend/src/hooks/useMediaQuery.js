import { useState, useEffect } from "react";

/**
 * useMediaQuery Hook
 * Detects if a media query matches
 *
 * @param {string} query - CSS media query string
 * @returns {boolean} Whether the query matches
 *
 * @example
 * const isMobile = useMediaQuery('(max-width: 767px)');
 * const isDesktop = useMediaQuery('(min-width: 1024px)');
 */
export function useMediaQuery(query) {
  const [matches, setMatches] = useState(() => {
    if (typeof window !== "undefined") {
      return window.matchMedia(query).matches;
    }
    return false;
  });

  useEffect(() => {
    const mediaQuery = window.matchMedia(query);

    const handleChange = (e) => {
      setMatches(e.matches);
    };

    // Listen for changes
    mediaQuery.addEventListener("change", handleChange);

    return () => {
      mediaQuery.removeEventListener("change", handleChange);
    };
  }, [query]);

  return matches;
}

/**
 * Predefined breakpoint hooks
 */
export function useBreakpoint() {
  const isXs = useMediaQuery("(max-width: 319px)");
  const isSm = useMediaQuery("(min-width: 320px) and (max-width: 767px)");
  const isMd = useMediaQuery("(min-width: 768px) and (max-width: 1023px)");
  const isLg = useMediaQuery("(min-width: 1024px) and (max-width: 1279px)");
  const isXl = useMediaQuery("(min-width: 1280px)");

  const isMobile = useMediaQuery("(max-width: 767px)");
  const isTablet = useMediaQuery("(min-width: 768px) and (max-width: 1023px)");
  const isDesktop = useMediaQuery("(min-width: 1024px)");

  let current = "xl";
  if (isXs) current = "xs";
  else if (isSm) current = "sm";
  else if (isMd) current = "md";
  else if (isLg) current = "lg";

  return {
    isXs,
    isSm,
    isMd,
    isLg,
    isXl,
    isMobile,
    isTablet,
    isDesktop,
    current,
  };
}

export default useMediaQuery;
