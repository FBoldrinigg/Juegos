import random


class rockPaperScissor:

    playerIn = ""
    computerIn = ""

    def __init__(self):
        self.scoreA = 0
        self.scoreB = 0
        self.result = ("rock", "paper", "scissor")

    def winner(self):
        if self.playerIn == self.computerIn:
            print(self.playerIn, " x ", self.computerIn)
            print("It's a tie.")
        if self.playerIn == "rock" and self.computerIn == "paper":
            print(self.playerIn, " x ", self.computerIn)
            self.scoreB += 1
        elif self.playerIn == "paper" and self.computerIn == "scissor":
            print(self.playerIn, " x ", self.computerIn)
            self.scoreB += 1
        elif self.playerIn == "scissor" and self.computerIn == "rock":
            print(self.playerIn, " x ", self.computerIn)
            self.scoreB += 1
        elif self.playerIn == "paper" and self.computerIn == "rock":
            print(self.playerIn, " x ", self.computerIn)
            self.scoreA += 1
        elif self.playerIn == "rock" and self.computerIn == "scissor":
            print(self.playerIn, " x ", self.computerIn)
            self.scoreA += 1
        elif self.playerIn == "scissor" and self.computerIn == "paper":
            print(self.playerIn, " x ", self.computerIn)
            self.scoreA += 1

    def gameOverText(self):
        if self.scoreA == 3:
            print("\n### You win ###")
            print(" The ending score is: ", self.scoreA, " - ", self.scoreB)
        else:
            print("\n### You lose ###")
            print(" The ending score is: ", self.scoreA, " - ", self.scoreB)

    def bestOfFive(self):
        while self.scoreA < 3 and self.scoreB < 3:
            self.playerIn = input("\nChoose one: 'rock', 'paper', 'scissor': ")
            self.playerIn = self.playerIn.lower()
            self.computerIn = self.result[random.randint(0, 2)]
            if self.playerIn not in self.result:
                print("Wrong input.")
            else:
                self.winner()
                print("Player ", self.scoreA, " - ", self.scoreB, " Computer")
        self.gameOverText()


newInstance = rockPaperScissor()
newInstance.bestOfFive()
