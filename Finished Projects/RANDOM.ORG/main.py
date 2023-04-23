import random


def Low_Digit(low):
    while low.isdigit() is False:
        print("Only Integers Allowed")
        low = input("Enter The Lowest Number: ")
    return int(low)


def High_Digit(high):
    while high.isdigit() is False:
        print("Only Integers Allowed")
        high = input("Enter The Highest Number: ")
    return int(high)


def Low_Exceeding(low):
    while low > high:
        print("Your Lowest Number Must Be Less Than Your Greatest Number")
        low = input("Enter The Lowest Number: ")
        low = Low_Digit(low)
    return int(low)


def High_Deficient(high):
    while high < low:
        print("Your Highest Number Must Be Greater Than Your Lowest Number")
        high = input("Enter The Highest Number: ")
        high = High_Digit(high)
    return int(high)


def Exceeding(low, high):
    while low > 10000:
        print("Enter A Number Less Than Or Equal To 10,000")
        low = input("Enter The Lowest Number: ")
        low = Low_Digit(low)
        low = Low_Exceeding(low)
    while high > 10000:
        print("Enter A Number Less Than Or Equal To 10,000")
        high = input("Enter The Highest Number: ")
        high = High_Digit(high)
        high = High_Deficient(high)
    return int(low), int(high)


low = input("Enter The Lowest Number: ")
low = Low_Digit(low)
high = input("Enter The Highest Number: ")
high = High_Digit(high)
low = Low_Exceeding(low)
high = High_Deficient(high)
low, high = Exceeding(low, high)
numbers = list(range(low, high + 1))
random.shuffle(numbers)
for i in numbers:
    print(i)
