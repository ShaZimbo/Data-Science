""" Hangman game """
# Modules for hangman game
import random
from hangman_image import HANGMAN_IMAGE, HANGMAN_LOGO
from hangman_words import hangman_words

print(HANGMAN_LOGO)

LIVES = 6
chosen_word = random.choice(hangman_words)
PLACEHOLDER = ["_"] * len(chosen_word)
print(f"\n{"".join(PLACEHOLDER)}")
all_guesses = []

while LIVES != 0:
    guess = input("\nGuess a letter: ").lower().strip()
    if guess in all_guesses:
        print(f"\033[33mYou have already guessed {guess}\033[0m\n")
    elif guess in chosen_word:
        all_guesses.append(guess)
        for i, letter in enumerate(chosen_word):
            if guess == letter:
                PLACEHOLDER[i] = letter
    else:
        LIVES -= 1
        all_guesses.append(guess)
        print(f"\n{guess} is not in the word."
              f"\n\033[33mYou lose a life\033[0m\n")
    print("".join(PLACEHOLDER))
    print(HANGMAN_IMAGE[LIVES])
    print(f"\nYou have {LIVES} turn(s) left\n")
    if "_" not in PLACEHOLDER:
        print("\n\033[32mCONGRATULATIONS!\033[0m\nYou won!\n")
        break
    if LIVES == 0:
        print(f"\033[31m\nYou have lost\033[0m\nThe word was {chosen_word}\n")
        break
