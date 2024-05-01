class TooManyAttemptsError(Exception):
    def __init__(self, message="Too many failed attempts."):
        self.message = message
        super().__init__(self.message)
