def Handle_Game_Type(prompt, options):
    response = input(f"{prompt}: ")
    while response.strip().lower() not in options:
        print("Invalid input. Please try again.")
        response = input(f"{prompt}: ")
    return response.strip().lower()


def Handle_Input(prompt):
    response = input(f"{prompt}: ")
    while response.title() in responses:
        print("You have already entered this")
        response = input(f"{prompt}: ")
    return response.title()


def Results(location_type, item_name):
    correct = (
        [i for i in responses if i in location_type]
        if item_name == "states"
        else [i for i in responses if i in list(location_type.values())]
    )
    incorrect = (
        [i for i in responses if i not in location_type]
        if item_name == "states"
        else [i for i in responses if i not in list(location_type.values())]
    )
    missed_answers = (
        [i for i in location_type if i not in responses]
        if item_name == "states"
        else {
            i: location_type[i]
            for i in location_type
            if location_type[i] not in responses
        }
    )
    score = len(correct)
    percentage = round(score / 50 * 100, 2)

    print()
    print(
        f"You have entered {score} {item_name.removesuffix('s')}(s) correctly out of 50 [{percentage}%]"
    )
    print()
    print("What you entered that was correct:")
    if correct:
        for i in correct:
            print(i)
    else:
        print("You didn't enter anything correctly")
    print()
    print("What you entered that was incorrect:")
    if incorrect:
        for i in incorrect:
            print(i)
    else:
        print("You didn't enter anything incorrectly")
    print()
    print("What you didn't enter:")
    if missed_answers is False:
        print(f"You entered all possible {item_name}")
        return
    if item_name == "states":
        for i in missed_answers:
            print(i)
    else:
        for i in missed_answers.items():
            print(f"{i[0]}: {i[1]}")


game_type = Handle_Game_Type(
    "Would you like to play the states game [s] or the capitals game [c]", ["s", "c"]
)
responses = []
print("Enter 'q' to stop early")

if game_type == "s":
    from states import states

    for i in range(50):
        user_answer = Handle_Input("Enter a state")
        if user_answer == "Q":
            break
        responses.append(user_answer)
    Results(states, "states")
else:
    from random import choice

    from capitals import capitals

    possible_capitals = capitals.copy()
    print("Enter nothing if you don't know the answer")
    for i in range(50):
        state = choice(list(capitals.keys()))
        user_answer = Handle_Input(f"What is the capital of {state}")
        if user_answer == "Q":
            break
        if user_answer != "":
            responses.append(user_answer)
        capitals.pop(state)
    Results(possible_capitals, "capitals")
