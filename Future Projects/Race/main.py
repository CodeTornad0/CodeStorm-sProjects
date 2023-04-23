import time
import random


class Racer:
    def __init__(self, racer_id: int, racer_design: str) -> None:
        self.racer_id = racer_id
        self.racer_design = racer_design
        self.position = 0

    def is_close_enough_to_win(self) -> bool:
        return self.position + 2 >= 10

    def increase_position(self) -> None:
        self.position += random.randint(1, 2)

    def get_racer_image(self) -> None:
        return f"{' ' * self.position}{self.racer_design}"


def get_racer_design() -> str:
    while True:
        racer_design = input("Enter a design that will represent the racers: ")
        if racer_design.strip() and len(racer_design.strip()) < 4:
            return racer_design
        print("The design has to less than four characters and cannot be empty")


def count_down_to_start() -> None:
    for count_down_number in range(3, 0, -1):
        print(f"{count_down_number} {'.' * count_down_number}")
        time.sleep(1)
    print("Go!")
    for _ in range(4):
        print()


def create_racers(racer_design: str) -> list:
    return [Racer(racer_id, racer_design) for racer_id in range(1, 6)]


def clear_terminal() -> None:
    """Clear the terminal of all text."""
    print("\033c", end="")


def display_racers(racers: list) -> None:
    for racer in racers:
        print(racer.get_racer_image())
    time.sleep(1)
    clear_terminal()


def advance_racers_position(racers: list) -> None:
    racers_to_advance = []
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


def check_win(racers: list) -> None:
    return [racer for racer in racers if racer.position >= 10]


def calculate_racers_finishing_position(racers: list) -> None:
    first_place = check_win(racers)[0].racer_id
    


def main() -> None:
    racer_design = get_racer_design()
    racers = create_racers(racer_design)

    input("Press enter to start the race")
    count_down_to_start()

    while True:
        display_racers(racers)
        advance_racers_position(racers)
        if check_win(racers):
            break

    clear_terminal()
    calculate_racers_finishing_position(racers)


if __name__ == "__main__":
    main()
