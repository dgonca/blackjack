from deck import *

class Shoe:
    shoe = []
    shoe_length = 6
    cards = []

    def __init__(self):
        self.create_shoe()
        self.shuffle_shoe()

    def create_shoe(self):
        for i in range(self.shoe_length):
            new_deck = Deck()
            self.shoe.append(new_deck)

    def shuffle_shoe(self):
        for d in self.shoe:
            for card in d.cards:
                self.cards.append(card)
        random.shuffle(self.cards)

    def get_card(self, index):
        return self.cards.pop(index)