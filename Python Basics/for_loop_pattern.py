""" This program prints a pattern of stars. """
MAX_STARS = 10
TOTAL_LINES = MAX_STARS * 2

for i in range(1, TOTAL_LINES):
    if i <= MAX_STARS:
        print(i * "*")
    else:
        print("*" * (TOTAL_LINES - i))
