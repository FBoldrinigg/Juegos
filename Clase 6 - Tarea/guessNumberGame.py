import random


def guessGame():
    randomNum = random.randint(1, 100)
    tries = 10
    while tries:
        tries -= 1
        guess = int(input("Take a guess between 1 and 100: "))
        while guess < 1 or guess > 100:
            print("Wrong input, ", guess, " is not a number between 1 and 100")
            guess = int(input("Guess again: "))
        if guess == randomNum:
            print("Congratulations you guessed correctly in: ", 10 - tries, "tries.")
            break
        elif guess > randomNum:
            print("The random number is smaller than ", guess)
        else:
            print("The random number is bigger than ", guess)
    if not tries:
        print("Game over. You ran out of tries, the number was: ", randomNum)


guessGame()
