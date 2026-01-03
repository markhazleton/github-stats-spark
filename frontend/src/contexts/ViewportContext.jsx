import { createContext, useContext, useState, useEffect } from "react";
import PropTypes from "prop-types";

const ViewportContext = createContext(null);

/**
 * Viewport Context Provider
 * Tracks current breakpoint, dimensions, and device orientation
 */
export function ViewportProvider({ children }) {
  const [viewport, setViewport] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
    breakpoint: getBreakpoint(window.innerWidth),
    isMobile: window.innerWidth < 768,
    isTablet: window.innerWidth >= 768 && window.innerWidth < 1024,
    isDesktop: window.innerWidth >= 1024,
    orientation:
      window.innerWidth > window.innerHeight ? "landscape" : "portrait",
  });

  useEffect(() => {
    const handleResize = () => {
      const width = window.innerWidth;
      const height = window.innerHeight;

      setViewport({
        width,
        height,
        breakpoint: getBreakpoint(width),
        isMobile: width < 768,
        isTablet: width >= 768 && width < 1024,
        isDesktop: width >= 1024,
        orientation: width > height ? "landscape" : "portrait",
      });
    };

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <ViewportContext.Provider value={viewport}>
      {children}
    </ViewportContext.Provider>
  );
}

ViewportProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

/**
 * Hook to access viewport context
 */
export function useViewport() {
  const context = useContext(ViewportContext);
  if (!context) {
    throw new Error("useViewport must be used within ViewportProvider");
  }
  return context;
}

/**
 * Get breakpoint name from width
 */
function getBreakpoint(width) {
  if (width < 320) return "xs";
  if (width < 768) return "sm";
  if (width < 1024) return "md";
  if (width < 1280) return "lg";
  return "xl";
}

export default ViewportContext;
