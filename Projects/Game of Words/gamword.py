""" Functions"""

import random


def get_words():
    "Function to open words.txt"
    word_list = []
    with open("words.txt", "r", encoding="utf-8") as words_data:
        word_list = [word.strip() for word in words_data]
    return word_list


def menu_selection():
    """ Function to provide menu options"""
    print(f"\n{'Select one of the following options:'}\n")
    print('\u2500' * 50)
    print(f"{'p':<10} - {'play game'}\n"
          f"{'e':<10} - {'exit'}\n")
    selection = input("Selection: ").lower()
    if selection not in ['p', 'e']:
        print("\033[31m\n"
              "Invalid selection. Please try again.\n\033[0m"
              )
        return menu_selection
    return selection


correct = []
misplaced = []
incorrect = []
max_turn = 5
current_turn = 0

user_name = input("Enter your name:\n")
print(f"\nHello {user_name}! Welcome to the game of words.\n"
      f"\nThere are 5 letters in each word.\n"
      f"You have to guess the word in 5 turns.\n"
      )

while True:
    menu_choice = menu_selection()

    while menu_choice == "p":
        current_turn = 0
        rand_word = random.choice(get_words())
        while current_turn < max_turn:
            user_guess = input("Enter your guess:\n").lower()
            if len(user_guess) != 5:
                print("\033[31m\n"
                      "Your guess must be 5 characters long.\n\033[0m"
                      )
                user_guess = input("Enter your guess:\n").lower()
            current_turn += 1
            if user_guess == rand_word:
                print(f"\033[32m\nCongratulations!\033[0m\n\n"
                      f"You have guessed the word in {current_turn} turns."
                      )
                break
            else:
                correct.clear()
                misplaced.clear()
                incorrect.clear()
                for i in range(5):
                    if user_guess[i] == rand_word[i]:
                        correct.append(user_guess[i])
                    if (user_guess[i] in rand_word and
                            user_guess[i] not in correct):
                        misplaced.append(user_guess[i])
                    if user_guess[i] not in rand_word:
                        incorrect.append(user_guess[i])
                print(f"Correct letters in correct position:\n"
                      f"\033[32m{correct}\033[0m\n"
                      f"Correct letters in wrong position:\n"
                      f"\033[33m{misplaced}\033[0m\n"
                      f"Incorrect letters:\n"
                      f"\033[31m{incorrect}\033[0m\n"
                      f"Turns left: {max_turn - current_turn}"
                      )
            if current_turn == max_turn:
                print(f"\033[31mSorry!\033[0m\n"
                      f"You have exhausted all your turns.\n"
                      f"The word was {rand_word}"
                      )
                break
        menu_choice = menu_selection()

    # Exit section
    if menu_choice == 'e':
        print(f"\nGoodbye {user_name}!!!\n")
        exit()
