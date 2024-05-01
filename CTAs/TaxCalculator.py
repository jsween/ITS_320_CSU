from sys import maxsize


class TaxCalculator:
    """ Tax Calculator """

    # dictionary to store current tax rates
    tax_rates_dict = {
        'ten_percent': [0, 500],
        'fifteen_percent': [500, 1_000],
        'twenty_percent': [1_000, 2_500],
        'thirty_percent': [2_500, maxsize]
    }

    def calculate_tax_rate(self, income):
        """
        Calculates the tax rate based on the user's weekly income
        :param income: int - user's weekly income
        :return: float - user's tax rate
        """
        # an if-else block to return the user's tax rate dependent on the weekly income
        # check max bracket only because this approach is shorter than
        # if income >= tax_dict['ten_percent'][0] and income < tax_dict['ten_percent'][1]
        # elif income >= tax_dict['fifteen_percent'][0] and  income < tax_dict['fifteen_percent'][1]:
        if income < self.tax_rates_dict['ten_percent'][1]:
            return 0.10
        elif income < self.tax_rates_dict['fifteen_percent'][1]:
            return 0.15
        elif income < self.tax_rates_dict['twenty_percent'][1]:
            return 0.20
        elif income < self.tax_rates_dict['thirty_percent'][1]:
            return 0.3
        else:
            print(f'Wow! Why do you even care about taxes with a weekly income of ${income:,.0f}?')
            return 0.5

    @staticmethod
    def calculate_weekly_taxes(cust_dict):
        """
        Calculates the tax rate based on the user's weekly income
        :param cust_dict: dict - user's tax information
        returns: tuple (float, float) - user's weekly tax rate and weekly net income
        """
        weekly_taxes = cust_dict['tax_rate'] * cust_dict['gross_weekly_income']
        net_weekly_income = cust_dict['gross_weekly_income'] - weekly_taxes
        return weekly_taxes, net_weekly_income
