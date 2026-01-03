import { useState } from 'react';
import PropTypes from 'prop-types';
import { LanguageBadge } from './LanguageBadge';
import { useGesture, triggerHapticFeedback } from '@/hooks/useGesture';
import './RepositoryCard.css';

/**
 * RepositoryCard Component
 * Mobile-optimized card layout for repository display with swipe-to-delete
 * 
 * @param {Object} props
 * @param {Object} props.repository - Repository data
 * @param {string} props.variant - Display state ('collapsed'|'expanded')
 * @param {boolean} props.selectable - Show selection checkbox
 * @param {boolean} props.selected - Current selection state
 * @param {boolean} props.swipeable - Enable swipe-to-delete
 * @param {Function} props.onSelect - Selection callback
 * @param {Function} props.onExpand - Expansion callback
 * @param {Function} props.onClick - Card click callback
 * @param {Function} props.onDelete - Delete callback (for swipe-to-delete)
 */
export function RepositoryCard({ 
  repository,
  variant = 'collapsed',
  selectable = false,
  selected = false,
  swipeable = false,
  onSelect,
  onExpand,
  onClick,
  onDelete
}) {
  const [isExpanded, setIsExpanded] = useState(variant === 'expanded');
  const [swipeOffset, setSwipeOffset] = useState(0);
  const [showDeleteButton, setShowDeleteButton] = useState(false);

  const handleCardClick = (e) => {
    // Don't trigger if clicking checkbox
    if (e.target.type === 'checkbox') return;
    
    const newExpandedState = !isExpanded;
    setIsExpanded(newExpandedState);
    
    if (onExpand) {
      onExpand(repository.name);
    }
    if (onClick) {
      onClick(repository);
    }
  };

  const handleCheckboxChange = (e) => {
    e.stopPropagation();
    triggerHapticFeedback('light');
    if (onSelect) {
      onSelect(repository.name);
    }
  };

  const handleDelete = () => {
    triggerHapticFeedback('heavy');
    if (onDelete) {
      onDelete(repository.name);
    }
    setShowDeleteButton(false);
    setSwipeOffset(0);
  };

  // Swipe gesture configuration for swipe-to-delete
  const bind = useGesture(
    swipeable
      ? {
          onSwipeLeft: ({ distance }) => {
            if (distance > 100) {
              setShowDeleteButton(true);
              triggerHapticFeedback('medium');
            }
          },
        }
      : {},
    {}
  );

  // Format date to relative time
  const formatDate = (dateString) => {
    if (!dateString) return 'Unknown';
    const date = new Date(dateString);
    const now = new Date();
    const diffDays = Math.floor((now - date) / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return 'Today';
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`;
    if (diffDays < 365) return `${Math.floor(diffDays / 30)} months ago`;
    return `${Math.floor(diffDays / 365)} years ago`;
  };

  const cardClasses = [
    'repository-card',
    isExpanded && 'repository-card-expanded',
    selected && 'repository-card-selected',
    showDeleteButton && 'repository-card-swipe-revealed',
    'interactive-card'
  ].filter(Boolean).join(' ');

  return (
    <div className="repository-card-wrapper">
      {/* Delete button (shown on swipe) */}
      {swipeable && showDeleteButton && (
        <button
          className="repository-card-delete-button"
          onClick={(e) => {
            e.stopPropagation();
            handleDelete();
          }}
          aria-label="Delete repository"
        >
          Delete
        </button>
      )}

      <article 
        {...(swipeable ? bind() : {})}
        className={cardClasses}
        onClick={handleCardClick}
        role="button"
        tabIndex={0}
        onKeyPress={(e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            handleCardClick(e);
          }
        }}
        aria-expanded={isExpanded}
        aria-label={`Repository: ${repository.name}`}
      >
      {/* Collapsed State - Always Visible */}
      <div className="repository-card-header">
        <div className="repository-card-title-row">
          <h3 className="repository-card-title">{repository.name}</h3>
          {selectable && (
            <div className="repository-card-checkbox-wrapper touch-target">
              <input
                type="checkbox"
                checked={selected}
                onChange={handleCheckboxChange}
                onClick={(e) => e.stopPropagation()}
                aria-label={`Select ${repository.name}`}
                className="repository-card-checkbox"
              />
            </div>
          )}
        </div>

        <div className="repository-card-meta">
          {repository.language && (
            <LanguageBadge language={repository.language} size="sm" />
          )}
          
          <div className="repository-card-stats">
            <span className="repository-card-stat" aria-label={`${repository.stars} stars`}>
              ⭐ {repository.stars || 0}
            </span>
            <span className="repository-card-stat" aria-label={`Last commit ${formatDate(repository.lastCommitDate)}`}>
              🕒 {formatDate(repository.lastCommitDate)}
            </span>
          </div>
        </div>
      </div>

      {/* Expanded State - Additional Details */}
      {isExpanded && (
        <div className="repository-card-body">
          {repository.description && (
            <p className="repository-card-description">{repository.description}</p>
          )}

          <div className="repository-card-metrics">
            <div className="repository-card-metric">
              <span className="repository-card-metric-label">Commits</span>
              <span className="repository-card-metric-value">{repository.commits || 0}</span>
            </div>
            <div className="repository-card-metric">
              <span className="repository-card-metric-label">Contributors</span>
              <span className="repository-card-metric-value">{repository.contributors || 0}</span>
            </div>
            <div className="repository-card-metric">
              <span className="repository-card-metric-label">Forks</span>
              <span className="repository-card-metric-value">{repository.forks || 0}</span>
            </div>
          </div>

          {repository.technologies && repository.technologies.length > 0 && (
            <div className="repository-card-technologies">
              <span className="repository-card-section-title">Technologies:</span>
              <div className="repository-card-tech-list">
                {repository.technologies.slice(0, 5).map((tech) => (
                  <span key={tech} className="repository-card-tech-tag">
                    {tech}
                  </span>
                ))}
              </div>
            </div>
          )}

          {repository.commit_history && repository.commit_history.length > 0 && (
            <div className="repository-card-commits">
              <span className="repository-card-section-title">Recent Commits:</span>
              <ul className="repository-card-commit-list">
                {repository.commit_history.slice(0, 3).map((commit, index) => (
                  <li key={index} className="repository-card-commit-item">
                    <span className="repository-card-commit-date">
                      {formatDate(commit.date)}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}

      {/* Expand/Collapse Indicator */}
      <div className="repository-card-expand-indicator" aria-hidden="true">
        {isExpanded ? '▲' : '▼'}
      </div>
    </article>
  </div>
  );
}

RepositoryCard.propTypes = {
  repository: PropTypes.shape({
    name: PropTypes.string.isRequired,
    language: PropTypes.string,
    stars: PropTypes.number,
    updated_at: PropTypes.string,
    description: PropTypes.string,
    commits: PropTypes.number,
    contributors: PropTypes.number,
    forks: PropTypes.number,
    technologies: PropTypes.arrayOf(PropTypes.string),
    commit_history: PropTypes.arrayOf(PropTypes.shape({
      date: PropTypes.string
    }))
  }).isRequired,
  variant: PropTypes.oneOf(['collapsed', 'expanded']),
  selectable: PropTypes.bool,
  selected: PropTypes.bool,
  swipeable: PropTypes.bool,
  onSelect: PropTypes.func,
  onExpand: PropTypes.func,
  onClick: PropTypes.func,
  onDelete: PropTypes.func,
};

export default RepositoryCard;
