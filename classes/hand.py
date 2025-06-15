from shoe import Shoe
from card_helper import card_numbers

class Hand:

    cards = []
    player_type = None # either Player, Dealer

    def __init__(self, player_type):
        self.player_type = player_type

    def calc_hard_score(self):
        hard_score = 0
        for card in self.cards:
            card_value = card_numbers[card['card_number']]
            if isinstance(card_value) == list:
                hard_score += card_value[1]
            else:
                hard_score += card_value
        return hard_score

    def calc_soft_score(self):
        soft_score = 0 
        for card in self.cards:
            card_value = card_numbers[card['card_number']]
            if isinstance(card_value) == list:
                soft_score += card_value[0]
            else:
                soft_score += card_value
        return soft_score

    def score(self):
        soft_score = self.calc_soft_score()
        hard_score = self.calc_hard_score()
        if soft_score != hard_score:
            return [soft_score, hard_score]
        return hard_score
    
    def current_score(self, soft_flag):
        score = self.score()
        ace_level = score[0] if soft_flag == True else score[1]
        return ace_level if isinstance(score) == list else score

    def add_card(self, card):
        self.cards.append(card)
    
    def is_bust(self):
        if self.current_score(soft_flag=True) > 21:
            return True
        return False
    
    def blackjack(self):
        if self.current_score(soft_flag=False) == 21:
            return True
        return False
        
    def must_stand(self):
        if self.current_score(soft_flag=True) >= 17 or self.current_score(soft_flag=False) >= 17:
            return True
        return False



    

    
    