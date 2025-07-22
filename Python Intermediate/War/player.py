""" Player cards """

class Player:
    """ Tracks player and their deck of cards"""
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """ Returns one card """
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """ Adds cards to deck """
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
