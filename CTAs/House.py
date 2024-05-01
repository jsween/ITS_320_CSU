class House:
    __next_id = 1

    def __init__(self, square_feet, address, city, state, zipcode, model_name, sale_status):
        self.id = House.__next_id
        House.__next_id += 1

        self.__square_feet = square_feet
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__model_name = model_name
        self.__sale_status = sale_status

    def get_square_feet(self):
        return self.__square_feet

    def set_square_feet(self, value):
        self.__square_feet = value

    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value

    def get_city(self):
        return self.__city

    def set_city(self, value):
        self.__city = value

    def get_state(self):
        return self.__state

    def set_state(self, value):
        self.__state = value

    def get_zipcode(self):
        return self.__zipcode

    def set_zipcode(self, value):
        self.__zipcode = value

    def get_model_name(self):
        return self.__model_name

    def set_model_name(self, value):
        self.__model_name = value

    def get_sale_status(self):
        return self.__sale_status

    def set_sale_status(self, value):
        self.__sale_status = value

    def __str__(self):
        return (f'House ID: {self.id}\n'
                f'Square Feet: {self.__square_feet}\n'
                f'Address: {self.__address}\n'
                f'City: {self.__city}\n'
                f'State: {self.__state}\n'
                f'Zip: {self.__zipcode}\n'
                f'Model name: {self.__model_name}\n'
                f'Sale status: {self.__sale_status.value.capitalize()}\n')
