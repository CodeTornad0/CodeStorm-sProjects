def Convert_Time(input_time, input_unit, decimal_places):
    """
    Convert time units to other units.
    Input: input_time: float, the amount of time in the input unit.
           input_unit: string, the input unit of time, must be one of the keys in the conversions dictionary
           decimal_places: int, the number of decimal places to round to
    Output: the time in all units
    """

    # Initialize the dictionary that contains the conversion factors or divisors
    conversions = {
        "nanoseconds": input_time / 1000000000,
        "microseconds": input_time / 1000000,
        "milliseconds": input_time / 1000,
        "seconds": input_time,
        "minutes": input_time * 60,
        "hours": input_time * 60 * 60,
        "days": input_time * 60 * 60 * 24,
        "weeks": input_time * 60 * 60 * 24 * 7,
        "fortnights": input_time * 60 * 60 * 24 * 14,
        "months": input_time * 60 * 60 * 24 * 30,
        "years": input_time * 60 * 60 * 24 * 365,
        "decades": input_time * 60 * 60 * 24 * 365 * 10,
        "centuries": input_time * 60 * 60 * 24 * 365 * 100,
        "millenniums": input_time * 60 * 60 * 24 * 365 * 1000,
    }

    # Convert the time
    seconds = conversions[input_unit]
    milliseconds = round(seconds * 1000, decimal_places)
    microseconds = round(milliseconds * 1000, decimal_places)
    nanoseconds = round(milliseconds * 1000000, decimal_places)
    minutes = round(seconds / 60, decimal_places)
    hours = round(minutes / 60, decimal_places)
    days = round(hours / 24, decimal_places)
    weeks = round(days / 7, decimal_places)
    fortnights = round(weeks / 2, decimal_places)
    years = round(days / 365, decimal_places)
    months = round(years * 12, decimal_places)
    decades = round(years / 10, decimal_places)
    centuries = round(decades / 10, decimal_places)
    millenniums = round(centuries / 10, decimal_places)

    # Store the converted time
    converted_values = {
        "nanoseconds": nanoseconds,
        "microseconds": microseconds,
        "milliseconds": milliseconds,
        "seconds": seconds,
        "minutes": minutes,
        "hours": hours,
        "days": days,
        "weeks": weeks,
        "fortnights": fortnights,
        "months": months,
        "years": years,
        "decades": decades,
        "centuries": centuries,
        "millenniums": millenniums,
    }

    # Get the user's choice of how to print the converted values
    print_method = (
        input(
            "Would you like to print out all the information [a] or a specific time unit [u]: "
        )
        .lower()
        .strip()
    )

    # Check for invalid input
    while print_method not in ["a", "u"]:
        print(
            "Invalid choice. Please enter either 'a' to print all the information or 'u' to print a specific time unit."
        )
        print_method = (
            input(
                "Would you like to print out all the information [a] or a specific time unit [u]: "
            )
            .lower()
            .strip()
        )

    # Print the values based on the user's choice
    if print_method == "a":
        for val in converted_values.items():
            print(f"{val[1]:,} {val[0]}")
    else:
        input_unit = input("Enter the time unit: ")
        input_unit = Check_String_Input(input_unit)
        print(f"{converted_values[input_unit]:,} {input_unit}")


# Check for errors in the time_value input
def Check_Float_Input(number):
    while True:
        try:
            return float(number)
        except ValueError:
            print("Invalid time value. Please enter a valid numerical value.")
            number = input("Enter the amount of time: ")


# Check for errors in the time_unit input
def Check_String_Input(value):
    UNITS = [
        "nanoseconds",
        "microseconds",
        "milliseconds",
        "seconds",
        "minutes",
        "hours",
        "days",
        "weeks",
        "fortnights",
        "months",
        "years",
        "decades",
        "centuries",
        "millenniums",
    ]
    while value not in UNITS:
        print(
            f"Invalid time unit. Please enter a valid time unit from the list: {', '.join(UNITS)}."
        )
        value = input("Enter the time unit: ")
    return value


# Check for errors in the amount_of_decimals input
def Check_Int_Input(number):
    while number.isdigit() is False:
        print("Invalid decimal places. Please enter an integer value.")
        number = input(
            "Enter the amount of decimal places in each measurement [increase this to increase the accuracy of the calculations]: "
        )
    return int(number)


# Ask for input and run error checking
time_value = input("Enter the amount of time: ")
time_value = Check_Float_Input(time_value)
time_unit = input("Enter the time unit: ")
time_unit = Check_String_Input(time_unit)
amount_of_decimals = input(
    "Enter the amount of decimal places in each measurement [increase this to increase the accuracy of the calculations]: "
)
amount_of_decimals = Check_Int_Input(amount_of_decimals)

# Say disclaimer and convert the time_value
print(
    "Keep in mind that a very large or small number will revert to scientific notation"
)
Convert_Time(time_value, time_unit, amount_of_decimals)
