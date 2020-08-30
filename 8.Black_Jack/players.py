class Players():

    def __init__(self, name):
        
        self._name = name
        self._hand_cards = []
        self._hand_value = 0 # cards value 'Jack', 'Queen', 'King' = 10. Ace 1 or 11
        self._ace_number = 0 # how many 'Ace' has the player 
        self._score = 0     # score
        self._bust = 0      # if player bust "bust = 1"
        self._stand = 0     # if choiced stand, velue = 1
        self._black_jack = 0 #Black jack value
       
    @property    
    def name(self):
        return self._name

    @name.setter    
    def name(self, new_name):
        self._name = new_name
        return self._name

    @property    
    def hand_cards(self):
        return self._hand_cards

    @hand_cards.setter    
    def hand_cards(self, new_card):
        self._hand_cards.append(new_card)
        if new_card == 'Ace':
            self.ace_number = 1           
        return self._hand_cards

    @property    
    def ace_number(self):
        return self._ace_number

    @ace_number.setter    
    def ace_number(self, new_ace):
        self._ace_number += new_ace
        return self._ace_number 

    @property    
    def hand_value(self):
        return self._hand_value

    @hand_value.setter    
    def hand_value(self, card_value):
        self._hand_value += card_value

        if self.hand_value > 21 and self.ace_number > 0:
            self.hand_value = -10
            self.ace_number = -1
       
        if self.hand_value > 21:
            self.bust = 1        
        return self._hand_value

    @property    
    def score(self):
        return self._score

    @score.setter    
    def score(self, new_score):
        self._score += new_score
        return self._score 

    @property    
    def bust(self):
        return self._bust

    @bust.setter
    def bust(self, new_bust):        
        self._bust += new_bust
        return self._bust

    @property    
    def stand(self):
        return self._stand

    @stand.setter    
    def stand(self, new_stand):
        self._stand = new_stand
        return self._stand

    @property    
    def black_jack(self):
        return self._black_jack

    @black_jack.setter    
    def black_jack(self, new_black_jack):
        self._black_jack = new_black_jack
        return self._black_jack

    
