"""Generate a password."""


import random


def generate_password(password_length: int = None):
    """
    Summary:
        Generate a password with the length being a given length.

    Args:
        password_length (int, optional): The length of the generated password.
        Defaults to None to then be defaulted to 12.
    """

    if password_length is None:
        password_length = 12

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    numbers = "1234567890"
    symbols = "!@#$%^&*()`~-=_+[]{}|;:,./<>?"
    characters = random.sample(lower + upper + numbers + symbols, password_length)

    password = ""
    for character in characters:
        password += character
    print(f"Generated Password: {password}")
