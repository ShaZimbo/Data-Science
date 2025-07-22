""" Game logic for War game """
from cards import Deck
from player import Player

deck = Deck()
deck.shuffle()

player_1 = Player("Player 1")
player_2 = Player("Player 2")

# Deal cards
for i in range(52):
    if i % 2 != 0:
        player_1.add_cards(deck.deal_one())
    if i % 2 == 0:
        player_2.add_cards(deck.deal_one())

COUNT = 0
GAME_ON = True

while GAME_ON:
    if len(player_1.all_cards) == 0:
        print("Player 1 is out of cards.\nPlayer 2 wins!")
        GAME_ON = False
        break
    if len(player_2.all_cards) == 0:
        print("Player 2 is out of cards.\nPlayer 1 wins!")
        GAME_ON = False
        break
    COUNT += 1
    print(f"Round {COUNT}:")


    # Start round
    player_1_cards = [player_1.remove_one()]
    player_2_cards = [player_2.remove_one()]
    print(f"Player 1 hand: {player_1_cards[-1]}\nPlayer 2 hand: {player_2_cards[-1]}")

    # Check winner of each round
    AT_WAR = True
    while AT_WAR:
        if player_1_cards[-1].value > player_2_cards[-1].value:
            player_1.add_cards(player_1_cards)
            player_1.add_cards(player_2_cards)
            print("Player 1 wins the round\n")
            AT_WAR = False
            break
        if player_2_cards[-1].value > player_1_cards[-1].value:
            player_2.add_cards(player_1_cards)
            player_2.add_cards(player_2_cards)
            print("Player 2 wins the round\n")
            AT_WAR = False
            break

        else:
            print("WAR!")
            if len(player_1.all_cards) < 5:
                print(
                    "Player 1 does not have enough cards to continue the war."
                    "\nPlayer 2 wins the game!")
                GAME_ON = False
                break
            elif len(player_2.all_cards) < 5:
                print(
                    "Player 2 does not have enough cards to continue the war."
                    "\nPlayer 1 wins the game!"
                    )
                GAME_ON = False
                break
            else:
                for card in range(5):
                    player_1_cards.append(player_1.remove_one())
                    player_2_cards.append(player_2.remove_one())
