class TooManyAttemptsError(Exception):
    def __init__(self, message="Too many failed attempts."):
        self.message = message
        super().__init__(self.message)


class InvalidNegativeNumberError(Exception):
    def __init__(self, message="Invalid negative number."):
        self.message = message
        super().__init__(self.message)