"""
Rock-paper-scissors-lizard-Spock 
Rock-paper-scissors is a hand game that is played by two people. 
The players count to three in unison and simultaneously "throw” one of three hand signals 
that correspond to rock, paper or scissors. The winner is determined by the rules:
Rock smashes scissors
Scissors cuts paper
Paper covers rock
Rock-paper-scissors is a surprisingly popular game that many people play seriously 
(see the Wikipedia article for details). 

Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. 
Each choice wins against two other choices, loses against two other choices and ties against itself. 
The Wikipedia entry for RPSLS gives the complete description of the details of 
the game.
"""
# https://py3.codeskulptor.org/#user305_GFKbdh0AKnW6H6t.py

import random

werts=["rock","spock","paper","lizard","scissors"]

player_name=''
challange_number=''


def name_to_number(name):
    return werts.index(name)

def number_to_name(number):
   return werts[number]

while not player_name:
    player_name = input('Pleyer Name: ')
    
while not challange_number:
    challange_number = input('Challange number: ')
    if challange_number.isdigit() == False:
        challange_number=''

print('')

if player_name!='':
    for i in werts:
            print(werts.index(i),'-', i)
print('q - Exit')


def winner(player, computer):    
    difference= (player - computer) % 5

    if difference == 0:
        #print ("{} and computer tie!".format(player_name))
        return '0'
    elif difference <= 2:
        #print ("{} wins!".format(player_name))
        return 'Player'           
    elif difference >= 3:
        #print ("Computer wins!")
        return 'computer'

def rpsls():
    score_player = 0
    score_computer = 0   
    counter = 1    
    while counter <= int(challange_number):
        
        if counter == int(challange_number):
            player_choice = input("\nLast Choise: ")
        else:
            player_choice = input("\n{}. Choise: ".format(counter))
        if(player_choice == 'q'):
            print('Left the game')
            return        
        if player_choice in ['0','1','2','3','4']:
            print("\n{}: ".format(player_name), number_to_name(int(player_choice)))
            computer = random.randrange(0,5)
            print('Computer: ', number_to_name(computer))
            winn=winner(int(player_choice), computer)
            if winn == '0':
                print ("{} and computer tie!".format(player_name))
            elif winn == 'Player':
                print ("{} wins!".format(player_name))
                score_player = score_player + 1
            elif winn == 'computer':
                print ("Computer wins!")
                score_computer = score_computer + 1

            counter += 1
        else:
            print('False choice\n')
        

    if score_player > score_computer:
        print("\n!! {} Champion !!".format(player_name))
    elif score_player < score_computer:
        print("\n!! Computer Champion !!")
    else:
        print("\n!! Computer and {} tiel !!".format(player_name))    
    print("{} times {} win.".format(score_player,player_name))
    print("{} times Computer win.".format(score_computer))
rpsls()




