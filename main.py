import random
from thisgame import ThisGame

newJanken = ThisGame()
# while True:
# print("Choose an option.")
# print("1.Rock")
# print("2.Paper")
# print("3.Scissors")

# # Option 1 = Rock
# # Option 2 = Scissors
# # Option 3 = Paper

# userSelect = input("Enter a choice (1, 2, 3): ")
# possibleActions = ["rock", "paper", "scissors"]
# userInput = possibleActions[int(userSelect)-1]
# computerInput = random.choice(possibleActions)
# print(f"\nYou chose {userInput}, computer chose {computerInput}.\n")
print(newJanken.initial())


# if userInput == computerInput:
#     print(f"Both players selected {userInput}. It's a tie!")
# elif userInput == "rock":
#     if computerInput == "scissors":
#         print("Rock smashes scissors! You win!")
#     else:
#         print("Paper covers rock! You lose.")
# elif userInput == "paper":
#     if computerInput == "rock":
#         print("Paper covers rock! You win!")
#     else:
#         print("Scissors cuts paper! You lose.")
# elif userInput == "scissors":
#     if computerInput == "paper":
#         print("Scissors cuts paper! You win!")
# else:
#     print("Rock smashes scissors! You lose.")

# play_again = input("Play again? (y/n): ")
# if play_again.lower() != "y":
#     break
