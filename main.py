"""
Title: Calculator
Author: Michał Chojna
Date: 10.06.2022
Description: Calculator to add, subtract, multiply and divide
"""

# Imports modules
import art


# Defines function
def calculation(number_1, number_2, operator):
    """
    Function takes the first number given by a user, takes the second number given by a user, takes type of operation (+ for addition, - for subtraction, * for multiplication, / for division) given by a user
    Function returns result of the equation
    """

    # Checks if the type of the operation given by a user is addition
    if operator == "+":

        # If the type of the operation given by a user is addition
        # Performs addition and returns the result
        result = number_1 + number_2

    # Checks if the type of the operation given by a user is subtraction
    elif operator == "-":

        # If the type of the operation given by a user is subtraction
        # Performs subtraction and returns the result
        result = number_1 - number_2

    # Checks if the type of the operation given by a user is multiplication
    elif operator == "*":

        # If the type of the operation given by a user is multiplication
        # Performs multiplication and returns the result
        result = number_1 * number_2

    # Checks if the type of the operation given by a user is division
    elif operator == "/":

        # If the type of the operation given by a user is division
        # Performs division and returns the result
        result = number_1 / number_2

    return result


# Prints welcome logo
print(art.logo)

# Creates string for checking the next calculation with the last result
again = "no"

# Creates integer to storage result of the calculation
result = 0

# Boolean initializes Calculator
calculator = True

# While loop initializes Calculator
while calculator:

    # Checks if the answer to perform next calculation with the last result is no
    if again.lower() == "no":

        # If the answer to perform next calculation with the last result is no
        # Takes the first number given by a user
        first_number = float(input("What is the first number? "))

    else:

        # If the answer to perform next calculation with the last result is yes
        # Imputes the last result to the first number
        first_number = result

    # While loop to check the type of the operation given by a user
    while True:

        # Takes the type of the operation given by a user
        operation = input("Pick an operation ('+', '-', '*', '/'): ")

        # Checks if the type of the operation given by a user is correct
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":

            # If the type of the operation given by a user is correct
            # Breaks the loop
            break

    # While loop to check if the second number given by a user is correct
    while True:

        # Takes the second number given by a user
        second_number = float(input("What is the second number? "))

        # Checks if the second number given by a user is 0
        # And
        # Checks if the type of operation given by user is division
        if second_number == 0 and operation == "/":

            # If the second number given by a user is 0 and if the type of operation given by user is division
            # Prints that it is not possible
            print("Division by 0 is not possible!")
        else:

            # If the second number given by a user is not 0 and if the type of operation given by user is not division
            # Breaks the loop
            break

    # Initializes "calculation" function with argument given by a user
    result = calculation(first_number, second_number, operation)

    # Prints the equation and the result of the equation
    print(f"{first_number} {operation} {second_number} = {result}")

    # While loop checks if the user wants to perform next calculation with the current result
    while True:

        # Takes the answer if the user wants to perform next calculation with the current result
        again = input(f"Type 'yes' if you want continue calculating with {result}. Otherwise type 'no'. If you want "
                      f"to exit the program type 'exit'. ")

        # Checks if the answer to the question if the user wants to perform next calculation with the current result or to exit is correct
        if again.lower() == "yes" or again.lower() == "no" or again.lower() == "exit":

            # If the answer to the question if the user wants to perform next calculation with the current result or to exit is correct
            # Breaks the loop
            break

    # Checks if the answer to the question if the user wants to perform next calculation with the current  result or to exit is exit
    if again.lower() == "exit":

        # If the answer to the question if the user wants to perform next calculation with the current  result or to exit is exit

        # Exit the while loop
        calculator = False

        # Breaks the loop
        break
