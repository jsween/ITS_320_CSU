import datetime
from HelperClass import HelperClass as hc

should_quit = False
# empty dictionary to store multiple cars
cars = {}
# id of the cars to add to the dictionary
car_id = 0
# while user does not want to quit
while not should_quit:
    # increment the id by 1
    car_id += 1
    # new car dictionary object (a class could have also worked here)
    new_car = {'make': hc.get_valid_input('Enter car make: ', str),
               'model': hc.get_valid_input('Enter car model: ', str),
               'year': hc.get_valid_input(f'Enter car year year (1908-{datetime.datetime.now().year + 1}): '
                                          , int),
               'odometer_start': hc.get_valid_input('Enter starting odometer reading (0-999999): ', int),
               'odometer_end': hc.get_valid_input('Enter final odometer reading (0-999999): ', int),
               'miles_per_gallon': hc.get_valid_input('Enter estimated miles per gallon (ex. 32.5): ', float)}
    # add new car by car ID
    cars[car_id] = new_car
    # ask user if they want to quit
    should_quit = str.lower(input('Do you want to add another car? (y/n) ')) == 'n'
# Display all cars to user
hc.display(cars)


