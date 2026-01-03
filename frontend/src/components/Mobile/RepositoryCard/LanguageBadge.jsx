import PropTypes from "prop-types";
import "./LanguageBadge.css";

/**
 * LanguageBadge Component
 * Displays primary programming language with color coding
 *
 * @param {Object} props
 * @param {string} props.language - Programming language name
 * @param {string} props.size - Badge size ('sm'|'md'|'lg')
 * @param {string} props.className - Additional CSS classes
 */
export function LanguageBadge({ language, size = "md", className = "" }) {
  if (!language) return null;

  const classes = [
    "language-badge",
    `language-badge-${size}`,
    `language-${language.toLowerCase().replace(/[^a-z0-9]/g, "-")}`,
    className,
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <span className={classes} aria-label={`Programming language: ${language}`}>
      {language}
    </span>
  );
}

LanguageBadge.propTypes = {
  language: PropTypes.string.isRequired,
  size: PropTypes.oneOf(["sm", "md", "lg"]),
  className: PropTypes.string,
};

export default LanguageBadge;
