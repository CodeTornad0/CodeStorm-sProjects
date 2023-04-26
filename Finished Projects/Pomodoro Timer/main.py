"""Pomodoro timer that runs in the terminal."""


import time
from enum import Enum


def return_formatting(format_code: int) -> str:
    """
    Summary:
        Return text formatting using a format code.

    Args:
        format_code (int): The code for the text format.

    Returns:
        str: The text formatting.
    """

    return f"\x1b[{format_code}m"


class Color(Enum):
    """
    Summary:
        Reset text color, working colors, and resting colors in one location
        to be easily be accessed for printing text.

    Args:
        Enum (class): Enum class for defining a fixed set of color options for use in terminal
        text formatting.
    """

    RESET_TEXT_COLOR = return_formatting(format_code=0)

    # working colors
    GREEN = return_formatting(format_code=32)
    ORANGE = return_formatting(format_code=33)

    # resting colors
    BLUE = return_formatting(format_code=34)
    RED = return_formatting(format_code=31)


def get_time_input(prompt: str) -> dict[str, int]:
    """
    Summary:
        Get the user's input on how long an activity will last.

    Args:
        prompt (str): The prompt the user will be questioned on. This will be to enter
        how long an activity will last.

    Returns:
        dict[str, int]: How long an activity will last in hours,
        minutes, and seconds.
    """

    print(prompt)

    time_in_hours = get_int_input(prompt="Enter how many hours it will take")
    time_in_minutes = get_int_input(prompt="Enter how many minutes it will take")
    time_in_seconds = get_int_input(prompt="Enter how many seconds it will take")

    clear_terminal()

    return {
        "hours": time_in_hours,
        "minutes": time_in_minutes,
        "seconds": time_in_seconds,
    }


def get_int_input(prompt: str) -> int:
    """
    Summary:
        Get an integer input. This is used for getting how long an activity
        will take in an unit of time.

    Args:
        prompt (str): The prompt the user will be prompted on while asking for input.

    Returns:
        int: The time it will take in a time unit.
    """

    while True:
        time_allocated = input(f"{prompt}: ")
        if (
            time_allocated.isdigit() and int(time_allocated) < 60
        ):  # 60 seconds or minutes is an invalid time because it goes to next unit of time
            # if it is greater than 59
            # 60 hours is considered invalid also because of this condition
            return int(time_allocated)

        print("Invalid input. Enter an integer less than 59")


def clear_terminal() -> None:
    """Clear the terminal of all text."""
    print("\033c", end="")


def run_timer(time_allocated: dict[str, int], activity: str) -> None:
    """
    Summary:
        Run the timer by calculating the time left, displaying the timer,
        and updating the time left.

    Args:
        time_allocated (dict[str, int, str, int, str, int]): The time for the timer to run in hours,
        minutes, and seconds.

        activity (str): The activity the timer is running for.
    """

    clear_terminal()

    hours = time_allocated["hours"]
    minutes = time_allocated["minutes"]
    seconds = time_allocated["seconds"]
    total_seconds = hours * 3600 + minutes * 60 + seconds

    activity = f"{activity.title()}ing..."  # work -> Working...

    text_colors: list[str] = {
        "Working...": [Color.GREEN.value, Color.ORANGE.value],
        "Resting...": [Color.BLUE.value, Color.RED.value],
    }[activity]

    for seconds_left in range(total_seconds, -1, -1):
        seconds_left_low_or_high = {seconds_left > 3: 0, seconds_left < 4: 1}[True]
        # 3 and 4 are used because they are low numbers
        # 0 gets the color for when the timer is not ending soon while 1 does the opposite
        text_color = text_colors[seconds_left_low_or_high]

        display_timer(
            text_color=text_color, activity=activity, time_allocated=time_allocated
        )

        time.sleep(1)
        seconds, minutes, hours = update_time_remaining(seconds, minutes, hours)

        time_allocated = {"hours": hours, "minutes": minutes, "seconds": seconds}

        clear_terminal()

    print(Color.RESET_TEXT_COLOR.value, end="")


def display_timer(
    text_color: str, activity: str, time_allocated: dict[str, int]
) -> None:
    """
    Summary:
        Print out the time and the activity of the timer.

    Args:
        text_color (str): The color the text is printed in.
        activity (str): The activity the timer is running for.
        time_allocated (dict[str, int, str, int, str, int]): The time in hours, minutes,
        and seconds.
    """

    print(f"{text_color}{activity}")

    print(
        f"{text_color}{time_allocated['hours']:02}:{time_allocated['minutes']:02}:"
        f"{time_allocated['seconds']:02}"
    )


def update_time_remaining(seconds: int, minutes: int, hours: int) -> list[int]:
    """
    Summary:
        Update the time remaining for the timer.

    Args:
        seconds (int): The number of seconds left.
        minutes (int): The number of minutes left.
        hours (int): The number of hours left.

    Returns:
        list[int]: A list of the seconds, minutes, and hours left.
    """

    seconds -= 1

    if seconds < 0:
        seconds = 59
        minutes -= 1

    if minutes < 0:
        minutes = 59
        hours -= 1

    return [seconds, minutes, hours]


def main() -> None:
    """
    Run the program by asking for the time working and resting and
    running a timer for each of those times.
    """

    time_working = get_time_input(prompt="Enter time given for working")
    time_resting = get_time_input(prompt="Enter time given for resting")

    input("Press enter to start the timer")

    run_timer(time_allocated=time_working, activity="work")

    print(f"{Color.BLUE.value}Done! Break starting")
    time.sleep(1)

    run_timer(time_allocated=time_resting, activity="rest")

    print(f"{Color.GREEN.value}Break is over")


if __name__ == "__main__":
    main()
