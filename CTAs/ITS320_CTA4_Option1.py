from HelperClass import HelperClass
# initialize a list to store the user's numbers
numbers = []
# create a named tuple to store if input is valid bool and the float value
print('Enter 5 Numbers')
# run the code block 5x
for i in range(0, 5):
    valid_input = False  # assume input is false
    while not valid_input:  # while loop until each number is verified
        user_num_str = input(f' * Number {i+1}: ')  # store initial input as a string
        valid_input, float_value = HelperClass.validate_input_float(user_num_str)  # get bool if float/int or not and value
        if not valid_input:  # if not a float/int
            print(f'Invalid input `{user_num_str}`, please enter a whole or decimal number.')
        else:  # is float/int
            numbers.append(float_value)

# initialize dict
cta4_dict = {
    'total': 0,
    'avg': 0,
    'max': numbers[0],  # use first number in case all values are < 0
    'min': numbers[0],  # use first number in case all values are > 0
    'interest': 0
}
rate = 0.2  # interest rate
# calculate each dictionary stat with for loop
for num in numbers:
    cta4_dict['total'] += num
    cta4_dict['avg'] = cta4_dict['total'] / len(numbers)
    cta4_dict['max'] = max(cta4_dict['max'], num)
    cta4_dict['min'] = min(cta4_dict['min'], num)
    cta4_dict['interest'] += num * rate

if cta4_dict['interest'] < 0:
    cta4_dict['interest'] = 0  # assuming interest is never negative

print(f'\nYou Entered: {numbers}\n')
# for loop through key-value pairs in dictionary
for key, value in cta4_dict.items():
    print(f'{key}: {round(value, 2)}')

print(f'Interest calculated with a rate of {rate * 100}%')
print(f'Total with Interest: {round(cta4_dict["interest"] + cta4_dict["total"], 2)}')
