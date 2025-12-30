"""Custom exceptions for Stats Spark workflow errors."""

from typing import Optional


class WorkflowError(Exception):
    """Raised when a critical workflow stage fails.

    This exception indicates a failure that should halt workflow execution,
    typically used for required stages like GitHub API data fetching or
    report file generation.

    Attributes:
        message: Human-readable error description
        stage: Name of the workflow stage where the error occurred
        cause: Optional underlying exception that triggered this error
    """

    def __init__(
        self,
        message: str,
        stage: str = "unknown",
        cause: Optional[Exception] = None
    ):
        """Initialize workflow error with context.

        Args:
            message: Description of what went wrong
            stage: Which workflow stage failed (e.g., "fetch_github_data")
            cause: Original exception if this is wrapping another error
        """
        super().__init__(message)
        self.message = message
        self.stage = stage
        self.cause = cause

    def __str__(self) -> str:
        """Format error message with stage and cause context.

        Returns:
            Formatted error string like "[stage] message (caused by ExceptionType)"
        """
        cause_info = f" (caused by {type(self.cause).__name__})" if self.cause else ""
        return f"[{self.stage}] {self.message}{cause_info}"
