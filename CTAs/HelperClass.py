class HelperClass:
    """Helper Class provides functionality to validate user input and display to user"""
    @staticmethod
    def validate_input_float(val):
        """
        Validates the user input and returns boolean value if a valid float or not
        :param val: (string) user input to be converted
        :return: (boolean, float) if data is valid or not and float (-1 if exception raised)
        """
        # check if valid data type
        try:
            # return true if cast to float is successful
            return True, float(val)
        # catch ValueError if alpha characters exist and return false
        except ValueError:
            return False, -1

    @staticmethod
    def display(dictionary):
        """Displays the Cars Dictionary to the User
        :param dictionary: (dictionary) Car dictionary"""
        # Loop through each car by id
        for car, value in dictionary.items():
            print()
            for key, val in value.items():
                # print the key value pairs
                print(f'{key}: {val}')

    @staticmethod
    def get_valid_input(car_prompt, data_type):
        """
        Gets valid input from the user
        :param car_prompt: (str) Displays prompt for the user
        :param data_type: (type) Expected type of data
        :return: (any) Expected data
        """
        # get user input
        user_input = input(car_prompt)
        # check if user input is valid the first time
        valid = HelperClass.validate_input(user_input, data_type)
        # if input is invalid, repeat until valid input is received
        while not valid:
            print("Incorrect input. Please try again.")
            # get the user input again
            user_input = input(car_prompt)
            # check if the input is valid
            valid = HelperClass.validate_input(user_input, data_type)
        # convert the data to appropriate data type
        user_input = HelperClass.convert_data(user_input, data_type)

        return user_input

    @staticmethod
    def convert_data(val, dt):
        """
        Converts or formats data to appropriate format
        :param val: (string) Value to be converted
        :param dt:  (any) Expected type of data
        :return: (any) Converted/formatted data
        """
        if dt == int:
            return int(val)
        elif dt == float:
            return float(val)
        elif dt == str:
            # title case the make/model
            return val.title()

    @staticmethod
    def validate_input(value, data_type):
        """
        Validates the user input and returns boolean value if valid or not
        :param value: (string) user input to be converted
        :param data_type: (type) desired data type
        :return: (boolean) if data is valid or not
        """
        # check if valid data type
        if data_type == int:
            # return true if value is an integer and >= 0
            return value.isdigit() and int(value) >= 0
        elif data_type == float:
            try:
                # return true if cast to float is successful and >= 0
                float(value)
                return float(value) >= 0
            # catch ValueError if alpha characters exist and return false
            except ValueError:
                return False
        else:
            # make sure string is not empty
            return len(value) > 0

    @staticmethod
    def validate_input_is_numeric_and_positive(value):
        """
        Validates the user input and returns boolean value if valid or not
        :param value: (string) user input to be converted
        :return: (boolean) if data is valid or not
        """
        # check if valid data type
        try:
            # return true if cast to float is successful and >= 0
            float(value)
            return float(value) >= 0, float(value)
        # catch ValueError if alpha characters exist and return false
        except ValueError:
            return False

    @staticmethod
    def validate_input_is_digit_and_between_one_and_ten(value):
        """
        Validates the user input is an integer between [1, 10]
        :param value: (string) user input to be checked
        :return: (boolean) if value is integer between [1, 10]
        """
        is_digit = value.isdigit()
        if is_digit:
            return 1 <= int(value) < 11
        else:
            return False

    @staticmethod
    def validate_input_is_integer(value):
        """
        Validates the user input is an integer
        :param value: (str) Value to be checked
        :return: (boolean) if value is an integer or not
        """
        try:
            int(value)
            return True
        except ValueError:
            return False




































