import random
import sys
import threading
import time


def clear_terminal() -> None:
    """Clear the terminal of all text."""
    print("\033c", end="")


def loading_animation(
    loading_target: str = None,
    loading_time: float = None,
    animation_speed: float = None,
) -> None:
    """
    Summary:
        Print a loading animation in the terminal.

    Args:
        loading_target (str, optional): What is being loaded. For example: "Finishing Setup."
        Defaults to None to then be defaulted to "Loading."

        loading_time (float, optional): The amount of time it takes for the animation to finish.
        Defaults to None to then be defaulted to 0.8.

        animation_speed (float, optional): The speed that the loading characters change
        making it seem like it is running at a certain pace.
        The smaller the size - the faster it changes.
        Defaults to None to then be defaulted to 0.3.

    Requirements:
        random
        threading
        time

    Example:
        loading_animation(loading_target="Fixing Errors", loading_time=3.4, animation_speed=0.35)
    """

    # Helper function to validate input
    def validate_time_speed(time_speed: float, time_name: str):
        """
        Summary:
            Check if the variable passed is a number greater than zero.

        Args:
            time_speed (float): To be validated if it is a number greater than zero.
            The time that it takes for something is called "time_speed" here.
            For example, loading_time can be the time_speed.

            time_name (str): Used to tell the user what variable is invalid.
            time_name = the name of the amount of time being checked or time_speed.
            For example: "loading time."

        Raises:
            ValueError: If variable is not a number greater than zero.

        Returns:
            Float if the number is valid.
            Otherwise, print an error message and return False.
        """

        error = f"Loading {time_name} must be a number"
        try:
            time_speed = float(
                time_speed
            )  # raises ValueError here if time_speed is not a number
            if time_speed < 0:
                error = f"Loading {time_name} must be a positive number"
                raise ValueError()

            return time_speed
        except ValueError:
            print(f"Error: {error}")
            return False

    # Set default values if none are provided
    if loading_target is None:
        loading_target = "Loading"
    if loading_time is None:
        loading_time = 1.3
    if animation_speed is None:
        animation_speed = 0.3

    # Validate input
    loading_time = validate_time_speed(time_speed=loading_time, time_name="time")
    animation_speed = validate_time_speed(time_speed=animation_speed, time_name="speed")
    if not all([animation_speed, loading_time]):
        return

    # The period of time that the animation will run
    wait = threading.Thread(target=lambda: time.sleep(loading_time))
    wait.start()

    special_characters = ["*", "?", "!", "$", "«««", "»»»", "</>", "", "¿"]

    # Start the loading animation
    while wait.is_alive():
        for character in ["\\", "|", "/"]:
            if random.randint(1, 1000) == 1000:
                character = random.choice(
                    special_characters
                )  # randomly choose a special character in rare instances as an easter egg
            clear_terminal()
            print(f"{loading_target}... {character}")
            time.sleep(animation_speed)

    clear_terminal()
    print("Process complete!")
    return


def print_animation(text: str, print_speed: float = None) -> None:
    """
    Summary:
        Print text like a video game speech bubble.

    Args:
        text (str): Print out this text.
        print_speed (float, optional): The speed of which text is printed.
        Defaults to None to then be defaulted to 0.02.
        The smaller size of the print speed - the faster the print speed is.

    Requirements:
        time
    """

    if print_speed is None:
        print_speed = 0.02

    # check if print_speed is a number and return out of the function if not
    try:
        float(print_speed)
    except ValueError:
        print("Printing speed must be a number")
        return

    text = str(text)  # incase text is not a string
    current_index = 0

    while current_index <= len(text):
        clear_terminal()
        print(text[0:current_index])
        current_index += 1
        time.sleep(print_speed)
    print()


def handle_option_input(prompt: str, options: list):
    """
    Summary:
        Prompt the user for an option and return the valid option selected.

    Args:
        prompt (str): The prompt the user will be prompted on.
        options (list): The options available to the user.

    Returns:
        str: The option the user has selected.
    """

    while True:
        user_input = input(f"{prompt}: ")
        if user_input in options:
            return user_input
        error_message = f"Invalid option. Please enter one of the following: \
                        {', '.join(str(i) for i in options)}"
        print(error_message)


# validate if an input is an integer
def handle_int_input(prompt):
    while True:
        number = input(f"{prompt}: ")
        if number.isdigit():
            return int(number)
        print("Invalid input. Enter an integer")


# ask for input and validate if the input is a float
def handle_float_input(number, prompt):
    while True:
        number = input(f"{prompt}: ")
        try:
            return float(number)
        except ValueError:
            print("Invalid input. Input must be a number")


# validate input from a list of commands/actions
def handle_command_input(actions, filepath, restart_command):
    user_command = input("Action: ").lower().strip()
    if user_command in ["q", "quit"]:
        sys.exit()
    if user_command in ["r", "restart", filepath]:
        restart_command()
    if user_command == "?":
        formatted_actions = [
            f"{k}. {v.__name__.replace('_', ' ').title()}" for k, v in actions.items()
        ]
        print(
            f"You have the following options for your input: {' '.join(formatted_actions)}"
        )
        return
    if user_command not in list(map(str, list(actions))):
        print("Invalid Action")
        return
    user_command = int(user_command)
    action = actions.get(user_command)
    action()
