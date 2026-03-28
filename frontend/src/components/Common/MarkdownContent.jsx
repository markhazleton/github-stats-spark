import PropTypes from "prop-types";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import styles from "./MarkdownContent.module.css";

function MarkdownContent({ content, className = "" }) {
  if (!content) {
    return null;
  }

  const mergedClassName = className
    ? `${styles.markdown} ${className}`
    : styles.markdown;

  return (
    <div className={mergedClassName}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ ...props }) => (
            <a {...props} target="_blank" rel="noopener noreferrer" />
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}

MarkdownContent.propTypes = {
  content: PropTypes.string,
  className: PropTypes.string,
};

export default MarkdownContent;
