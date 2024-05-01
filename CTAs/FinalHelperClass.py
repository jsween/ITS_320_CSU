import sys
from CustomErrors import TooManyAttemptsError


class HelperClass:
    """Helper Class provides functionality to validate user input and display to user"""
    @staticmethod
    def get_user_choice():
        valid_choices = ['1', '2', '3', '4', '5']
        valid_input = False
        attempts_left = 5

        while not valid_input and attempts_left > 0:
            user_input = input('Enter your choice: ')
            if user_input == 'q':
                sys.exit('Thank you for using National Builder. Exiting program...')
            elif user_input in valid_choices:
                return user_input
            elif attempts_left > 1:
                print('Invalid input. Please try again.')
            attempts_left -= 1

        raise TooManyAttemptsError(
            'Maximum number of errors reached. Any changes will not be saved. Exiting Program...')

    @staticmethod
    def perform_user_operation(choice, home_inventory):
        """
        Performs the appropriate operation for user input
        :param choice: (str) The choice to perform
        :param home_inventory: (list[House]) The home inventory
        """
        if choice == '1':  # add a new house
            home_inventory.add_new_house()
        elif choice == '2':  # remove a house
            home_inventory.select_house_to_remove_from_inventory()
        elif choice == '3':  # update a house
            home_inventory.select_house_to_modify()
        elif choice == '4':  # display all
            home_inventory.display_all_inventory_to_user()
        elif choice == '5':  # save to file
            home_inventory.save_inventory_to_text_file()
        else:
            raise TypeError(f'Unknown Type: Invalid choice reached perform_user_operation({choice}). Please try again.')

    @staticmethod
    def validate_square_footage(square_footage):
        """
        Validates user inputted square footage.
        :param square_footage: User input to validate.
        :return: (bool) True or False if user entered a valid square footage value.
        """
        if square_footage == '':
            return False
        try:
            return 0 < int(square_footage) < 200_000
        except ValueError:
            return False

    @staticmethod
    def validate_zipcode(zipcode):
        if len(zipcode) != 5:
            return False
        try:
            int(zipcode)
            return True
        except ValueError:
            return False







