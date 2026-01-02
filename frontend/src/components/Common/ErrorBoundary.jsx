import React from 'react'
import PropTypes from 'prop-types'

/**
 * ErrorBoundary Component
 *
 * Catches JavaScript errors in child components and displays a fallback UI.
 * Prevents the entire app from crashing due to errors in a single component.
 *
 * @component
 * @example
 * <ErrorBoundary>
 *   <MyComponent />
 * </ErrorBoundary>
 */
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      hasError: false,
      error: null,
      errorInfo: null,
    }
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI
    return { hasError: true }
  }

  componentDidCatch(error, errorInfo) {
    // Log error details for debugging
    console.error('ErrorBoundary caught an error:', error, errorInfo)

    this.setState({
      error,
      errorInfo,
    })
  }

  handleReset = () => {
    this.setState({
      hasError: false,
      error: null,
      errorInfo: null,
    })
  }

  render() {
    if (this.state.hasError) {
      // Render fallback UI
      return (
        <div
          style={{
            padding: 'var(--spacing-xl)',
            maxWidth: '800px',
            margin: '0 auto',
            textAlign: 'center',
          }}
          role="alert"
          aria-live="assertive"
        >
          <h1 style={{ color: 'var(--color-error)', marginBottom: 'var(--spacing-lg)' }}>
            Oops! Something went wrong
          </h1>

          <p style={{ marginBottom: 'var(--spacing-md)', color: 'var(--color-text-secondary)' }}>
            We encountered an unexpected error. Please try refreshing the page.
          </p>

          <div style={{ display: 'flex', gap: 'var(--spacing-md)', justifyContent: 'center' }}>
            <button
              className="btn btn-primary"
              onClick={() => window.location.reload()}
              aria-label="Reload page"
            >
              Reload Page
            </button>

            <button
              className="btn btn-secondary"
              onClick={this.handleReset}
              aria-label="Try again without reloading"
            >
              Try Again
            </button>
          </div>

          {process.env.NODE_ENV === 'development' && this.state.error && (
            <details
              style={{
                marginTop: 'var(--spacing-xl)',
                textAlign: 'left',
                backgroundColor: 'var(--color-bg-secondary)',
                padding: 'var(--spacing-md)',
                borderRadius: 'var(--border-radius)',
                border: '1px solid var(--color-border)',
              }}
            >
              <summary
                style={{
                  cursor: 'pointer',
                  fontWeight: 600,
                  marginBottom: 'var(--spacing-sm)',
                }}
              >
                Error Details (Development Only)
              </summary>
              <pre
                style={{
                  overflow: 'auto',
                  fontSize: 'var(--font-size-sm)',
                  backgroundColor: '#000',
                  color: '#0f0',
                  padding: 'var(--spacing-sm)',
                  borderRadius: 'var(--border-radius-sm)',
                }}
              >
                {this.state.error.toString()}
                {'\n\n'}
                {this.state.errorInfo?.componentStack}
              </pre>
            </details>
          )}
        </div>
      )
    }

    return this.props.children
  }
}

ErrorBoundary.propTypes = {
  children: PropTypes.node.isRequired,
}

export default ErrorBoundary
