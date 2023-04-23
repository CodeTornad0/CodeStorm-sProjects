import random


def ResetText():
    erase = "\x1b[2K"
    up = "\033[1A"
    print((up + erase) * 100, end="")


def Game():
    ResetText()
    try:
        guesses = int(input("Enter The Amount Of Guesses: "))
        highNum = int(input("Enter What The Maximum Number Is: "))
        lowNum = int(input("Enter What The Lowest Number Is: "))
        genNum = random.randint(lowNum, highNum)
        answer = int(input("Enter What The Number Is: "))
        while True:
            ResetText()
            if answer == genNum:
                print("You've Won!")
                restart = input("Press Enter To Play Again: ")
                Game()
            elif guesses - 1 > 0:
                if answer < genNum:
                    print("The Number Is Higher")
                else:
                    print("The Number Is Lower")
                guesses -= 1
                answer = int(input("Enter What The Number Is: "))
            else:
                print(f"You've Lost! The Number Was {genNum}")
                break
    except Exception:
        print("Invalid Input")
        Game()


Game()
