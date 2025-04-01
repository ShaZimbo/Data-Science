""" This programme takes a word and both encrypts and decrypts it"""
from art import LOGO, alphabet


def caesar(user_direction, original_text, shift_amount):
    """ Function to encrypt/decrypt based on user inputs """
    message = ""
    for letter in original_text:
        if letter in alphabet:
            if user_direction == "encode":
                encoded_index = alphabet.index(letter) + shift_amount
            elif user_direction == "decode":
                encoded_index = alphabet.index(letter) - shift_amount
            encoded_index %= len(alphabet)
            message += alphabet[encoded_index]
        else:
            message += letter
    print(f"Here is your {user_direction}d message: {message}")


print(LOGO)

SHOULD_CONTINUE = True

while SHOULD_CONTINUE:
    direction = input(
        "Type 'encode' to encrypt or 'decode' to decrypt.\n").lower()
    if direction in ("encode", "decode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
    else:
        print("You have selected an invalid option")
    user_choice = input("Type 'yes' if you want to go again.\n").lower()
    if user_choice != "yes":
        print("Goodbye!")
        break
