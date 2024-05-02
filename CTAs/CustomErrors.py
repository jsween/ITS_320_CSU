class TooManyAttemptsError(Exception):
    """
    Raised when a user attempts to run out of attempts.
    """
    def __init__(self, message="Too many failed attempts."):
        self.message = message
        super().__init__(self.message)


class InvalidNegativeNumberError(Exception):
    """
    Raised when a user attempts to enter a negative number when not allowed.
    """
    def __init__(self, message="Invalid negative number."):
        self.message = message
        super().__init__(self.message)