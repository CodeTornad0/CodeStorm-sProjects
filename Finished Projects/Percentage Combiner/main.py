def Handle_Input(prompt):
    while True:
        percentage = input(f"{prompt}: ")
        try:
            return float(percentage)
        except ValueError:
            print("Invalid input. Input must be a number")


percentage1 = Handle_Input("Enter the first percentage")
percentage2 = Handle_Input("Enter the second percentage")
percentage1_worth = Handle_Input("What percentage is the first percentage worth")
percentage2_worth = Handle_Input("What percentage is the second percentage worth")
result = round(
    (percentage1 * percentage1_worth / 100) + (percentage2 * percentage2_worth / 100), 2
)
print(
    f"{percentage1_worth}% of {percentage1}% + {percentage2_worth}% of {percentage2}% = {result}%"
)
