# Is User Input Valid: Bool
valid_input = False
# User Input Variables
input1 = None
input2 = None

# Loop until valid input
while not valid_input:
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    # check if input is an integer
    valid_input = input1.isdigit() and input2.isdigit()
    if not valid_input:
        print(f"Please enter valid integer numbers.\nYou entered ({input1}, {input2})")
    else:
        input1 = int(input1)
        input2 = int(input2)
# output results
print(f"\nInteger Division: {input1} // {input2} = {input1 // input2}")
print(f"Float Division: {input1} / {input2} = {input1 / input2}")
print(f"Modulus: {input1} % {input2} = {input1 % input2}")

