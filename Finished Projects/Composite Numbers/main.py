user_input = input(
    "Action 1. Find Composite Numbers From x Through y 2. Find The nth Composite Number: "
)
while user_input not in ["1", "2"]:
    print("Invalid Action")
    user_input = input(
        "Action 1. Find Composite Numbers From x Through y 2. Find The nth Composite Number: "
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
            low = input("Enter The Lowest Number You Want To Go To: ")
            low = Digit_Low(low)
            low = Low_Exceeding(low)
        while high > 10000:
            print("Enter A Number Less Than Or Equal To 10,000")
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
    composites = list(set(j for i in range(2, 8) for j in range(i * 2, high, i)))
    composites.sort()
    print(f"Composites From {low} Through {high} Are {composites}")
else:

    def Digit_Composite(composite_index):
        while composite_index.isdigit() is False:
            print("Only Integers Allowed")
            composite_index = input(
                "Enter What Composite Number You Want To See (Up To 10,000): "
            )
        return int(composite_index)

    def Low_Composite(composite_index):
        while composite_index == 0:
            print("Enter A Number Greater Than Or Equal To One")
            composite_index = input(
                "Enter What Composite You Want To See (Up To 10,000): "
            )
            composite_index = Digit_Composite(composite_index)
        return int(composite_index)

    def High_Composite(composite_index):
        while composite_index > 10000:
            print("Please Enter A Number Less Than Or Equal To 10,000")
            composite_index = input(
                "Enter What Composite You Want To See (Up To 10,000): "
            )
            composite_index = Digit_Composite(composite_index)
            composite_index = Low_Composite(composite_index)
        return int(composite_index)

    composite_index = input("Enter What Composite You Want To See (Up To 10,000): ")
    composite_index = Digit_Composite(composite_index)
    composite_index = Low_Composite(composite_index)
    composite_index = High_Composite(composite_index)
    composite = list(set(j for i in range(2, 8) for j in range(i * 2, 43730, i)))
    print(f"The {composite_index}th Composite Is {composite[composite_index - 1]}")
