from HelperClass import HelperClass
from TaxCalculator import TaxCalculator
# instantiate dictionary to store tax rate and weekly income information

# is user input valid
valid_input = False
# dictionary to store customer tax information
customer_taxes_dict = {
    'tax_rate': None,
    'gross_weekly_income': None,
    'weekly_taxes_paid': None,
    'net_weekly_income': None,
}


def display_tax_dict(cust_dict):
    """
    Display the customer tax information in a user-friendly format
    """
    print(f'\nEstimated Tax Rate: {round(customer_taxes_dict['tax_rate']*100)}%\n')
    print('****** Weekly Estimated Income ******')
    print(f'\nGross Income: ${round(cust_dict['gross_weekly_income']):,.0f}')
    print(f'Net Income: ${round(customer_taxes_dict['net_weekly_income']):,.0f}')
    print(f'Taxes: ${round(customer_taxes_dict['weekly_taxes_paid']):,.0f}')
    print('\n****** Annual Estimated Income ******')
    print(f'\nGross Income: ${round(cust_dict['gross_weekly_income'] * 52):,.0f}')
    print(f'Net Income: ${round(customer_taxes_dict['net_weekly_income'] * 52):,.0f}')
    print(f'Total Taxes: ${round(customer_taxes_dict['weekly_taxes_paid'] * 52):,.0f}')


# while input not validated or valid
while not valid_input:
    # string input after stripping commas and dollar signs
    user_input = (input("Enter your estimated weekly income (ex. 1000): ").replace(",", "")
                  .replace("$", ""))
    # check if input is valid
    valid_input = HelperClass.validate_input_is_numeric_and_positive(user_input)
    # if invalid ask display error message to user
    if not valid_input:
        print("Unable to parse your estimated annual income. Please try again as a whole number >= 0.")
    # safely convert the input to a float
    else:
        customer_taxes_dict['gross_weekly_income'] = float(user_input)  # safe to convert
calculator = TaxCalculator()  # instantiate a tax calculator
customer_taxes_dict['tax_rate'] = calculator.calculate_tax_rate(customer_taxes_dict['gross_weekly_income'])  # get user's tax rate
customer_taxes_dict['weekly_taxes_paid'], customer_taxes_dict['net_weekly_income'] = (
    TaxCalculator.calculate_weekly_taxes(customer_taxes_dict))  # get customer's weekly taxes and income
display_tax_dict(customer_taxes_dict)  # display pay information in user-friendly format

