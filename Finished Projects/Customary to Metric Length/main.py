"""Convert customary to metric and vise versa"""


CUSTOMARY_LENGTH_UNITS = ["inches", "feet", "yards", "miles"]
METRIC_LENGTH_UNITS = [
    "millimeters",
    "centimeters",
    "decimeters",
    "meters",
    "dekameters",
    "hectometers",
    "kilometers",
]
LENGTH_UNITS = {"1": CUSTOMARY_LENGTH_UNITS, "2": METRIC_LENGTH_UNITS}


def handle_option_input(prompt: str, options: list[str]) -> str:
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


def get_conversion_direction() -> str:
    """
    Summary:
        Prompt the user if they want to go from customary to metric or vise versa and
        return the valid option selected.

    Args:
        options (list): The options available to the user.

    Returns:
        str: The option the user has selected.
    """

    conversion_direction = handle_option_input(
        prompt="Would you like to convert 1. customary to metric or 2. convert metric to customary",
        options=["1", "2"],
    )
    return conversion_direction


def get_converting_length() -> float:
    """
    Summary:
        Get the length the user will convert.

    Returns:
        float: The length to be converted.
    """

    while True:
        converting_length = input("Enter the length you would like to convert: ")
        try:
            return float(converting_length)
        except ValueError:
            print("Invalid input. Input must be a number")


def get_length_unit(conversion_direction: str) -> str:
    """
    Summary:
        Get the unit converting number is in.

    Args:
        conversion_direction (str): The option to convert customary to metric or vise versa.
        Used to see what the user has available to them for what the converting number's unit is.

    Returns:
        str: The unit of what the converting number is.
    """

    length_unit = handle_option_input(
        prompt="Enter the unit that the previous number you have entered is in",
        options=LENGTH_UNITS[conversion_direction],
    )
    return length_unit


def convert_customary_length_to_metric(length: float, unit: str) -> None:
    """
    Summary:
        Convert customary length to metric.

    Args:
        length (float): The length that will be converted.
        unit (str): The unit of the length being converted.
    """

    customary_to_metric_in_millimeters = {
        "inches": 25.4,
        "feet": 304.8,
        "yards": 914.4,
        "miles": 1.609344e6,
    }

    metric_units_in_millimeters = {
        "millimeters": 1 / 1,
        "centimeters": 1 / 10,
        "decimeters": 1 / 100,
        "meters": 1 / 1000,
        "dekameters": 1 / 10_000,
        "hectometers": 1 / 100_000,
        "kilometers": 1 / 1_000_000,
    }

    converted_length_in_metric_units = {
        "millimeters": customary_to_metric_in_millimeters[unit]
        * length
        * metric_units_in_millimeters["millimeters"],
        "centimeters": customary_to_metric_in_millimeters[unit]
        * length
        * metric_units_in_millimeters["centimeters"],
        "decimeters": customary_to_metric_in_millimeters[unit]
        * length
        * metric_units_in_millimeters["decimeters"],
        "meters": customary_to_metric_in_millimeters[unit]
        * length
        * metric_units_in_millimeters["meters"],
        "dekameters": customary_to_metric_in_millimeters[unit]
        * length
        * metric_units_in_millimeters["dekameters"],
        "hectometers": customary_to_metric_in_millimeters[unit]
        * length
        * metric_units_in_millimeters["hectometers"],
        "kilometers": customary_to_metric_in_millimeters[unit]
        * length
        * metric_units_in_millimeters["kilometers"],
    }

    for key, value in converted_length_in_metric_units.items():
        print(f"{key.capitalize()}: {round(value, 3):,}")


def convert_metric_length_to_customary(length: float, unit: str) -> None:
    """
    Summary:
        Convert metric length to customary.

    Args:
        length (float): The length that will be converted.
        unit (str): The unit of the length being converted.
    """

    metric_to_customary_in_inches = {
        "millimeters": 0.03937008,
        "centimeters": 0.3937008 * 10,
        "decimeters": 0.03937008 * 100,
        "meters": 0.03937008 * 1000,
        "dekameters": 0.03937008 * 10_000,
        "hectometers": 0.03937008 * 100_000,
        "kilometers": 0.03937008 * 1_000_000,
    }

    customary_units_in_inches = {
        "inches": 1 / 1,
        "feet": 1 / 12,
        "yards": 1 / 36,
        "miles": 1 / 63360,
    }

    converted_length_in_customary_units = {
        "inches": metric_to_customary_in_inches[unit]
        * length
        * customary_units_in_inches["inches"],
        "feet": metric_to_customary_in_inches[unit]
        * length
        * customary_units_in_inches["feet"],
        "yards": metric_to_customary_in_inches[unit]
        * length
        * customary_units_in_inches["yards"],
        "miles": metric_to_customary_in_inches[unit]
        * length
        * customary_units_in_inches["miles"],
    }

    for key, value in converted_length_in_customary_units.items():
        print(f"{key.capitalize()}: {round(value, 3):,}")


def main() -> None:
    """
    Run the program by asking the user if they would like to convert from customary
    to metric or vise versa, taking in their measurement, taking in their unit of that measurement,
    and then returning the measurement converted.
    """

    conversion_direction = get_conversion_direction()
    converting_length = get_converting_length()
    length_unit = get_length_unit(conversion_direction)

    if conversion_direction == "1":
        convert_customary_length_to_metric(length=converting_length, unit=length_unit)
    else:
        convert_metric_length_to_customary(length=converting_length, unit=length_unit)


if __name__ == "__main__":
    main()
