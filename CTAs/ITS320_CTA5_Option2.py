def get_three_strings():
    """
    Prompts the user for three strings

    Returns:
        list[string]: A list of three strings
    """
    three_strings = []  # an empty list to store the values
    for i in range(1, 4):  # 1-3
        three_strings.append(input(f'Enter string {i}: ').strip()) # remove any extra spaces before returning
    return three_strings


def generate_final_string(three_strings):
    """
    Generates the final string to be displayed to the user.

    Args:
        three_strings (list[string]): A list of three strings from the user

    Returns:
        string: The first 2 strings followed by the 3rd string reversed
    """
    return three_strings[0] + three_strings[1] + three_strings[2][::-1]  # reverses the last string


def main():
    """
    Main Function of the program
    """
    three_strings = get_three_strings()  # get the 3 strings from the user
    print(generate_final_string(three_strings))  # display them to the user


if __name__ == "__main__":
    main()
