import re
import longre as long


def messageProb(userMessage, recognizedWord, singleResponse=False, requiredWords=[]):
    messageCert = 0
    hasRequiredWord = True
    for word in userMessage:
        if word in recognizedWord:
            messageCert += 1
    percentage = float(messageCert) / float(len(recognizedWord))
    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWord = False
            break
    if hasRequiredWord or singleResponse:
        return int(percentage * 100)
    else:
        return 0


def checkMessage(message):
    highProbList = {}

    def response(botResponse, listOfWords, singleResponse=False, requiredWords=[]):
        nonlocal highProbList
        highProbList[botResponse] = messageProb(
            message, listOfWords, singleResponse, requiredWords
        )

    response("Hello", ["hello", "hi", "sup", "hey", "heyo", "yo"], singleResponse=True)
    response(
        "I'm doing fine, and you?",
        ["how", "are", "you", "doing"],
        requiredWords=["how"],
    )
    response(":)", ["good", "great", "amazing", "fine", "well"], singleResponse=True)
    response("ඞඞඞඞඞඞඞඞඞඞ", ["sus", "among", "us", "baka"])
    response(long.binaryResponse, long.binaryLetters)
    response(
        "Thank you!",
        ["this", "was", "obviously", "made", "by", "the", "best", "programmer", "ever"],
        requiredWords=["programmer", "ever"],
    )
    bestMatch = max(highProbList, key=highProbList.get)
    return long.unknown() if highProbList[bestMatch] < 1 else bestMatch


def response(input):
    splitMessage = re.split(r"\s+|[,;?!.-]\s*", input.lower())
    response = checkMessage(splitMessage)
    return response


while True:
    print("Bot: " + response(input("You: ")))
