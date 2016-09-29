##################################################################
# FILE : ex2_rpsls.py
# WRITER : Ori Broda , orib , 308043447
# EXERCISE : intro2cs ex2 2013-2014
# DESCRIPTION :
# Task 2: The function rpsls_game which gets no input, plays
# the game: "Rock - Paper - Scissors - Lizard -Spock" as demonstrated
# in the TV series "The Big Bang Theory". The game is comprised of
# rounds in which the user faces the computer
# and when one side leads by 2, he wins the game and the
# function returns the adequate value (1 for user, -1 for pc).
# Task 3: The function rpsls_play which also gets no input,
# calls for rpsls_game in order to implement "Best of" mode.
# The user will face the computer in sets of games of rpsls_game
# until a winner is declared. The user then can decide whether
# or not to continue playing.
##################################################################

#!/usr/bin/env python3
import random
from ex2_rpsls_helper import get_selection

def rpsls_game():
    # Counters for game statistics and winner declaration.
    player_round_wins = 0 
    computer_round_wins = 0
    draws = 0
    # Continue until one side leads by 2.
    while (abs(computer_round_wins - player_round_wins) != 2):
        player_choice = int(input("    Please enter your selection: "
                                  "1 (Rock), 2 (Paper), 3 (Scissors), 4 "
                                  "(Lizard) or 5 (Spock): "))
        # Confirming that the input is a legal option.
        while ((player_choice < 1) or (player_choice > 5)):
            print("    Please select one of the available options.\n")
            player_choice = int(input("    Please enter your selection: "
                                      "1 (Rock), 2 (Paper), 3 (Scissors), "
                                      "4 (Lizard) or 5 (Spock): "))
        player_selection = get_selection(player_choice)    
        print("    Player has selected: ", player_selection, ".", sep="")
        computer_choice = random.randint(1,5)
        computer_selection = get_selection(computer_choice)
        print("    Computer has selected: ",
              computer_selection, ".", sep="")
        # Determining the winner of the round according to the winning
        # graph.
        if ((player_choice == 1 and computer_choice == 3) or
            (player_choice == 1 and computer_choice == 4) or
            (player_choice == 2 and computer_choice == 1) or
            (player_choice == 2 and computer_choice == 5) or
            (player_choice == 3 and computer_choice == 2) or
            (player_choice == 3 and computer_choice == 4) or
            (player_choice == 4 and computer_choice == 5) or
            (player_choice == 4 and computer_choice == 2) or
            (player_choice == 5 and computer_choice == 3) or
            (player_choice == 5 and computer_choice == 1)):
                print("    The winner for this round is: Player\n")
                player_round_wins = player_round_wins + 1
        elif ((computer_choice == 1 and player_choice == 3) or
               (computer_choice == 1 and player_choice == 4) or
               (computer_choice == 2 and player_choice == 1) or
               (computer_choice == 2 and player_choice == 5) or
               (computer_choice == 3 and player_choice == 2) or
               (computer_choice == 3 and player_choice == 4) or
               (computer_choice == 4 and player_choice == 5) or
               (computer_choice == 4 and player_choice == 2) or
               (computer_choice == 5 and player_choice == 3) or
               (computer_choice == 5 and player_choice == 1)):
                    print("    The winner for this round is: Computer\n")
                    computer_round_wins = computer_round_wins + 1
        else:
             print("    This round was drawn\n")
             draws = draws + 1
    if (player_round_wins > computer_round_wins):
        print("The winner for this game is: Player")
    else:
        print("The winner for this game is: Computer")
    print("Game score: Player ", player_round_wins, ", Computer ",
          computer_round_wins, ", draws ", draws, sep="")
    if (player_round_wins > computer_round_wins):
        return 1   # Winner: player
    else:
        return -1  # Winner: computer          
    pass    

def rpsls_play():
    print("Welcome to the Rock-Scissors-Paper-Lizard-Spock game!")
    option = 2             # Variable for choosing game options.
    sets = 0               # Number of sets that have been played.
    player_set_wins = 0    # Counter for set statistics.
    while (option != 1):   # Game is on.
        if (option == 2):  # User chose to reset scores.
            N = int(input("Select set length: "))
        player_game_wins = 0        # Counters for game statistics
        computer_game_wins = 0      # and winner decleration.
        i = 1
        while (i <= N):    # Set of games
            print("Now beginning game ", i, sep="") #Current game number.
            if (rpsls_game() == 1):    # Player won
                player_game_wins = player_game_wins + 1
            else:                      # Computer won 
                computer_game_wins = computer_game_wins + 1
            print("Set score: Player ", player_game_wins, ", Computer ",
                  computer_game_wins, sep="") 
            i = i + 1
            # The set ends and we have a winner.
            # The weaker side cant win the set within
            # the remaining games.
            if ((player_game_wins > N//2) or
                (computer_game_wins > N//2)):
                break
        # Set is over and still no winner - tied game.    
        if (computer_game_wins == player_game_wins):
            # Keep playing until the set is concluded = tie breaker.
            while (abs(computer_game_wins - player_game_wins) != 2):
                print("Now beginning game ", i, sep="") 
                if (rpsls_game() == 1):
                    player_game_wins = player_game_wins + 1
                else:
                    computer_game_wins = computer_game_wins + 1
                
                print("Set score: Player ", player_game_wins,
                      ", Computer ", computer_game_wins, sep="") 
                i = i + 1
                    
        sets = sets + 1   # Set is over
        if(player_game_wins > computer_game_wins):
            print("Congratulations! You have won in ",
                  player_game_wins+computer_game_wins, " games.",
                  sep="")
            player_set_wins = player_set_wins + 1
            
        else:
            print("Too bad! You have lost in ",
            player_game_wins+computer_game_wins, " games.", sep="")
        print("You have played ", sets, " sets, and won ",
              player_set_wins, "!\n", sep="")    
        option = int(input("Do you want to: 1 - quit, "
                           "2 - reset scores or 3 - continue? "))
        if (option == 2):
            print("Resetting scores")
            sets = 0
            player_set_wins = 0
 

if __name__=="__main__": #If we are the main script, and not imported
    from sys import argv
    try:
        random.seed(argv[1]) # as a string is good enough
    except:
        pass

    rpsls_play()
