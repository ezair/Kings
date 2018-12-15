#!/usr/bin/env python
##################################################################
#Author:  Eric Zair                                              #
#File:    kings.py                                               #
#Description:    This program simulates the Card game "Kings"    #
##################################################################

import time
import random
import pyttsx
from pygame import mixer
from os import system
from os.path import isfile


#Check to see if sound file exists for can breaking sound.
#Returns: boolean -- true if song exists, false otherwise.
def sound_exists():
    return isfile('../sounds/Can Breaking.mp3')


#Add all of the cards into a deck of 52.
#The list of cards with be a list of strings,
#where each index represents a card in string form.
#return: list of cards
def get_cards():
    cards = []
    #populate list of cards with with 2-11 and face cards.
    for i in range(2, 11):
        cards.append(str(i))
    cards += ["Queen", "King", "Jack", "Ace"]
    cards *= 4
    return cards


#Ask the user if they want to print out another card.
#If they say yes, Print out another card.
#Exit if they say no.
#parameters:
#           cards -- list of cards for game
#           players -- list of players.
#           number_of_turns -- number of turns
#                              in the game.
def play(cards, players, number_of_turns):
    print_players_turn(players, number_of_turns)
    play = raw_input("Press enter to print a card(N to end program): ")
    if play.upper() != "N":
        system("clear")
        print_random_card(cards)
    else:
        print "\nHave a nice day!"
        exit()


#Play the sound of a given string.
#parameters:
#           sound -- string of the card that was just played.
def play_sound(sound):
    engine = pyttsx.init()
    engine.say(sound)
    engine.runAndWait()


#Play can Break sound (saved in sounds folder).
def play_can_break_sound():
    #We need to make a pygame mixer to play sounds.
    mixer.init()
    mixer.music.load('../sounds/Can Breaking.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()


#Print out a random card from the deck.
#Remove that Random card from given list of
#cards afterwards, because it has been used.
#parameters:
#           cards -- list of cards in the deck
def print_random_card(cards):
    card = random.choice(cards)
    #create engine object to play sound from string.
    print(str(card))
    cards.remove(card)
    play_sound(str(card))


#Ask user if they want to play again.
#return if they say yes or no
#return: Boolean -- true if user wants to play again; false otherwise.
def play_again():
    print "\nThere are no more cards left in the deck."
    while True:
        answer = raw_input("Would you like to play again(Y/N)? ")
        if (answer.upper() == "Y") or (answer.upper() == "N"):
            return answer.upper() == "Y"
        else:
            print "\nThat is not a valid answer"


#Ask user to enter the number of players.
#Error check to make sure user does not enter a string
#Return: integer that will be the number of players
#        playing the game.
#        Note: we recall recursively if there is an error.
def get_number_of_players():
    while True:
        # Return the number of players.
        try:
            return input("Enter the number of players: ")
        #error, we have to tell the user there is an issue and ask again(recursively).
        except:
            print "Error: That is not a number!"
            print "Please try again."
            return get_number_of_players()


#Set the names of all the players playing
#Add players to list.
#return: players -- list of players
def get_players():
    players = []
    number_of_players = get_number_of_players()
    for i in range(number_of_players):
        player = raw_input("Enter the player" + str(i+1) + "'s name: ")
        player.strip()
        players.append(player)
    system("clear")
    return players


#Print which player's turn it is.
#Parameters:
#           players -- list of players playing the game.
#           number_of_turns -- number of turns that we are
#                              on in the game.
def print_players_turn(players, number_of_turns):
    player = players[number_of_turns % len(players)]
    print "\nIt's " + player + "'s turn."


#Check to see if the can is broken.
#parameters:
#           number_of_can_hits -- the number of times the can
#                                 will get hit before breaking
#return: boolean -- true if can is broken; false otherwise.
def is_broken(number_of_can_hits, number_of_turns):
    return (number_of_turns >= number_of_can_hits)


#This method is reached when the player breaks the can.
#Play the sound of can breaking.
#Sleep for 5 seconds.
#parameters:
#           players -- list of players
#           number_of_turns -- integer number of turns
#                              that will be played.
#return: cards -- list of cards.
def can_breaks(players, number_of_turns):
    #print that the player broke the can to the screen
    for i in range(30):
        player = players[number_of_turns % len(players)]
    print player + " Broke The Can!"    
    play_can_break_sound()
    time.sleep(2)
    system("clear")
    return cards


#----------------------------------------------------------------------
def main():
    #make sure that the sound file exists
    #because if it does not, this runins the game.
    if not sound_exists():
        print "Error: sound file not found"
        exit()

    system("clear")
    number_of_turns = 0
    #Save this for if the user wants to play again after first game is completed.
    run_program_again = True
    while run_program_again:
        #number that can breaks at.
        number_of_can_hits = random.randint(10, 52)	
        cards = get_cards()
        players = get_players()
	
        #Make sure that there are cards left and the can is not broken.
        while (len(cards) > 0) and (not is_broken(number_of_can_hits, number_of_turns)):
            play(cards, players, number_of_turns)
            #we increment the number of turns, because a turn has passed.
            number_of_turns += 1
	    
    	#Can breaks / Ask if user wants to play again
    	can_breaks(players, number_of_turns)
    	run_program_again = play_again()
    
    #User doesn't wanna play again.
    print "Have a great day!"
#----------------------------------------------------------------------
if __name__ == '__main__':
    main()