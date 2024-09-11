class InvalidTaskTypeException(Exception):
    """Exception raised for invalid task types."""
    pass


class TaskNotFoundException(Exception):
    """Exception raised when task is not found."""
    pass
