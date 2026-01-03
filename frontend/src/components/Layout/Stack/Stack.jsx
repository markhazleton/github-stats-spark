import PropTypes from "prop-types";
import "./Stack.css";

/**
 * Stack Component
 * Flexible layout for vertical/horizontal spacing with mobile-friendly gaps
 *
 * @param {Object} props
 * @param {React.ReactNode} props.children - Content to stack
 * @param {string} props.direction - Stack direction ('vertical'|'horizontal')
 * @param {number} props.spacing - Gap between items in pixels
 * @param {string} props.align - Alignment ('start'|'center'|'end'|'stretch')
 * @param {string} props.justify - Justification ('start'|'center'|'end'|'space-between'|'space-around')
 * @param {string} props.className - Additional CSS classes
 */
export function Stack({
  children,
  direction = "vertical",
  spacing = 16,
  align = "stretch",
  justify = "start",
  className = "",
}) {
  const style = {
    "--stack-spacing": `${spacing}px`,
  };

  const classes = [
    "stack",
    `stack-${direction}`,
    `stack-align-${align}`,
    `stack-justify-${justify}`,
    className,
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <div className={classes} style={style}>
      {children}
    </div>
  );
}

Stack.propTypes = {
  children: PropTypes.node.isRequired,
  direction: PropTypes.oneOf(["vertical", "horizontal"]),
  spacing: PropTypes.number,
  align: PropTypes.oneOf(["start", "center", "end", "stretch"]),
  justify: PropTypes.oneOf([
    "start",
    "center",
    "end",
    "space-between",
    "space-around",
  ]),
  className: PropTypes.string,
};

export default Stack;
