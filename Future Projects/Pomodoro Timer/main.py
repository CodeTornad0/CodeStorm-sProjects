"""Pomodoro timer that runs in the terminal"""

# ask user for work time
# ask user for break time
# change text color when getting close to end and different colors for work and break
import time


def clear_terminal() -> None:
    """Clear the terminal of all text."""
    print("\033c", end="")


clear_terminal()
for seconds in range(5, -1, -1):
    print(f"00:00:{seconds:02}")
    time.sleep(1)
    clear_terminal()
