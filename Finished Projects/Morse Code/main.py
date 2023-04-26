"""Convert text to morse code and vise versa"""


from morse_code_map import CHARACTER_TO_MORSE_CODE, MORSE_CODE_TO_CHARACTER


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

        error_message = f"""
            Invalid option. Please enter one of the following: {", ".join(str(option) for option in options)}
        """.lstrip()
        print(error_message)


def convert_text_to_morse_code(text: str):
    """
    Summary:
        Convert text to morse code.

    Args:
        text (str): The text to be converted.

    Returns:
        str: The text converted to morse code.
    """

    result = "".join(
        [
            f"{CHARACTER_TO_MORSE_CODE.get(character.upper(), '?')} "
            for character in text
        ]
    )
    if "?" in result:
        error_message = """
            There was an invalid character that cannot be converted to morse code. It will be shown as "?"
        """.lstrip()
        print(error_message)
    return result


def convert_morse_code_to_text(morse_code: str):
    """
    Summary:
        Convert morse code to text.

    Args:
        morse_code (str): The morse code to be converted.

    Returns:
        str: The morse code converted to text.
    """

    result = "".join(
        [MORSE_CODE_TO_CHARACTER.get(morse, "?") for morse in morse_code.split()]
    )
    allowed_characters = ["-", ".", " ", "/"]
    for morse in morse_code:
        if morse not in allowed_characters:
            error_message = """
            There was an invalid sequence of characters passed as input that is not morse code.
            Results may vary because of this.
            """
            print(error_message)
            break
    return result


def main():
    """
    Ask the user for what action they would like to do and convert
    their text based on their action.
    """

    print("An unrecognized character will print out as '?'")

    action = handle_option_input(
        prompt="Action 1. Convert text to morse code 2. Convert morse code to text",
        options=["1", "2"],
    )

    text = input("Enter the text you would like to convert: ")

    action_map = {"1": convert_text_to_morse_code, "2": convert_morse_code_to_text}
    converted_text = action_map[action](text)

    print(f"Result: {converted_text}")


if __name__ == "__main__":
    main()
