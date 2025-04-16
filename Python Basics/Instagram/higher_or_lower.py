""" Higher or Lower game using instagram followers """
import os
import random
from insta import insta
from art import LOGO, VS

print(LOGO)
compare_a = random.choice(insta)
SCORE = 0
CONTINUE_PLAY = True
while CONTINUE_PLAY is True:
    print(f"Compare A: {compare_a['owner']}, "
          f"a {compare_a['profession']}, "
          f"from {compare_a['country']}")
    print(VS)
    compare_b = random.choice(insta)
    while compare_a == compare_b:
        compare_b = random.choice(insta)
    print(f"Against B: {compare_b['owner']}, "
          f"a {compare_b['profession']}, "
          f"from {compare_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    os.system('cls')

    if guess == "A":
        if compare_a['followers'] > compare_b['followers']:
            SCORE += 1
            print(LOGO)
            print(f"You're right! Current score: {SCORE}")
            compare_a = compare_b
        else:
            print(LOGO)
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            CONTINUE_PLAY = False
    elif guess == "B":
        if compare_b['followers'] > compare_a['followers']:
            SCORE += 1
            print(LOGO)
            print(f"You're right! Current score: {SCORE}")
            compare_a = compare_b
        else:
            print(LOGO)
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            CONTINUE_PLAY = False
    else:
        print("\033[91mThat choice is not valid.\033[0m")
        print(LOGO)
