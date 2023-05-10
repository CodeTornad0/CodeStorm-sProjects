"""
Has the player guess a secret code made of three digits with each digit 
either one, two, three, or four until they lose all their guesses or win. 
The player gets hints if their guess was wrong.
"""


import random


HIGHEST_CODE_NUMBER = 4
LOWEST_CODE_NUMBER = 1
CODE_LENGTH = 3
PLAYER_GUESSES = 3

VALID_CHARACTERS = ["1", "2", "3", "4"]


def generate_secret_code() -> str:
    """
    Summary:
        Generate a three digit code with each digit either one, two, three, or four.

    Returns:
        str: The secret code.
    """

    code_digits = [
        str(random.randint(LOWEST_CODE_NUMBER, HIGHEST_CODE_NUMBER))
        for _ in range(CODE_LENGTH)
    ]
    secret_code = "".join(code_digits)
    return secret_code


def player_guess_valid(player_guess: str) -> bool:
    """
    Summary:
        Check if the player guess is valid by checking if it is a valid length (3 digits) and
        does not include any characters that are not one, two, three, or four.

    Args:
        player_guess (str): The player's guess to be validated.

    Returns:
        bool: If the player's guess is valid or not.
    """

    player_guess_length_correct = len(player_guess) == CODE_LENGTH
    player_guess_characters_valid = all(
        character in VALID_CHARACTERS for character in player_guess
    )
    return player_guess_length_correct and player_guess_characters_valid


def get_player_guess(prompt: str) -> str:
    """
    Summary:
        Get the player's guess by prompting the player, checking if their guess is valid,
        and returning it if it is, while otherwise prompting the player to renter it.

    Args:
        prompt (str): The prompt the player is asked.

    Returns:
        str: The player's guess.
    """

    while True:
        player_guess = input(prompt)
        if player_guess_valid(player_guess=player_guess):
            return player_guess

        print()
        print(
            "Invalid input. The length of the guess must be three digits with each digit either"
            "one, two, three, or four"
        )
        print()


def return_player_guess_hints(secret_code: str, player_guess: str) -> str:
    """
    Summary:
        Returns hints on the answer. The hints say if the player got any characters
        correct and where.

    Args:
        secret_code (str): The answer that the player is guessing.
        player_guess (str): The guess the player entered.

    Returns:
        str: Hints on what the player got correct.
    """

    player_guess_hints = [
        f"The digit at position {index_of_digit + 1} is correct\n"
        for index_of_digit, digit in enumerate(player_guess)
        if digit == secret_code[index_of_digit]
    ]

    if not player_guess_hints:
        player_guess_hints = ["None of your digits are in the correct place\n"]

    return "".join(player_guess_hints)


def run_intro() -> None:
    """
    Give information on where to find more about the game, prompts the player to start,
    and gives the player the number of guesses they have.
    """

    print("Refer to the 'README' file for information on the game")
    input("Press enter to start")

    print()
    print(f"You have {PLAYER_GUESSES} guesses")
    print()


def main() -> None:
    """
    Run the game by generating a secret code, running the intro, repeating the game as long as
    the player has guesses, getting the player's guess, and showing the results of their guess
    by it either correct, incorrect and hints on the answer, or incorrect and they ran out
    of guesses.
    """

    three_digit_secret_code = generate_secret_code()

    run_intro()

    for player_guesses in range(PLAYER_GUESSES, 0, -1):
        player_code_guess = get_player_guess(prompt="Guess the code: ")

        if player_code_guess == three_digit_secret_code:
            print()
            print("You guessed the code correctly!")
            return

        # checks if the game has not ended by checking if when removing
        # a guess from the player, the player still has guesses
        # this is needed because the guesses remaining only go down by one once the
        # entirety of the code inside of the loop finishes
        game_has_not_ended = player_guesses - 1 > 0
        if game_has_not_ended:
            print()
            print(
                f"Your guess was incorrect. You have {player_guesses - 1} guess(es) left"
            )
            print(
                return_player_guess_hints(
                    secret_code=three_digit_secret_code, player_guess=player_code_guess
                )
            )

    print()
    print("You lost all of your guesses!")
    print(f"The correct answer was {three_digit_secret_code}")


if __name__ == "__main__":
    main()
