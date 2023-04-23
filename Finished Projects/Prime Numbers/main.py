user_input = input(
    "Action 1. Find Prime Numbers From x Through y 2. Find The nth Prime Number: "
)
while user_input not in ["1", "2"]:
    print("Invalid Action")
    user_input = input(
        "Action 1. Find Prime Numbers From x Through y 2. Find The nth Prime Number: "
    )
if user_input == "1":

    def Digit_Low(low):
        while low.isdigit() is False:
            print("Only Integers Allowed")
            low = input("Enter The Lowest Number You Want To Go To: ")
        return int(low)

    def Digit_High(high):
        while high.isdigit() is False:
            print("Only Integers Allowed")
            high = input("Enter The Highest Number You Want To Go To: ")
        return int(high)

    def Low_Exceeding(low):
        while low > high:
            print("Your Lowest Number Must Be Less Than Your Greatest Number")
            low = input("Enter The Lowest Number You Want To Go To: ")
            low = Digit_Low(low)
        return int(low)

    def High_Deficient(high):
        while high < low:
            print("Your Highest Number Must Be Greater Than Your Lowest Number")
            high = input("Enter The Highest Number You Want To Go To: ")
            high = Digit_High(high)
        return int(high)

    def Exceeding(low, high):
        while low > 10000:
            print("Enter A Number Less Than Or Equal To 10,000")
            low = Digit_Low(low)
            low = Low_Exceeding(low)
        while high > 10000:
            high = input("Enter The Highest Number You Want To Go To: ")
            high = Digit_High(high)
            high = High_Deficient(high)
        return int(low), int(high)

    low = input("Enter The Lowest Number You Want To Go To: ")
    low = Digit_Low(low)
    high = input("Enter The Highest Number You Want To Go To: ")
    high = Digit_High(high)
    low = Low_Exceeding(low)
    high = High_Deficient(high)
    low, high = Exceeding(low, high)
    non_primes = set(j for i in range(2, 8) for j in range(i * 2, high, i))
    primes = (
        [1, 2]
        if low == 1 and high == 2
        else [x for x in range(low, high) if x not in non_primes]
    )
    print(f"Primes From {low} Through {high} Are {primes}")
else:

    def Digit_Prime(prime_index):
        while prime_index.isdigit() is False:
            print("Only Integers Allowed")
            prime_index = input(
                "Enter What Prime Number You Want To See (Up To 10,000): "
            )
        return int(prime_index)

    def Low_Prime(prime_index):
        while prime_index == 0:
            print("Enter A Number Greater Than Or Equal To One")
            prime_index = input("Enter What Prime You Want To See (Up To 10,000): ")
            prime_index = Digit_Prime(prime_index)
        return int(prime_index)

    def High_Prime(prime_index):
        while prime_index > 10000:
            print("Please Enter A Number Less Than Or Equal To 10,000")
            prime_index = input("Enter What Prime You Want To See (Up To 10,000): ")
            prime_index = Digit_Prime(prime_index)
            prime_index = Low_Prime(prime_index)
        return int(prime_index)

    prime_index = input("Enter What Prime You Want To See (Up To 10,000): ")
    prime_index = Digit_Prime(prime_index)
    prime_index = Low_Prime(prime_index)
    prime_index = High_Prime(prime_index)
    non_primes = set(j for i in range(2, 8) for j in range(i * 2, 43730, i))
    primes = [x for x in range(1, 43730) if x not in non_primes]
    print(f"The {prime_index}th Prime Is {primes[prime_index - 1]}")
