""" Cards for War game """
from random import shuffle
values = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
              'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suits = {
        "diamonds": "\033[91m♦\033[0m",
        "clubs": '♣',
        "hearts": "\033[91m♥\033[0m",
        "spades": '♠',
    }
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Card:
    """ Card options """
    def __init__(self, suit, rank):
        self.suit = suits[suit]
        self.value = values[rank]

    def __str__(self):
        return f'''
    ┌─────────┐
    │{str(self.value):<2}{self.suit}      │
    │         │
    │         │
    │    {self.suit}    │
    │         │
    │         │
    │      {str(self.value):>2}{self.suit}│
    └─────────┘
    '''

class Deck:
    """ Create deck and shuffle """
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for value in values:
                create_card = Card(suit, value)
                self.all_cards.append(create_card)

    def shuffle(self):
        """Shuggle deck of cards """
        shuffle(self.all_cards)

    def deal_one(self):
        """ Deal a new card """
        return self.all_cards.pop()

cards = Deck()
cards.shuffle()
print(cards.all_cards[0])
