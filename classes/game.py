from shoe import Shoe

class Game:

    shoe = []

    def __init__(self):
        self.shoe = Shoe()

    def deal_hand(self):
        player_hand = []
        dealer_hand = []
        player_hand.append(self.shoe.get_first_card())
        dealer_hand.append(self.shoe.get_first_card())
        player_hand.append(self.shoe.get_first_card())
        dealer_hand.append(self.shoe.get_first_card())
        return {
            'player_hand' : player_hand
            ,'dealer_hand' : dealer_hand
            ,'remaining_deck' : self.shoe.cards
    }