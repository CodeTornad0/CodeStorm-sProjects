from sys import maxsize


def Handle_Option(prompt, options):
    user_input = input(f"{prompt}: ")
    while user_input not in options:
        print("Invalid option. Please enter 'c' or 'f'")
        user_input = input(f"{prompt}: ")
    return user_input


def Handle_Input(prompt):
    def Input_Is_Valid_Year():
        return (
            user_input.isdigit(),
            False if not user_input.isdigit() else int(user_input) > 1581,
        )

    user_input = input(f"{prompt}: ")
    while not all(Input_Is_Valid_Year()):
        print(
            f"Invalid year. {'Please enter a integer' if not Input_Is_Valid_Year()[0] else 'Leap years only occur after 1581'}"
        )
        user_input = input(f"{prompt}: ")
    return int(user_input)


def Handle_Errors(start, end):
    def Start_Is_Less_Than_End(start, end):
        while start > end:
            print(
                "Invalid year. Your starting year must be less or equal to your ending year"
            )
            start, end = Handle_Input("Enter the starting year"), Handle_Input(
                "Enter the ending year"
            )
        return start, end

    def Input_Under_Maxsize(start, end):
        while end - start > maxsize:
            print("Invalid year. Your starting and ending year is too large to compute")
            start, end = Handle_Input("Enter the starting year"), Handle_Input(
                "Enter the ending year"
            )
            start, end = Start_Is_Less_Than_End(start, end)
        return start, end

    def Input_Exceeds_Memory(start, end):
        while True:
            try:
                list(range(start, end + 1))
                break
            except MemoryError:
                print(
                    "Invalid year. Your starting and ending year is too large and is not possible with the amount of memory available"
                )
                start, end = Handle_Input("Enter the starting year"), Handle_Input(
                    "Enter the ending year"
                )
                start, end = Start_Is_Less_Than_End(start, end)
                start, end = Input_Under_Maxsize(start, end)
        return start, end

    start, end = Start_Is_Less_Than_End(start, end)
    start, end = Input_Under_Maxsize(start, end)
    start, end = Input_Exceeds_Memory(start, end)
    return start, end


def Is_Leap_Year(user_year):
    return user_year % 400 == 0 or user_year % 4 == 0 and user_year % 100 != 0


option = Handle_Option(
    "Would you like to calculate if a year is a leap year [c] or find leap years in a list of years [f]",
    ["c", "f"],
)
if option == "c":
    year = Handle_Input("Year")
    if Is_Leap_Year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    start_year, end_year = Handle_Input("Enter the starting year"), Handle_Input(
        "Enter the ending year"
    )
    start_year, end_year = Handle_Errors(start_year, end_year)
    leap_years = [
        year for year in range(start_year, end_year + 1) if Is_Leap_Year(year)
    ]
    if leap_years:
        print(f"{leap_years} are(is a) leap year(s)")
    else:
        print("There are no leap years")
