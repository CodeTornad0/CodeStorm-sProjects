"""An animation of a slinky falling down."""


import time


SLINKY_LENGTH = 5


def clear_terminal() -> None:
    """Clear the terminal of all text."""

    print("\033c", end="")


def print_slinky_dashes_then_dots() -> None:
    """Print the slinky from the dashes then dots."""

    for step in range(SLINKY_LENGTH):
        # move cursor to bottom of terminal
        print(f"\033[{str(SLINKY_LENGTH + 2)};0H", end="")
        print("-" * (SLINKY_LENGTH - step - 1), end="")  # print dashes
        print("." * (step + 1))  # print dots
        time.sleep(0.1)


def print_slinky_dots_then_dashes() -> None:
    """Print the slinky from the dots then dashes."""

    for step in range(SLINKY_LENGTH):
        # move cursor to bottom of terminal
        print(f"\033[{str(SLINKY_LENGTH + 2)};0H", end="")
        print("." * step, end="")  # print dots
        print("-" * (SLINKY_LENGTH - step))  # print dashes
        time.sleep(0.1)


def main():
    """Print the slinky using both print animations."""

    while True:
        print_slinky_dashes_then_dots()
        print_slinky_dots_then_dashes()


if __name__ == "__main__":
    main()
