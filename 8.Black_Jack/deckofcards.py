from card import Card
import random

class DeckOfCards:
    NUMBER_OF_CARDS = 52  # constant number of Cards

    def __init__(self):
        """Initialize the deck."""
        
        self._deck = []  
        # self._deck = deck
        self.deck_fill()        

    def deck_fill(self):
        for count in range(DeckOfCards.NUMBER_OF_CARDS): 
            self._deck.append(Card(Card.FACES[count % 13], 
                Card.SUITS[count // 13]))
        self.shuffle()
    
    def shuffle(self):
        """Shuffle deck."""
        random.shuffle(self._deck)

    
    def card_deal(self):
        try:
            return self._deck.pop(0).face
        except :
            return None
        
    def cardvalue(self,card):

        if card =='Ace':
            return 11
        elif card in ('Jack', 'Queen', 'King'):
            return 10
        else:
            return int(card)

    @property
    def deck(self):
        return self._deck        

