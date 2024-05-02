from CustomErrors import InvalidNegativeNumberError
from Enums import FileExtension, SaleStatus
from FinalHelperClass import HelperClass as fhc
from House import House


class Inventory:

    def __init__(self):
        self.__inventory = []  # Keeping as a class attribute in case multiple types in future (e.g., home, commercial)

    def __str__(self):
        string = '\n******************\nCurrent Inventory:\n******************\n\n'
        for house in self.__inventory:
            string += str(house) + '\n'
        return string

    def _add_house_to_inventory(self, house):
        self.__inventory.append(house)

    def _get_inventory(self):
        return self.__inventory

    def _perform_update_action(self, index):
        done = False
        while not done:
            self._display_update_house_options__()
            choice = input('Enter a choice: ').strip().lower()
            if choice == '1':  # square footage
                self._update_square_footage(index)
            elif choice == '2':  # address
                self._update_address(index)
            elif choice == '3':  # city
                self._update_city(index)
            elif choice == '4':  # state
                self._update_state(index)
            elif choice == '5':  # zip
                self._update_zipcode(index)
            elif choice == '6':  # model name
                self._update_model_name(index)
            elif choice == '7':  # sale status
                self._update_sale_status(index)
            else:  # quit
                print('Exiting to main menu...')
                done = True

    def _remove_house_by_id(self, id_to_remove):
        for house in self.__inventory:
            if house.id == id_to_remove:
                self.__inventory.remove(house)
                print(f'House ID {id_to_remove} successfully removed.')
                return
        print(f'House ID {id_to_remove} not found. Nothing removed from Inventory.')

    def _update_square_footage(self, index):
        user_input = input('Enter new square footage in nearest whole number: ').strip()
        valid = fhc.validate_square_footage(user_input)
        if valid:
            self.__inventory[index].set_square_feet(int(user_input))
            print(f'Square footage successfully updated: {self.__inventory[index].get_square_feet()}')
        else:
            print(f'Invalid square footage entered: {user_input}. Try again.')

    def _update_address(self, index):
        user_input = input('Enter new address: ').strip().lower()
        if user_input != '':
            self.__inventory[index].set_address(user_input)
            print(f'Address successfully updated: {self.__inventory[index].get_address()}')
        else:
            print(f'Invalid input entered: `{user_input}`. Try again.')

    def _update_city(self, index):
        user_input = input('Enter new city: ').strip().lower()
        if user_input != '':
            self.__inventory[index].set_city(user_input)
            print(f'City successfully updated: {self.__inventory[index].get_city()}')
        else:
            print(f'Invalid input entered: `{user_input}`. Try again.')

    def _update_state(self, index):
        user_input = self._get_state_from_user('Enter new state: ')
        self.__inventory[index].set_state(user_input)
        print(f'State successfully updated: {self.__inventory[index].get_state()}')

    def _update_zipcode(self, index):
        user_input = input('Enter new zipcode: ')
        if fhc.validate_zipcode(user_input):
            self.__inventory[index].set_zipcode(int(user_input))
            print(f'Zipcode successfully updated: {self.__inventory[index].get_zipcode()}')
        else:
            print(f'Invalid zipcode entered: `{user_input}`. Try again.')

    def _update_model_name(self, index):
        user_input = input('Enter new model name: ').strip().lower()
        if user_input != '':
            self.__inventory[index].set_model_name(user_input)
            print(f'Model name successfully updated: {self.__inventory[index].get_model_name()}')
        else:
            print(f'Invalid input entered: `{user_input}`. Try again.')

    def _update_sale_status(self, index):
        print('Select new status:\n(s): Sold.\n(a): Available.\n(u): Under Contract\n')
        user_input = input('Enter new sale status: ').strip().lower()
        if user_input != '' and user_input in ['s', 'a', 'u']:
            new_status = None
            if user_input == 's':
                new_status = SaleStatus.SOLD
            elif user_input == 'a':
                new_status = SaleStatus.AVAILABLE
            else:
                new_status = SaleStatus.UNDER_CONTRACT
            self.__inventory[index].set_sale_status(new_status)
            print(f'Sale status successfully updated: {self.__inventory[index].get_sale_status()}')
        else:
            print(f'Invalid input entered: `{user_input}`. Try again.')

    @staticmethod
    def _display_update_house_options__():
        print('Update Menu\nEnter the appropriate key to update the attribute.')
        print('\t(1): Square Footage.')
        print('\t(2): Address.')
        print('\t(3): City.')
        print('\t(4): State.')
        print('\t(5): Zipcode.')
        print('\t(6): Model Name')
        print('\t(7): Sale Status')
        print('\t(q): Exit back to Main Menu.\n')

    @staticmethod
    def _get_extension_format(option):
        return FileExtension.CSV.value if option == 'c' else FileExtension.TXT.value

    @staticmethod
    def _get_house_id_from_user(message):
        valid_input = False
        house_id = None
        while not valid_input:
            try:
                house_id_str = input(message).strip().lower()
                if house_id_str == 'q':
                    return -1  # handle negative number to cancel update
                else:
                    house_id = int(house_id_str)
                    valid_input = True
            except InvalidNegativeNumberError as e:
                print(e)
            except ValueError:
                print('Please enter a valid house ID as a whole number.')
        return house_id

    @staticmethod
    def _get_state_from_user(message):
        valid_input = False
        state = None
        while not valid_input:
            state = input(message).strip().lower()
            valid_input = fhc.validate_state(state)
            if not valid_input:
                print('Please enter a valid state (e.g., OR, WA.')
        return state

    @staticmethod
    def _get_string_house_attribute_from_user(message):
        valid_input = False
        value = None
        while not valid_input:
            value = input(message).strip().lower()
            if value == '':
                print('Please enter a value for house attribute.')
            else:
                valid_input = True
        return value

    def add_new_house(self):
        print('Adding a new house. Please provide the following information:')
        model_name = self._get_string_house_attribute_from_user('Model Name: ')
        square_feet = input('Square feet rounded to nearest foot (e.g., 1200): ').strip()  # TODO: add error checking for uint and range (50?, 500000?) & convert to int
        address = self._get_string_house_attribute_from_user('Address: ')
        city = self._get_string_house_attribute_from_user('City: ')
        state = self._get_state_from_user('State (e.g., WA, OR): ')
        zipcode = input('Zipcode (e.g., 97123): ').strip()  # TODO: add error checking for 5 digit int & convert to int
        sale_status = SaleStatus.AVAILABLE
        new_house = House(square_feet, address, city, state, zipcode, model_name, sale_status)
        self._add_house_to_inventory(new_house)
        print(self)

    def display_all_inventory_to_user(self):
        if len(self.__inventory) > 0:
            print('Viewing All Home Inventory...')
            print(self)
        else:
            print('\nWarning: Home Inventory is empty.\n')

    def select_house_to_remove_from_inventory(self):
        if len(self.__inventory) > 0:
            print(f'\nCurrent Inventory: \n{self}\n')
            house_id = self._get_house_id_from_user('Enter a house ID to remove: ')
            if house_id == -1:
                print('Canceling remove operation. Returning to main menu...')
                return
            self._remove_house_by_id(house_id)
        else:
            print('\nWarning: Inventory is empty. Unable to remove a house.\n')

    def select_house_to_modify(self):
        print(f'\nCurrent Inventory: \n{self}\n')
        house_id = self._get_house_id_from_user('Enter a house ID to modify: ')
        if house_id == -1:
            print('Canceling remove operation. Returning to main menu...')
            return
        for house in self.__inventory:
            if house.id == house_id:
                print(f'House Found. Current Attributes:\n{self}\n')
                index = self.__inventory.index(house)
                self._perform_update_action(index)
            else:
                print(f'House not found. Check if ID {house_id} exists in Inventory.')

    def save_inventory_to_text_file(self):
        extension_choice = input('Press `c` for csv format or any other key for text format: ').strip().lower()
        extension = self._get_extension_format(extension_choice)

        if len(self.__inventory) > 0:
            if extension == 'c':
                with open(f'HomeInventoryData.{extension}', 'w') as file:
                    data = 'id,square_feet,address,city,state,zipcode,model_name,sale_status\n'
                    for h in self.__inventory:
                        data += (f'{h.id},{h.get_square_feet()},{h.get_address()},{h.get_city()},{h.get_state()},'
                                 f'{h.get_zipcode()},{h.get_model_name()},{h.get_sale_status()}\n')
                    file.write(data)
            else:
                with open(f'HomeInventoryData.{extension}', 'w') as file:
                    file.write(str(self))
            print(f'Inventory saved to HomeInventoryData.{extension} in {extension.upper()} format.')
        else:
            print('Warning: There is no data to save. Add houses to inventory and try again.')







