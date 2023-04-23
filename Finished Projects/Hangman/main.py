import random
import words

erase = "\x1b[2K"
up = "\033[1A"
print((up + erase) * 2, end="")


def restart(linesToErase):
    print((up + erase) * (linesToErase + 2), end="")
    main()


def main():
    linesToErase = 0
    wordDisplay = []
    usedInput = []
    while True:
        guesses = input("Enter The Amount Of Guesses: ")
        linesToErase += 2
        if guesses.isdigit() is False or int(guesses) < 1:
            print("Invalid Input")
        else:
            guesses = int(guesses)
            word = words.words[random.randint(0, len(words.words))]
            print("The Word Length Is", len(word))
            charactersLeft = len(word)
            break
    for _ in word:
        wordDisplay.append("_")
    while True:
        userInput = input("Enter A Letter: ").lower().strip()
        if (
            userInput.isdigit()
            or len(userInput) > 1
            or userInput in words.incorrectCharacters
            or userInput == ""
        ):
            print("Invalid Input")
        elif userInput in usedInput:
            print("You've Already Entered This")
        else:
            usedInput.append(userInput)
            if userInput in word:
                charactersLeft -= list(word).count(userInput)
                if charactersLeft == 0:
                    userInput = input(
                        f"You've Won! The Word Was {word}. Press 'enter' or 'return' To Continue: "
                    )
                    restart(linesToErase)
                print(f"Correct, There Are {charactersLeft} Letters Left")
                for i in range(len(word)):
                    if word[i] == userInput:
                        wordDisplay[i] = userInput
                print(*wordDisplay)
                linesToErase += 1
            else:
                guesses -= 1
                if guesses == 0:
                    userInput = input(
                        f"You've Lost! The Correct Answer Was {word}. Press 'enter' or 'return' To Continue: "
                    )
                    restart(linesToErase)
                print(f"Incorrect, You Have {guesses} Guess Left")
        linesToErase += 2


main()
