"""Check the strength of a given password"""


import getpass
import os
import string

FILE_PATH = os.path.dirname(os.path.realpath(__file__))


def print_recommendations() -> None:
    """Print out recommendations for a higher rating password."""

    print()
    print("--- Recommendations ---")
    print("1. Add variety")
    print(
        "This includes lowercase and uppercase letters, numbers, and special characters"
    )
    print("2. Add length")
    print(
        "You can take phrases or sentences and put them as passwords. Use a password manager"
    )


def main() -> None:
    """
    Determines the password's strength based on length and character variety.
    If the password is not perfect, provides recommendations.
    """

    print("Your password will not be displayed. Do not be worried if you do not see it")
    password = getpass.getpass(prompt="Enter a password: ")

    if " " in password:
        print("Passwords cannot contain spaces.")
        return
    if "\t" in password:
        print("Passwords cannot contain tabs.")
        return

    password_has_upper_case = any(character.isupper() for character in password)
    password_has_lower_case = any(character.islower() for character in password)
    password_has_digits = any(character in string.digits for character in password)
    password_has_special_character = any(
        character in string.punctuation for character in password
    )
    characters = [
        password_has_upper_case,
        password_has_lower_case,
        password_has_digits,
        password_has_special_character,
    ]

    with open(
        f"{FILE_PATH}/common_passwords.txt",  # this does not work without using FILE_PATH
        "r",  # even though it is in the same workspace
        encoding="utf-8",
    ) as file:
        common_passwords = file.read().splitlines()[
            55:
        ]  # [55:] skips the first 55 lines of the file

    if password in common_passwords:
        print(
            "This password has been breached before and is in a list of common passwords"
        )
        print("Score: 0 / 7 (0%)")
        return

    # get() will return 0 if none of the statements are true making the score not increase
    password_length = len(password)
    increase_score_by_length = {
        password_length > 10: 1,
        password_length > 14: 2,
        password_length > 16: 3,
        password_length > 20: 4,
    }.get(True, 0)

    # sees how much variety is in the password from the amount of differentiating characters used
    # like uppercase, lowercase, numbers, and special characters
    increase_score_by_special_characters = {
        sum(characters) > 1: 1,
        sum(characters) > 2: 2,
        sum(characters) > 3: 3,
    }.get(True, 0)

    password_strength = increase_score_by_length + increase_score_by_special_characters
    password_grade = {
        password_strength < 4: "The password is weak",
        password_strength == 4: "The password is okay",
        password_strength == 5: "The password is good",
        password_strength > 5: "The password is great",
    }.get(True)

    print(password_grade)
    print(f"Score: {password_strength} / 7 ({round(password_strength / 7 * 100, 2)}%)")

    if password_strength != 7:
        print_recommendations()


if __name__ == "__main__":
    main()
