import random


def rockPaperScissor():
    result = ["rock", "paper", "scissor"]
    scoreA = 0
    scoreB = 0
    while scoreA < 3 and  scoreB < 3:
        playerIn = input("Choose one: 'rock', 'paper', 'scissor': ")
        computerIn = result[random.randint(0, 2)]
        playerIn = playerIn.lower()
        if playerIn not in result:
            print("Wrong input.")
        if playerIn == computerIn:
            print(playerIn, " x ", computerIn)
            print("It's a tie.")
        if playerIn == "rock" and computerIn == "paper":
            print(playerIn, " x ", computerIn)
            scoreB += 1
        elif playerIn == "paper" and computerIn == "scissor":
            print(playerIn, " x ", computerIn)
            scoreB += 1
        elif playerIn == "scissor" and computerIn == "rock":
            print(playerIn, " x ", computerIn)
            scoreB += 1
        elif playerIn == "paper" and computerIn == "rock":
            print(playerIn, " x ", computerIn)
            scoreA += 1
        elif playerIn == "rock" and computerIn == "scissor":
            print(playerIn, " x ", computerIn)
            scoreA += 1
        elif playerIn == "scissor" and computerIn == "paper":
            print(playerIn, " x ", computerIn)
            scoreA += 1
        print("The score is:", scoreA, " - ", scoreB)
    if scoreB == 3:
        print("###You lost###", scoreA, " - ", scoreB)
    elif scoreA == 3:
        print("###You won###", scoreA, " - ", scoreB)


rockPaperScissor()
