"""
Generate a map using a start and end of x and y
and allow the user to plot locations on the map.
"""

MAX_ROW_COLUMN_WIDTH_HEIGHT = 35


def get_valid_int_input(prompt: str) -> int:
    """
    Summary:
        Handle input and return a int.

    Args:
        prompt (str): The prompt the user will be asked.

    Returns:
        int: The number the user entered.
    """

    while True:
        number = input(f"{prompt}: ")
        if not number.isdigit() or int(number) > MAX_ROW_COLUMN_WIDTH_HEIGHT:
            print(
                "Invalid input. Input must be an integer greater than or equal to zero and"
                f" less than {MAX_ROW_COLUMN_WIDTH_HEIGHT}"
            )
            continue
        return int(number)


def clear_terminal() -> None:
    """Clear the terminal of all text."""
    print("\033c", end="")


def print_columns(
    y_end: int,
    y_start: int,
    x_start: int,
    x_end: int,
    location_markers: dict[tuple[int, int], str],
) -> None:
    """
    Summary:
        Print the columns on the y axis.

    Args:
        y_end (int): The end of the y axis.
        y_start (int): The start of the y axis.
        x_start (int): The start of the x axis.
        x_end (int): The end of the x axis.
    """

    for y in range(y_end, y_start - 1, -1):
        print(f"{y:03}", end="|")
        for x in range(x_start, x_end + 1):
            marker = f" {location_markers.get((x, y), ' ')} "
            print(f"{marker}|", end="")
            if x == x_end:
                print()

        columns = (x_end - x_start) + 1
        dashes_per_column = 4
        dashes_at_end = 4
        number_of_dashes = columns * dashes_per_column + dashes_at_end
        print("-" * number_of_dashes)


def print_rows(x_start: int, x_end: int) -> None:
    """
    Summary:
        Print the rows on the x axis.

    Args:
        x_start (int): The start of the x axis.
        x_end (int): The end of the x axis.
    """

    for x in range(x_start, x_end + 1):
        print(f"{x:03}", end="|")


def print_y_axis() -> None:
    """Print the y axis by showing arrows in which direction y goes."""
    print("y ↕|", end="")


def print_x_axis() -> None:
    """Print the x axis by showing arrows in which direction x goes."""
    print()
    print("   ← x →")


def is_user_editing_location_markers() -> str:
    """
    Summary:
        Asks the user if they would like to add or edit markers on the map.

    Returns:
        str: Allows the program to know if it should prompt the user to add markers.
    """

    user_editing = input(
        "Do not enter anything if you would like to not add or edit any markers"
        " or pin points on the map. Otherwise, enter something"
    )
    return user_editing


def get_marker_design() -> str:
    """
    Summary:
        Get the marker design from the user.

    Returns:
        str: The design of the marker. Can be any character. Cannot be greater than one character.
    """

    while True:
        design = input(
            "Enter the design of the pin point. This can be any letter, number, or symbol."
            " It can only be one character: "
        )
        if len(design) < 2:
            if design.strip() == "":
                design = " "
            return design
        print("Invalid input. Input must be one character")


def get_marker_axis(prompt: str, axis: str, axis_start: int, axis_end: int) -> int:
    """
    Summary:
        Get the location of the marker.

    Args:
        prompt (str): The prompt the user is asked.
        axis (str): The axis being asked. Either the x or y.
        axis_start (int): The start location of the said axis.
        axis_end (int): The end location of the said axis.

    Returns:
        int: The marker location.
    """

    while True:
        marker_location = get_valid_int_input(prompt=prompt)
        if marker_location not in range(axis_start, axis_end + 1):
            print(f"Invalid input. Input must one of the locations on the {axis} axis")
            continue
        return marker_location


def edit_location_markers(
    x_start: int,
    x_end: int,
    y_start: int,
    y_end: int,
    location_markers: dict[tuple[int, int], str],
) -> dict[tuple[int, int], str]:
    """
    Summary:
        Allow the user to add or edit location_markers on the map.

    Returns:
        dict: The location_markers with the location as the key and the design as the value.
    """

    editing_location_markers = "true"
    print(
        "Keep in mind, once adding a marker, that marker can be removed by entering"
        " the marker's design as a space or edited by entering a new design on the same location"
    )
    while editing_location_markers:
        marker_x = get_marker_axis(
            prompt="Enter the x of the pin point",
            axis="x",
            axis_start=x_start,
            axis_end=x_end,
        )
        marker_y = get_marker_axis(
            prompt="Enter the y of the pin point",
            axis="y",
            axis_start=y_start,
            axis_end=y_end,
        )

        marker_design = get_marker_design()
        location_markers[(marker_x, marker_y)] = marker_design
        editing_location_markers = input(
            "Enter something if you would like to add more pin points. Otherwise, enter nothing"
        )
    return location_markers


def main() -> None:
    """
    Run the program by getting the start and end of the x and y, generating a map from that,
    and asking the user to plot locations on the map.
    """

    x_start = get_valid_int_input(prompt="Enter the start of x")
    x_end = get_valid_int_input(prompt="Enter the end of x")
    y_start = get_valid_int_input(prompt="Enter the start of y")
    y_end = get_valid_int_input(prompt="Enter the end of y")
    location_markers: dict[tuple[int, int], str] = {}

    while True:
        clear_terminal()

        print_columns(
            y_end=y_end,
            y_start=y_start,
            x_start=x_start,
            x_end=x_end,
            location_markers=location_markers,
        )

        print_y_axis()
        print_rows(x_start=x_start, x_end=x_end)
        print_x_axis()

        if is_user_editing_location_markers():
            edit_location_markers(
                x_start=x_start,
                x_end=x_end,
                y_start=y_start,
                y_end=y_end,
                location_markers=location_markers,
            )


if __name__ == "__main__":
    main()
