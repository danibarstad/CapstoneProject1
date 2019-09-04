# ********************************************* #
#                                               #
# SHOWDOWN IN SHINJUKU is a simple, short       #
# text-based adventure game. Character names,   #
# attack names, locations, flavor text, etc     #
# are lifted or adapted from the psycadelic     #
# surf-rock band, Daikaiju!                     #
# https://daikaiju.bandcamp.com/                #
#                                               #
# ********************************************* #

from dataclasses import dataclass
import random

# global variable for each character's hit points
HEALTH = 10

# class a character's attack
@dataclass
class Attack:
    name: str
    damage: int

# class for creating a character
@dataclass
class Character:
    name: str
    hp: int
    atk: Attack
    taunt: str      # flavor text that a character says when they taunt
    defeat: str     # flavor text that a character says when they are defeated

def main():

    # creating attacks
    fist = Attack('Double Fist Attack', 7)
    serpent = Attack('Spiral Serpent Strike', 4)

    # creating the characters
    main = Character('Secret-Man', HEALTH, fist, '\'You cannot defeat me!\'', '\'I have been defeated!\'')
    villain = Character('Sharkakhan', HEALTH, serpent, '\'Daikaiju Die!\'', '\'Farewell, Monster Island\'')


    # displays the text telling the story of the game
    print()
    print(main.name, 'was attempting to escape from Nebula M Spacehunter!')
    print('But he was stopped by the evil ', villain.name, '!', sep='')
    print('This is... SHOWDOWN IN SHINJUKU!')
    print('<------------------------------>')
    print()

    while main.hp > 0 and villain.hp > 0:
        turn = True

        hitPoints(main, villain)            # display hit points

        playerTurn = menu(main, villain)    # show menu
        while turn:
            if playerTurn == 1:
                fight(main, villain)        # call fight function
                turn = False
            elif playerTurn == 2:
                tauntFun(main)              # call taunt function
                turn = False

        hitPoints(main, villain)

        while turn == False:
            # creates a random integer of either 1 or 2 for the villain to take its turn
            villainTurn = random.randint(1, 2)
            print(villain.name, '\'s turn!', sep='')
            if villainTurn == 1:
                fight(villain, main)        
                turn = True
            elif villainTurn == 2:
                tauntFun(villain)
                turn = True

    winner(main, villain)


# menu function for the player to choose their move
def menu(m, v):
    print('Press 1 to attack!\nPress 2 to taunt!\n')

    try:
        move = int(input('Your turn!: '))

        # asks to reenter input if value is below 1 or above 2
        while move != 1 and move != 2:
            print('YOU MUST ENTER 1 or 2!')
            move = int(input('Press 1 to attack!\nPress 2 to taunt!\n'))

    # throws exception if value is not an integer
    except ValueError:
        print('ERROR: YOU MUST ENTER A VALID NUMBER!')
    
    return move

# displays each character and their current health
def hitPoints(m, v):
    print('You:', m.name, 'HP:', m.hp)
    print('Villain:', v.name, 'HP:', v.hp)

# funtion for when a player taunts
def tauntFun(player):
    print(player.name, ': ', player.taunt, sep='')
    print()

# fight function for whoever when a player attacks
def fight(attacking, defending):
    print(attacking.name, 'attacked!')
    defending.hp -= attacking.atk.damage
    print()

# function that displays if the player has won or lost
def winner(m, v):
    if m.hp > v.hp:
        print('YOU WON!')
    elif m.hp < v.hp:
        print('YOU LOST!')

main()