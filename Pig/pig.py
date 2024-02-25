'''

A multiplayer game where everyone gets a turn. 
A player first rolls a dice and gets any score other than 1. The next 
number they roll will get added to the first roll. This keeps going
until they get a 1, in which case they will lose all the points. 
Assuming a player gets 5, and the next roll is 4, their score is 9. 
It's basically a gamble to determine who rolls the highest, and they 
can choose to stop whenever they want to. 
In our case, we keep a limit of 50 and two players. Once a player 
reaches 50, they win the game. 
If they roll a 1, their score resets to 0 and the turn goes to the next
player. 

Let's break down the steps. 
We need to come up with a system for a user to roll. So we create a 
random number generator giving us a number between 1 and 6. Then we ask
the use if they want to continue their roll. If they stop their turn,
we take the rolls played and add to some total score and constantly 
check for each roll if either player has a score that is above 50. If 
it is above 50 then we should end the game and announce who won. 

'''

import random  #allows to generate random numbers

def roll(): 
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

'''
In the code below, we are creating a system where the number of players
can only be between 2 and 4. If they don't enter a valid number of 
players, the code will keep looping until a proper input is given. 
We get the input in string and convert it to int later because when we 
configure to get input as int and the user inputs otherwise, the program
will crash. 
'''

while True: 
    players = input("Enter number of players (2-4): ")  # getting input as string
    if players.isdigit():
        players = int(players) # converting string to int
        if 2<=players<=4:
            break
        else:
            print("Must be between 2 and 4.")
    else:
        print("Invalid response, must be between 2 and 4.")

'''
We create a list to maintain the score for the players. By default, 
it's going to be 0 so we create a list with a for loop inside which 
will assign 0 for the number of players. 
'''

max_score = 50
player_scores = [0 for i in range(players)] 

#print("Let's start the game. Score: ",player_scores)

'''
As long as all the values in the list is less than the max_score, 
the while code block will keep looping. 
'''

while max(player_scores) < max_score:  #the max function will give the maximum value inside the array. 
    
    for player_index in range(players): # we're looping over all the players. 
        turn = input("\nPlayer " + str(player_index+1) + ", ready? (y/n) : ")
            
        if turn == "y":    
            current_score = 0 # the score from the beginning will be 0. 
            print("\nYour total score is : ", player_scores[player_index], "\n")

            while True:
                '''
                Here, if the user inputs y, then the code will keep executing. If it's anything 
                other than y, then the loop will break. 
                '''
                player_roll = input("Would you like to roll? (y/n) : ")
                if player_roll != "y":
                    break

                value = roll()
                if value == 1: 
                    print("You rolled a 1. Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You rolled a:",value)

                print("Your score is: ", current_score)

            player_scores[player_index] += current_score
            print ("Your total score is: ", player_scores[player_index])
        
        else: 
            print ("\nYour total score is: ", player_scores[player_index])

'''
As soon as all the turn ends, the loop checks the max value of player_scores
and if there's a value >50, then the loop will stop. We will then append the 
max_score with the max value of player_scores. 
'''

max_score = max(player_scores)
winning_index = player_scores.index(max_score) # we do this to find the winning player's position in the player_scores list. 
print("Player number ", winning_index + 1, " is the winner.")
print("Score: ", max_score)