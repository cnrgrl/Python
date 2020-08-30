from players import Players
from deckofcards import DeckOfCards
from game import Game
import time

print(' ### BLACKJACK GAME - (Soft 17) ### '.center(100,'*'))

current_players = []

game = Game(current_players)

while True:
    try:
        number_of_player = input("Number of players: ")
        
        for i in range(int(number_of_player)):
            print(f"{i+1}. player ", end='')
            player_name = input("name: ")
            current_players.append(Players(player_name.capitalize())) 
        break
        
    except ValueError:
        print("Opps! Enter player's number as a number")

game.cards_deal()
game.isBlackJack()
print("\n")
game.write_values(0)            

for player in current_players[1:]:
    while True:
        if player.black_jack == 1:
            print(f"\n{player.name}, Black Jack")
            break
        print(f"\n{player.name}, Stand(s) or Hit(h) - [{player.hand_value}] : ", end='')
        choise = input()
        if choise.lower() == 's':
            print(f"{player.name} = {player.hand_cards} => {player.hand_value}")
            break
            
        elif choise.lower() == 'h':
            temp_card = game.deck.card_deal()
            player.hand_cards = temp_card
            player.hand_value = game.cardvalue(temp_card)
            if player.bust == 1:                
                print(f"{player.hand_cards} => {player.hand_value}")
                print(f"{player.name}, BUST...")
                break
            else:
                print(f"{player.name} => {player.hand_cards} => {player.hand_value}")
        

        else:
            print("false choise")
     

while current_players[0].hand_value < 17:
    temp_card = game.deck.card_deal()
    current_players[0].hand_cards = temp_card
    current_players[0].hand_value = game.cardvalue(temp_card)

print("\n")
while True:
    print("Score calculating....")
    time.sleep(1)
    break

game.scoreValues()
game.write_values(1)



