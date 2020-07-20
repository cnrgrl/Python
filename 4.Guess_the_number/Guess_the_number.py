
#Guess the Number
#Choose the number to be guessed by selecting a rondom integer in the range 1 to 1000. 

import random

def game ():
    number = random.randrange(1,1000)
    player_guess=''
    counter=1
    
    print("\n***  Welcome the NumberGuess game  ***\n")
    while number != player_guess:
        player_guess=input("Enter a number between 1 and 1000 (q for Exit): ")
        if player_guess == "q":
            return

        if (player_guess.isdigit()!=True):
            continue
    
        if(number == int(player_guess)):
            print("\nBravo! You found at {}. guess".format(counter))
            break
        
        if number > int(player_guess):
            print("\nEnter a number higer than {}".format(player_guess))

        if number < int(player_guess):
            print("\nEnter a number smaller than {}".format(player_guess))
                
        counter+=1
    
    while True:
        again=input("Would you like to play again?  (y/n): ")
        if (again == "n"):
            print("Bye...")
            return
        if (again == "y"):
            game()
        print("False choice. Enter 'y' or 'n' ")

game()



