import sys
from CustomErrors import TooManyAttemptsError
from Inventory import Inventory


def display_main_options():
    print('\nPress the appropriate key for your selection.')
    print('\t1: Add a new home.')
    print('\t2: Remove a home.')
    print('\t3: Update a home.')
    print('\t4: View all homes.')
    print('\t5: Save Home Inventory.')
    print('\tq: Exit program.')


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

    raise TooManyAttemptsError('Maximum number of errors reached. Any changes will not be saved. Exiting Program...')


def perform_user_operation(choice, home_inventory):
    if choice == '1':
        home_inventory.add_new_house()
    elif choice == '2':
        print('Removing a home...')
        home_inventory.select_house_to_remove_from_inventory()
    elif choice == '3':
        print('Updating a home...')
        raise NotImplementedError()
    elif choice == '4':
        home_inventory.display_all_inventory_to_user()
    elif choice == '5':
        home_inventory.save_inventory_to_text_file()
    else:
        raise TypeError(f'Unknown Type: Invalid choice reached perform_user_operation({choice}). Please try again.')


def main():
    home_inventory = Inventory()
    print('Welcome to the National Builder system.\nChoose an option to manage the inventory of available houses.')
    user_input = None
    while user_input != "q":
        display_main_options()
        try:
            user_input = get_user_choice()
            perform_user_operation(user_input, home_inventory)
        except TooManyAttemptsError as e:
            print(e)
            sys.exit()
        except TypeError as e:
            print(e)


if __name__ == "__main__":
    main()
