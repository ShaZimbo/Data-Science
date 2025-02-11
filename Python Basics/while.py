""" This program will take a number inputted and add it to a total sum.
The program will also keep track of how many numbers have been inputted.
The program will then output the average of the numbers inputted.
The program will continue to ask for numbers until the user inputs -1. """

COUNTER = 0
NUMBER = 0

user_input = int(input("Please enter a number (-1 to exit): "))

# If the number inputted is not -1
while NUMBER != -1:
    if user_input != -1:
        NUMBER += user_input
        COUNTER += 1
        user_input = int(input("Please enter a number (-1 to exit): "))

# If the number inputted is -1
    else:
        print(round(NUMBER / COUNTER, 2))
        break
