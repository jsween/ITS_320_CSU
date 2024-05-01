from HelperClass import HelperClass as hc


class CTA6:
    """
    Compute the Cartesian Product of 2 User Supplied Lists
    """
    def __init__(self):
        """
        Constructor
        """
        self._dict_A = {'length': 0, 'list': []}
        self._dict_B = {'length': 0, 'list': []}
        self.cartesian_product = []

    def find_cartesian_product(self):
        """
        Find the Cartesian Product of 2 User Supplied Lists
        """
        print('Greetings! Let\'s find the cartesian product for your lists.')
        self._dict_A['length'] = self._get_lists_length('First')
        self._dict_B['length'] = self._get_lists_length('Second')
        self._ask_for_lists_from_user()
        for a in self._dict_A.get('list', []):
            for b in self._dict_B.get('list', []):
                self.cartesian_product.append((a, b))

    @staticmethod
    def _get_lists_length(order):
        """
        Get the Length of the List
        """
        valid_input = False
        list_length_str = None
        while not valid_input:
            list_length_str = input(f'Enter the {order} list length (1-10): ')
            valid_input = hc.validate_input_is_digit_and_between_one_and_ten(list_length_str)
            if not valid_input:
                print('Invalid input. Please enter a number between 1 and 10.')

        return int(list_length_str)

    def _ask_for_lists_from_user(self):
        """
        Get the lists from the user and set them to the CTA class
        """
        print('Note: When entering values, use whole numbers. Decimals will be converted to integer values.')
        print('Enter the First List:')
        self._dict_A['list'] = self._get_list_from_user(self._dict_A['length'])
        print('Enter the Second List:')
        self._dict_B['list'] = self._get_list_from_user(self._dict_B['length'])

    @staticmethod
    def _get_list_from_user(length):
        """
        Get the length of the lists from the user
        :param length: (int) The length of the list
        """
        temp_list = []
        for i in range(1, length + 1):
            valid_input = False
            while not valid_input:
                input_str = input(f'{i}: ')
                valid_input = hc.validate_input_is_integer(input_str)
                if not valid_input:
                    print('Invalid input. Please enter a whole number (ex. 5)')
                else:
                    temp_list.append(int(input_str))
        return temp_list

    def display_cartesian_product(self):
        """
        Display the cartesian product to user
        """
        print(f'{self._dict_A['list']} X {self._dict_B['list']} = {self.cartesian_product}')


if __name__ == '__main__':
    cta6 = CTA6()
    cta6.find_cartesian_product()
    cta6.display_cartesian_product()

