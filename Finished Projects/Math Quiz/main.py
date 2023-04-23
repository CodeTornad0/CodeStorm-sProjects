import random
import time

numQuestions = ""
operations = ["÷", "+", "-", "**", "x"]
difOperations = ["+", "-"]
answeredCorrectly = 0
correctAnswer = 0
correctNum = 0
guesses = 0
start = 0
currentQuestion = 1
streak = 1
points = 1


def Correct():
    global correctAnswer, answer1, answer2, answer3, answer4, correctNum
    if correctNum == 1:
        answer1 = correctAnswer
    elif correctNum == 2:
        answer2 = correctAnswer
    elif correctNum == 3:
        answer3 = correctAnswer
    else:
        answer4 = correctAnswer


def Incorrect():
    global answer1, answer2, answer3, answer4, difOperation
    hasAn1 = False
    hasAn2 = False
    hasAn3 = False
    hasAn4 = False
    for i in range(4):
        if difOperation == "+":
            if hasAn1 is False:
                answer1 = correctAnswer + random.randint(1, 20)
                hasAn1 = True
                difOperation = difOperations[random.randint(0, 1)]
            elif hasAn2 is False:
                answer2 = correctAnswer + random.randint(1, 20)
                hasAn2 = True
                difOperation = difOperations[random.randint(0, 1)]
            elif hasAn3 is False:
                answer3 = correctAnswer + random.randint(1, 20)
                hasAn3 = True
                difOperation = difOperations[random.randint(0, 1)]
            elif hasAn4 is False:
                answer4 = correctAnswer + random.randint(1, 20)
                hasAn4 = True
                difOperation = difOperations[random.randint(0, 1)]
        else:
            if hasAn1 is False:
                answer1 = correctAnswer - random.randint(1, 20)
                hasAn1 = True
                difOperation = difOperations[random.randint(0, 1)]
            elif hasAn2 is False:
                answer2 = correctAnswer - random.randint(1, 20)
                hasAn2 = True
                difOperation = difOperations[random.randint(0, 1)]
            elif hasAn3 is False:
                answer3 = correctAnswer - random.randint(1, 20)
                hasAn3 = True
                difOperation = difOperations[random.randint(0, 1)]
            elif hasAn4 is False:
                answer4 = correctAnswer - random.randint(1, 20)
                hasAn4 = True
                difOperation = difOperations[random.randint(0, 1)]


def ResetText():
    erase = "\x1b[2K"
    up = "\033[1A"
    print((up + erase) * 100, end="")


def Input():
    global currentQuestion, points, streak, answer1, answer2, answer3, answer4, guesses, numQuestions, answeredCorrectly

    def Done():
        global numQuestions, answeredCorrectly, currentQuestion, start
        if type(numQuestions) == int:
            if currentQuestion > numQuestions:
                end = time.time()
                print(
                    f"Test Finished... Score: {round(answeredCorrectly/numQuestions*100, 2)}% [{answeredCorrectly}/{numQuestions}] Time Taken: {round(end-start, 2)} Seconds"
                )
                quit()

    def Invalid():
        ResetText()
        print("Invalid Input")
        Guesses()
        return

    def Guesses():
        global guesses
        try:
            guesses = int(input("Enter The Amount Of Guesses: "))
            ResetText()
            if guesses < 1:
                Invalid()
        except Exception:
            Invalid()

    if guesses == 0:
        Guesses()
    if currentQuestion == 1:
        global start
        start = time.time()
    print(f"Question {currentQuestion}. What Is {randNum1} {operation} {randNum2}")
    print(f"1. {answer1} 2. {answer2} 3. {answer3} 4. {answer4}")
    try:
        userInput = input("Answer: ")
        ResetText()
        if userInput.lower().strip() == "restart" or userInput == "r":
            currentQuestion = 1
            streak = 1
            points = 1
            answeredCorrectly = 0
            guesses = 0
            Questions()
            Input()
            return
        userInput = int(userInput)
        if userInput < 1 or userInput > 4:
            print("Invalid Input")
            Input()
            return
        currentQuestion += 1
        if userInput == correctNum:
            current = points
            streak += 1
            answeredCorrectly += 1
            if streak == 2:
                points = round(points * streak / 1.5, 2)
            elif streak < 6:
                points = round(points * (streak - 1) / 1.5, 2)
            elif streak - 1 < 10:
                points = round(points * (streak - 1) / 3, 2)
            else:
                points = round(points * (streak - 1) / 6, 2)
            print(
                f"That Is Correct! You Have Gained {round(points - current, 2)} Points. Your Streak Is {streak - 1}"
            )
            print(f"You Have {round(points - 1, 2)} Points")
        else:
            guesses -= 1
            if guesses < 1:
                ResetText()
                print("You've Lost")
                Done()
                currentQuestion = 1
                streak = 1
                points = 1
                Questions()
                Input()
                return
            print(
                f"Incorrect! Answer Is {correctAnswer}. You Have Lost Your Streak"
            ) if streak > 1 else print(f"Incorrect! Answer Is {correctAnswer}")
            streak = 1
        Done()
    except Exception:
        ResetText()
        print("Only Numbers Allowed")
        Input()
        return


def Answer():
    global correctAnswer, operation, randNum1, randNum2
    randNum1 = random.randint(-100, 100)
    randNum2 = random.randint(-100, 100)
    try:
        if operation == "+":
            correctAnswer = randNum1 + randNum2
        elif operation == "-":
            correctAnswer = randNum1 - randNum2
        elif operation == "**":
            correctAnswer = round(randNum1**randNum2, 2)
        elif operation == "x":
            correctAnswer = round(randNum1 * randNum2, 2)
        else:
            correctAnswer = round(randNum1 / randNum2, 2)
        while len(str(correctAnswer)) > 6:
            Answer()
            return
    except ZeroDivisionError:
        correctAnswer = 0


def Questions():
    try:
        userInput = input(
            "Enter The Amount Of Question(s) You Would Like To Answer [NON or NA If Endless]: "
        )
        ResetText()
        if userInput.lower().strip() != "non" and userInput.lower().strip() != "na":
            global numQuestions
            numQuestions = userInput
            numQuestions = int(numQuestions)
            if numQuestions < 1:
                print("Invalid Input")
                Questions()
                return
    except Exception:
        ResetText()
        print("Invalid Input")
        Questions()
        return


Questions()
while True:
    operation = operations[random.randint(0, 4)]
    correctNum = random.randint(1, 4)
    Answer()
    difOperation = difOperations[random.randint(0, 1)]
    Incorrect()
    Correct()
    Input()
