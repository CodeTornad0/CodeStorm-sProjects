"""Have symbols, text, or emojis race against each other in the terminal."""


import time
import random

TRACK_LENGTH = 10


class Racer:
    """
    A racer that checks if it can win the next round, increases its position,
    and return an image of it on the racing field.
    """

    def __init__(self, racer_id: int, racer_design: str) -> None:
        self.racer_id = racer_id
        self.racer_design = racer_design
        self.position = 0

    def is_close_enough_to_win(self) -> bool:
        """
        Checks if the racer can win the next move.

        Returns:
            bool: True if the racer can win the next move.
        """

        return self.position + 2 >= TRACK_LENGTH

    def increase_position(self) -> None:
        """Increase the racer position by 1 or 2."""

        self.position += random.randint(1, 2)

    def get_racer_image(self) -> str:
        """
        Return the racer number, where the racer is, and the racer

        Returns:
            str: A display of the racer number, where the racer is, and the racer
        """

        spaces_moved = " " * self.position
        spaces_left = " " * (TRACK_LENGTH - self.position)
        racer = self.racer_design
        if len(spaces_left) != 0:
            return f"Racer {self.racer_id}: {spaces_moved}{racer}{spaces_left}| End"
        return f"Racer {self.racer_id}: {spaces_moved} {racer} !"


def get_racer_design() -> str:
    """
    Ask the user for a design to give the racers.

    Returns:
        str: The design for the racers.
    """

    while True:
        racer_design = input("Enter a design that will represent the racers: ")
        if racer_design.strip() and len(racer_design.strip()) < 4:
            return racer_design
        print("The design has to less than four characters and cannot be empty")


def count_down_to_start() -> None:
    """Count down until the race starts."""

    for count_down_number in range(3, 0, -1):
        print(f"{count_down_number} {'.' * count_down_number}")
        time.sleep(1)
    print("Go!")
    time.sleep(0.5)
    clear_terminal()


def create_racers(racer_design: str) -> list[Racer]:
    """
    Create a list of five racers.

    Args:
        racer_design (str): The design of the racers.

    Returns:
        list[Racer]: 5 racers that will compete.
    """

    return [Racer(racer_id, racer_design) for racer_id in range(1, 6)]


def clear_terminal() -> None:
    """Clear the terminal of all text."""

    print("\033c", end="")


def display_racers(racers: list[Racer]) -> None:
    """
    Print out the racers on the track.

    Args:
        racers (list[Racer]): The racers to be printed.
    """

    for racer in racers:
        print(racer.get_racer_image())
    time.sleep(1)
    clear_terminal()


def advance_racers_position(racers: list[Racer]) -> None:
    """
    Increase 1-3 different racers positions by 1-2 steps.

    Args:
        racers (list[Racer]): The racers to be moved.
    """

    racers_to_advance: list[Racer] = []
    number_of_racers_advancing = random.randint(1, 3)
    potential_racers_advancing = racers.copy()

    for racer in potential_racers_advancing:
        if racer.is_close_enough_to_win():
            number_of_racers_advancing = 1

    for _ in range(number_of_racers_advancing):
        advancing_racer = random.choice(potential_racers_advancing)
        racers_to_advance.append(advancing_racer)
        potential_racers_advancing.remove(advancing_racer)

    for racer in racers_to_advance:
        racer.increase_position()


def check_win(racers: list[Racer]) -> list[Racer]:
    """
    Check if any of the racers have won.

    Args:
        racers (list[Racer]): Racers to be checked.

    Returns:
        list[Racer]: The list of racers that have won.
    """

    return [racer for racer in racers if racer.position >= TRACK_LENGTH]


def calculate_racers_finishing_position(racers: list[Racer]) -> None:
    """
    Print out the racers on the podium and how far they got.

    Args:
        racers (list[Racer]): The racers to be graded.
    """

    podium_positions = ["1st", "2nd", "3rd", "4th", "5th"]
    finishing_places = sorted(
        racers, key=lambda racer: racers[racers.index(racer)].position, reverse=True
    )
    for index in range(5):
        finishing_position = podium_positions[index]
        racer = finishing_places[index].racer_id
        racer_position = finishing_places[index].position
        print(f"{finishing_position}. Racer {racer} with position {racer_position}")


def main() -> None:
    """
    Run the program by getting the racer design, creating the racers, starting the race,
    going through the loop of displaying the racers, checking if any have won, and increasing their
    position and displaying the racers on the podium at the end.
    """

    racer_design = get_racer_design()
    racers: list[Racer] = create_racers(racer_design)

    input("Press enter to start the race")
    clear_terminal()
    count_down_to_start()

    while True:
        display_racers(racers)
        if check_win(racers):
            break
        advance_racers_position(racers)

    clear_terminal()
    calculate_racers_finishing_position(racers)


if __name__ == "__main__":
    main()
