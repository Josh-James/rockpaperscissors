import random
print("ROCK, PAPER, SCISSORS GAME")
print("-" * 27)
name = input("Enter your name: ")  # Asks for user's name
# Initializes variables
userWins = 0
aiWins = 0
ties = 0
game = False
gameNotStarted = True
# Printed statements after each round
statements = ["It's a Tie", f"{name} Wins Round", "AI Wins Round"]
aiChoices = ["ROCK", "PAPER", "SCISSORS"]
while gameNotStarted:
    # Asks for number of games
    try:
        numOfRounds = int(input("Enter number of games to play: "))
    except:
        print("Error! Try again!")
        continue
    # Sets game mode
    mode = input("Enter the mode you want (Easy or Hard): ")
    mode = mode.upper()
    if mode == "EASY" or mode == "HARD":
        game = True
        gameNotStarted = False
    else:  # if user does not enter the proper mode, the program loops again
        print("Error! Try again!")

while game:
    if mode == "HARD":
        aiChoices.append("LIZARD")
        aiChoices.append("SPOCK")
        # Asks user to input a choice
        selection = input(
            "Enter your choice (Rock, Paper, or Scissors, Lizard, Spock): ")
    else:
        selection = input("Enter your choice (Rock, Paper, or Scissors): ")
    selection = selection.upper()
    # Checks if user input the right choice
    if (mode == "EASY" and (selection == "ROCK" or selection == "PAPER" or selection == "SCISSORS")
        # checks if mode is hard as well as a valid user selection
            or mode == "HARD" and (selection == "ROCK" or selection == "PAPER" or selection == "SCISSORS" or selection == "SPOCK" or selection == "LIZARD")):
        # List of choices the AI can choose
        aiSelection = random.choice(aiChoices)  # Randomly selects a value
        # Determines who won
        if selection == "ROCK":
            if aiSelection == "ROCK":
                result = statements[0]
                ties += 1
            elif aiSelection == "PAPER":
                result = statements[2]
                aiWins += 1
            elif aiSelection == "SCISSORS":
                result = statements[1]
                userWins += 1
            elif aiSelection == "SPOCK":
                result = statements[2]
                aiWins += 1
            else:
                result = statements[1]
                userWins += 1
        elif selection == "PAPER":
            if aiSelection == "ROCK":
                result = statements[1]
                userWins += 1
            elif aiSelection == "PAPER":
                result = statements[0]
                ties += 1
            elif aiSelection == "SCISSORS":
                result = statements[2]
                aiWins += 1
            elif aiSelection == "SPOCK":
                result = statements[1]
                userWins += 1
            else:
                result = statements[2]
                aiWins += 1
        elif selection == "SCISSORS":
            if aiSelection == "ROCK":
                result = statements[2]
                aiWins += 1
            elif aiSelection == "PAPER":
                result = statements[1]
                userWins += 1
            elif aiSelection == "SCISSORS":
                result = statements[0]
                ties += 1
            elif aiSelection == "SPOCK":
                result = statements[2]
                aiWins += 1
            else:
                result = statements[1]
                userWins += 1
        elif selection == "SPOCK":
            if aiSelection == "ROCK":
                result = statements[1]
                userWins += 1
            elif aiSelection == "PAPER":
                result = statements[2]
                aiWins += 1
            elif aiSelection == "SCISSORS":
                result = statements[1]
                userWins += 1
            elif aiSelection == "SPOCK":
                result = statements[0]
                ties += 1
            else:
                result = statements[2]
                aiWins += 1
        else:
            if aiSelection == "ROCK":
                result = statements[2]
                aiWins += 1
            elif aiSelection == "PAPER":
                result = statements[1]
                userWins += 1
            elif aiSelection == "SCISSORS":
                result = statements[2]
                aiWins += 1
            elif aiSelection == "SPOCK":
                result = statements[1]
                userWins += 1
            else:
                result = statements[0]
                ties += 1
        print("You choose: " + selection)  # prints user's choice
        print("The computer choose: " + aiSelection)  # prints AI's choice
        print(result)  # print statement value
        # prints user's name and current score out of 3
        print(f"{name}: " + str(userWins) + f"/{str(numOfRounds)}")
        # prints AI and current score out of 3
        print("AI: " + str(aiWins) + f"/{str(numOfRounds)}")
        print("Ties: " + str(ties))  # prints the number of ties
        if userWins == numOfRounds:  # stops program when 3 games are won
            print(f"{name} Wins!")
            game = False
        if aiWins == numOfRounds:  # stops program when 3 games are won
            print("AI Wins!")
            game = False
    else:  # if user does not enter the proper choice, the program loops again
        print("Error! Try again!")
