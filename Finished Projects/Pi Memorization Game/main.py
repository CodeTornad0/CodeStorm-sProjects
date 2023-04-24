"""Memorization game with the digits of pi."""


import time


PI = "\
3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534\
2117067\
"


def clear_terminal() -> None:
    """Clears all text in the terminal."""
    print("\033c", end="")


def main() -> None:
    """
    Run the program by printing instructions, and starting the main loop by
    clearing the terminal, calculating the digits that the user has to memorize,
    printing out that order for the user to memorize, giving the user time to memorize,
    asking the user for the answer, and giving the user the results of their answer.
    """

    print(
        "Do not enter anything until prompted to do so. Entering text could cause your answer to"
        " sometimes not be correct or the text to not be printed properly"
    )
    print("Memorize the digits of pi")
    input("Press enter to start")

    digits_memorized = 4  # the . is counted as a digit memorized

    while True:
        clear_terminal()

        pi_digits_to_memorize = PI[0:digits_memorized]
        print("The digits are: ", end="")
        for digit in pi_digits_to_memorize:
            print(digit, end="")
            time.sleep(0.33)
        print()

        time_for_memorization = len(pi_digits_to_memorize) * 0.5
        time.sleep(time_for_memorization)
        clear_terminal()

        user_order = input("Enter the order of the digits of pi provided: ")
        if user_order != pi_digits_to_memorize:
            score = (
                len(pi_digits_to_memorize) - 1 if len(pi_digits_to_memorize) != 4 else 0
            )
            # -1 removes the . as a digit memorized
            # the != 4 makes sure that the user did not lose on the first round, if they did
            # it counts it as 0 because they could not memorize the first 3 digits

            print(f"Wrong order! The order was {pi_digits_to_memorize}")
            print(f"Your score is {score}")
            break

        print("Correct!")
        digits_memorized += 1
        if digits_memorized == 101:
            print("Yon memorized all digits of pi up to the 100th digit!")
            break
        time.sleep(0.5)


if __name__ == "__main__":
    main()
