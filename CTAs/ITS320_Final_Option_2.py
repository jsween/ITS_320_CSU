import sys
from CustomErrors import TooManyAttemptsError
from FinalHelperClass import HelperClass as fhc
from Inventory import Inventory


def display_main_options():
    print('\nMain Menu\nPress the appropriate key for your selection.')
    print('\t(1): Add a new home.')
    print('\t(2): Remove a home.')
    print('\t(3): Update a home.')
    print('\t(4): View all homes.')
    print('\t(5): Save Home Inventory.')
    print('\t(q): Exit program.\n')


def main():
    home_inventory = Inventory()
    print('Welcome to the National Builder system.\nChoose an option to manage the inventory of available houses.')
    user_input = None
    while user_input != "q":
        display_main_options()
        try:
            user_input = fhc.get_user_choice()
            fhc.perform_user_operation(user_input, home_inventory)
        except TooManyAttemptsError as e:
            print(e)
            sys.exit()
        except TypeError as e:
            print(e)


if __name__ == "__main__":
    main()
