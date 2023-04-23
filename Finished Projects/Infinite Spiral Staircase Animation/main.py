"""An animation of an infinite spiral staircase."""


import time

STEPS = 5
DELAY_TIME = 0.1


# dots are stairs
# dashes are walls and railings


def print_top_of_staircase() -> None:
    """Print the top of the staircase."""

    print("Here is a house that has a reallllly tall staircase to get to")
    # print house
    print(" ___")
    print("/   \\")
    print("|ㅁ |")

    time.sleep(1)


def print_staircase_dashes_then_dots() -> None:
    """Print the staircase's dashes and then dots."""

    for step in range(STEPS):
        dashes = "-" * (STEPS - step - 1)
        dots = "." * (step + 1)
        print(f"{dashes}{dots}")
        time.sleep(DELAY_TIME)


def print_staircase_dots_then_dashes() -> None:
    """Print the staircase's dots then dashes."""

    for step in range(STEPS):
        dots = "." * step
        dashes = "-" * (STEPS - step)
        print(f"{dots}{dashes}")
        time.sleep(DELAY_TIME)


def main():
    """Run the program by printing the staircase's stairs, walls, and railing."""

    print_top_of_staircase()

    try:
        while True:
            print_staircase_dashes_then_dots()
            print_staircase_dots_then_dashes()
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()
