import random
from time import sleep


def Clear_Terminal():
    print("\033c", end="")


def Handle_Options(prompt, options):
    option = input(f"{prompt}: ")
    while option not in options:
        print("Invalid option. Please enter 'c' or 'd'")
        option = input(f"{prompt}: ")
    return option


def Handle_Input(prompt):
    def Input_Is_Valid():
        return float(response) >= 1

    while True:
        response = input(f"{prompt}: ")
        try:
            if time_delay_choice == "c" or Input_Is_Valid():
                return float(response)
            print("Invalid input. Please enter a number greater than or equal to one")
        except ValueError:
            print("Invalid input. Please enter a number")


character_order = []
characters = input("Enter a list of characters separated with spaces: ").split()

prompts = {
    "c": "Enter the time delay",
    "d": "Enter a number greater than or equal to one [the time delay will be the length of the order divided by this input]",
}
time_delay_choice = Handle_Options(
    "Would you like your time to memorize the order a constant number [c] or dependent on the length of the order [d]",
    ["c", "d"],
)
time_delay = Handle_Input(prompts[time_delay_choice])

Clear_Terminal()
print("Enter a space between each character")
print(
    "Don't enter any characters until prompted [if you do it will count your answer as wrong]"
)
print("Memorize the order")
input("Press enter to start")

while True:
    Clear_Terminal()
    character_order.append(random.choice(characters))
    print(f"The order is: {', '.join(character_order)}")
    if time_delay_choice == "d":
        time_delay = len(character_order) / time_delay
    sleep(time_delay)
    Clear_Terminal()

    user_order = input("Enter the order of characters separated by spaces: ").split()
    if user_order != character_order:
        score = len(character_order) - 1 if len(character_order) - 1 > -1 else 0
        print(f"Wrong order! The order was {', '.join(character_order)}")
        print(f"Your score is {score}")
        break
    print("Correct!")
    sleep(0.5)
