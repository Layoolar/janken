import random


class ThisGame():
    def handleInputs(self, userInput, computerInput):
        if userInput == computerInput:
            return f"Both players selected {userInput}. It's a tie!"
        elif userInput == "rock":
            if computerInput == "scissors":
                return "Rock smashes scissors! You win!"
            else:
                return "Paper covers rock! You lose."
        elif userInput == "paper":
            if computerInput == "rock":
                return "Paper covers rock! You win!"
            else:
                return "Scissors cuts paper! You lose."
        elif userInput == "scissors":
            if computerInput == "paper":
                return "Scissors cuts paper! You win!"
            else:
                return "Rock smashes scissors! You lose."

    def initial(self):
        print("Choose an option.")
        print("1.Rock")
        print("2.Paper")
        print("3.Scissors")

        userSelect = input("Enter a choice (1, 2, 3): ")
        possibleActions = ["rock", "paper", "scissors"]
        userInput = possibleActions[int(userSelect)-1]
        computerInput = random.choice(possibleActions)
        print(f"\nYou chose {userInput}, computer chose {computerInput}.\n")
        print(self.handleInputs(userInput, computerInput))
        self.nextGame()

    def nextGame(self):
        state = True
        while state:
            nextGame = input("Play again? (y/n): ")
            if nextGame == "n":
                break
            if nextGame == "y":
                self.initial()
