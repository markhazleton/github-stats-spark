/**
 * SkipLink Component
 * Provides keyboard navigation shortcuts to bypass repetitive navigation
 * WCAG 2.1 Level A requirement
 */

import React from "react";
import "./SkipLink.css";

export function SkipLink({ href, children }) {
  return (
    <a href={href} className="skip-link">
      {children}
    </a>
  );
}

export default SkipLink;
