""" Blackjack game """
import random
import os
from art import LOGO, FACE_DOWN_CARD


def draw_card(v, s):
    """ Card art based on suite and number cards """
    card_draw = f'''
    ┌─────────┐
    │{str(v):<2}{s}      │
    │         │
    │         │
    │    {s}    │
    │         │
    │         │
    │      {str(v):>2}{s}│
    └─────────┘
    '''
    return card_draw


def deal_card():
    """ Function to deal a random card"""
    suits = {
        "diamonds": "\033[91m♦\033[0m",
        "clubs": '♣',
        "hearts": "\033[91m♥\033[0m",
        "spades": '♠',
    }

    values = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
              'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    cards = list(values.keys())
    card_value = random.choice(cards)
    card_suit = random.choice(list(suits.values()))

    return values[card_value], draw_card(card_value, card_suit)


def calculate_score(cards):
    """ Calculates the score of the players """
    if sum(cards) == 21 and len(cards) == 2:
        return "BlackJack!"
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player, dealer):
    """ Function to identify winner """
    print(f"{"Dealer's cards:"} {''.join(d_cards_art)}\n")
    print(f"{"Your cards:"} {''.join(p_cards_art)}\n"
          f"{"Dealer's score:":<20} {dealer}\n"
          f"{"Your score:":<20} {player}")
    if player == dealer:
        print("It's a draw! 🙃")
    elif player == "BlackJack!":
        print("BlackJack! You win! 😃")
    elif dealer == "BlackJack!":
        print("Dealer has BlackJack. You lose 😱")
    elif player > 21:
        print("Bust! You lose! 😭")
    elif dealer > 21:
        print("You win! 😃")
    elif player > dealer:
        print("CONGRATULATIONS. You win! 😃")
    else:
        print("You lose! 😱")


END_GAME = False
print(LOGO)
end = input("Enter 'p' to play a game of BlackJack or 'e' to exit: ").lower()


while end == "p":
    os.system('cls')
    print(LOGO)
    p_cards = []
    d_cards = []
    p_cards_art = []
    d_cards_art = []

    for hand in range(2):
        value, art = deal_card()
        p_cards.append(value)
        p_cards_art.append(art)
        value, art = deal_card()
        d_cards.append(value)
        d_cards_art.append(art)

    GAME_OVER = False
    while not GAME_OVER:
        p_score = calculate_score(p_cards)
        d_score = calculate_score(d_cards)
        print(f"Dealer's cards:\n{d_cards_art[0]}\n{FACE_DOWN_CARD}")
        print(f"Your cards:\n{''.join(p_cards_art)}\nYour score: {p_score}")

        if p_score == "BlackJack!" or d_score == "BlackJack!" or p_score > 21:
            GAME_OVER = True
        else:
            more_cards = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if more_cards == "y":
                value, art = deal_card()
                p_cards.append(value)
                p_cards_art.append(art)
            else:
                GAME_OVER = True

    while d_score != "BlackJack!" and d_score < 17:
        value, art = deal_card()
        d_cards.append(value)
        d_cards_art.append(art)
        d_score = calculate_score(d_cards)

    compare(p_score, d_score)

    end = input("Enter 'p' to play a game of BlackJack or 'e' to exit: "
                ).lower()

if end == "e":
    os.system('cls')
    print(LOGO)
    print("Goodbye!")
    END_GAME = True
