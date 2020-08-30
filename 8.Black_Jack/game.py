from deckofcards import DeckOfCards
from players import Players

class Game(Players, DeckOfCards):
   
    def __init__(self, current_players):
        
        self._current_players = current_players
        self._deck = DeckOfCards()             
        self._current_players.append(Players("Kurpiye"))

        print("Game started..")

    def cards_deal(self):        
        for i in range(2):
            for player in self._current_players:
                temp_card = self._deck.card_deal()
                player.hand_cards = temp_card
                player.hand_value = self._deck.cardvalue(temp_card)

    def isBlackJack(self):
        for player in self._current_players:
            if player.hand_value == 21:
                player.black_jack = 1
                player.score = 1
    
    def scoreValues(self): 
        if self._current_players[0].black_jack == 1:            
            return
        elif self._current_players[0].bust > 0:
            for player in self._current_players[1:]:
                if player.bust == 0:
                    player.score = 1
                    
        elif self._current_players[0].bust == 0:
            for player in self._current_players[1:]:
                if self._current_players[0].hand_value > player.hand_value:
                    self._current_players[0].score = 1
                elif self._current_players[0].hand_value < player.hand_value and player.bust == 0:
                    player.score = 1

    def acecontrol(self):
        pass
    
    # if kurpiyes card2 = 0, it shown as "?"
    
    def write_values(self,kurpiyes_card2): 
        if kurpiyes_card2 == 1:
            for player in self._current_players:
                print(f"{player.name} = {player.hand_cards} => {player.hand_value}", 
                "=> BUST" if player.bust == 1 else '',
                f" /  Score => {player.score}",
                " => !!! Black Jack !!!" if player.black_jack == 1 else '')
                                
        elif kurpiyes_card2  == 0:
            for player in self._current_players:
                if player.name == "Kurpiye":
                    print(f"{player.name} = {player.hand_cards[0]} + ?")
                else:
                    print(f"{player.name} = {player.hand_cards} => {player.hand_value}", 
                    " => !!! Black Jacj !!!" if player.black_jack == 1 else '')
                

