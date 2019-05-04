import random


class GuessGame:

    def __init__(self):
        self.tries = 10
        self.randomNum = random.randint(1, 100)

    def hint(self, guess):
        if self.tries:
            if guess > self.randomNum:
                print("\nThe random number is smaller than ", guess,
                      "\nTries remaining: ", self.tries)
            else:
                print("\nThe random number is bigger than ", guess,
                      "\nTries remaining: ", self.tries)

    def setGuess(self):
        guess = ""
        while not guess:
            try:
                guess = int(input("\nTake a guess between 1 and 100: "))
                while guess < 1 or guess > 100:
                    print("Wrong input, ", guess, " is not a number between "
                          "1 and 100\n")
                    guess = int(input("Guess again: "))
            except ValueError:
                print("Wrong input.")
                guess = ""
        return guess

    def runGame(self):
        while self.tries:
            self.tries -= 1
            guess = self.setGuess()
            if guess == self.randomNum:
                print("Congratulations you guessed correctly in: ",
                      10 - self.tries, "tries.")
                break
            self.hint(guess)
        if not self.tries:
            print("\n\nGame over. You ran out of tries, the number was: ",
                  self.randomNum)


newGame = GuessGame()
newGame.runGame()
