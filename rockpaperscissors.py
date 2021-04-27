import random
print("ROCK, PAPER, SCISSORS GAME")
print("-" * 27)
name = input("Enter your name: ") # Asks for user's name
# Initializes variables
userWins = 0
aiWins = 0
ties = 0
result = ""
statements = ["It's a Tie", f"{name} Wins Round", "AI Wins Round"] # Printed statements after each round
while True:
    selection = input("Enter your choice (Rock, Paper, or Scissors): ") # Asks user to input a choice
    selection = selection.upper()
    if (selection == "ROCK" or selection == "PAPER" or selection == "SCISSORS"): # Checks if user input the right choice
        aiChoices= ["ROCK", "PAPER", "SCISSORS"] # List of choices the AI can choose
        aiSelection = random.choice(aiChoices) # Randomly selects a value
        # Determines who won
        result 
        if selection == "ROCK":
            if aiSelection == "ROCK":
                result = statements[0]
                ties += 1
            elif aiSelection == "PAPER":
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
            else:
                result = statements[0]
                ties += 1
        print("You choose: " + selection) # prints user's choice
        print("The computer choose: " + aiSelection) # prints AI's choice
        print(result) # print statement value
        print(f"{name}: " + str(userWins) + "/3") # prints user's name and current score out of 3
        print("AI: " + str(aiWins) + "/3") # prints AI and current score out of 3
        print("Ties: " + str(ties)) # prints the number of ties
        if userWins == 3: # stops program when 3 games are won
            print(f"{name} Wins!")
            break
        if aiWins == 3: # stops program when 3 games are won
            print("AI Wins!")
            break
    else: # if user does not enter the proper choice, the program loops again
        print("Error! Try again!")

