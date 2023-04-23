def Times_Digit(times):
    while times.isdigit() is False:
        print("Only Integers Allowed")
        times = input("Enter An Integer: ")
    return int(times)


def Times_Less(times):
    while times < 1:
        print("Enter A Number Greater Than Zero")
        times = input("Enter An Integer: ")
        times = Times_Digit(times)
    return int(times)


def Times_Greater(times):
    while times > 10000000:
        print("Enter A Number Less Than Or Equal To Ten Million")
        times = input("Enter An Integer: ")
        times = Times_Digit(times)
        times = Times_Less(times)
    return int(times)


times = input("Enter An Integer: ")
times = Times_Digit(times)
times = Times_Less(times)
times = Times_Greater(times)

for num in range(1, times + 1):
    if num % 15 == 0:
        print("Fizz Buzz!")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
