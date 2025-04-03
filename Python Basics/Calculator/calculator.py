""" Calculator function """
import os
from art import LOGO


def add(n1, n2):
    """ Function to add """
    return n1 + n2


def subtract(n1, n2):
    """ Function to subtract """
    return n1 - n2


def multiply(n1, n2):
    """ Function to multiply """
    return n1 * n2


def divide(n1, n2):
    """ Function to divide """
    return n1 / n2


operations_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(LOGO)

first_number = float(input("Enter the first number: "))

while True:
    for symbol in operations_dictionary:
        print(symbol)
    operation = input("Pick an operation: ")
    while operation not in ("+", "-", "*", "/"):
        print("That is not a valid option")
        operation = input("Pick an operation: ")
        continue
    next_number = float(input("Enter the second number: "))
    if operation == "/" and next_number == 0:
        print("You cannot divide by 0")
    else:
        output = operations_dictionary[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {output}")
        continue_n1 = input(f"Type 'y' to continue calculating with {output}"
                            f", or type 'n' to start a new calculation: "
                            ).lower()
        if continue_n1 == "y":
            first_number = output
        elif continue_n1 == "n":
            os.system('cls')
            print(LOGO)
            first_number = float(input("Enter the first number: "))
        else:
            print("Goodbye!")
            break
