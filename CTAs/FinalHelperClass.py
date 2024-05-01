class HelperClass:
    """Helper Class provides functionality to validate user input and display to user"""
    @staticmethod
    def validate_square_footage_valid(square_footage):
        try:
            return 0 < int(square_footage) < 200_000
        except ValueError:
            return False







