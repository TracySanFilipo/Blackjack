import random
import math


class Card():
    class_suit = ['hearts', 'diamonds', 'spades', 'clubs']
    class_value = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        self.deck1 = []
        for sui in Card.class_suit:
            for val in Card.class_value:
                card = Card(sui, val)
                self.deck1.append(card)

    def give_top_card(self):
        return self.deck1.pop(0)

    def check_deck(self):
        height = len(self.deck1)
        if height < 1:
            return True

    def shuffle(self):
        random.shuffle(self.deck1)

    def __repr__(self):
        return "{}".format(self.deck1)
