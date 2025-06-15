import random
from card_helper import *

class Deck:

    cards = []


    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        deck = []
        for suit in suits:
            for card_number in card_numbers.keys():
                deck.append({'suit': suit, 'card_number': card_number})
        return deck
    
    def shuffle(self):
        random.shuffle(self.cards)