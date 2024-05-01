from Enums import FileExtension, SaleStatus
from House import House


class Inventory:

    def __init__(self):
        self.inventory = []  # Keeping as a class attribute in case multiple types in future (e.g., home, commercial)

    def __str__(self):
        string = '\n******************\nCurrent Inventory:\n******************\n\n'
        for house in self.inventory:
            string += str(house) + '\n'
        return string

    def __add_house_to_inventory__(self, house):
        self.inventory.append(house)

    def __remove_house_from_inventory__(self, house):
        self.inventory.remove(house)

    @staticmethod
    def __get_extension_format(option):
        return FileExtension.CSV.value if option == 'c' else FileExtension.TXT.value

    def __get_inventory__(self):
        return self.inventory

    def __remove_house_by_id__(self, id_to_remove):
        for house in self.inventory:
            if house.id == id_to_remove:
                self.inventory.remove(house)
                print(f'House ID {id_to_remove} successfully removed.')
                return
        print(f'House ID {id_to_remove} not found. Nothing removed from Inventory.')

    def add_new_house(self):
        print('Adding a new house. Please provide the following information:')
        model_name = input('Model Name: ').strip()  # TODO: for all strings, add method to check if empty
        square_feet = input('Square feet: ').strip()  # TODO: add error checking for uint and range (50?, 500000?) & convert to int
        address = input('Street Address: ').strip()
        city = input('City: ').strip()
        state = input('State: ').strip()
        zip_code = input('Zip Code: ').strip()  # TODO: add error checking for 5 digit int & convert to int
        sale_status = SaleStatus.AVAILABLE
        new_house = House(model_name, square_feet, address, city, state, zip_code, sale_status)
        self.__add_house_to_inventory__(new_house)
        print(self)

    def display_all_inventory_to_user(self):
        if len(self.inventory) > 0:
            print('Viewing All Home Inventory...')
            print(self)
        else:
            print('\nWarning: Home Inventory is empty.\n')

    def select_house_to_remove_from_inventory(self):
        print(f'\nCurrent Inventory: \n{self}\n')
        house_id = int(input('Enter a house ID to remove: '))  # TODO: add check if 'c' to cancel or if int
        self.__remove_house_by_id__(house_id)

    def save_inventory_to_text_file(self):

        extension_choice = input('Press `c` for csv format or any other key for text format: ').strip().lower()

        extension = self.__get_extension_format(extension_choice)

        if len(self.inventory) > 0:
            if extension == 'c':
                with open(f'HomeInventoryData.{extension}', 'w') as file:
                    data = 'id,square_feet,address,city,state,zipcode,model_name,sale_status\n'
                    for h in self.inventory:
                        data += (f'{h.id},{h.get_square_feet()},{h.get_address()},{h.get_city()},{h.get_state()},'
                                 f'{h.get_zipcode()},{h.get_model_name()},{h.get_sale_status()}\n')
                    file.write(data)
            else:
                with open(f'HomeInventoryData.{extension}', 'w') as file:
                    file.write(str(self))
            print(f'Inventory saved to HomeInventoryData.{extension} in {extension.upper()} format.')
        else:
            print('Warning: There is no data to save. Add houses to inventory and try again.')







