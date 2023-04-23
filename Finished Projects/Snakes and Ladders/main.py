import random
import time


def main():
    while True:
        try:
            WAIT_TIME = float(
                input(
                    "Enter The Amount Of Wait Time Between Each Action [This Can Simulate The Board Game Feeling (One Is Recommended) ]: "
                )
            )
            while WAIT_TIME < 0:
                print("This Must Be A Number Greater Than Or Equal To Zero")
                WAIT_TIME = float(
                    input(
                        "Enter The Amount Of Wait Time Between Each Action [This Can Simulate The Board Game Feeling (One Is Recommended) ]: "
                    )
                )
            break
        except ValueError:
            print("Invalid Input")
    ladders = {4: 8, 6: 13, 11: 17, 15: 21, 18: 27, 22: 25, 26: 30}
    snakes = {3: 0, 10: 5, 19: 16, 23: 20, 24: 7, 31: 20, 32: 1}
    players_created = []
    wining_position = 35
    cur = 0
    instructions = f"""
    Instructions:  
        1. All Players Start At The Starting Position (0)
        2. Each Player Will Roll A Dice On Their Turn From The Numbers One To Six That Will Move Them Up Said Dice Roll
        3. All Players Will Get One Turn Before It Moves On To The Next Player
        4. If A Player Lands On A Ladder They Will Be Taken To The Top Of Said Ladder
        5. If A Player Lands On A Snake They Will Be Taken To The Bottom Of Said Snake
        6. The Position Of Ladders Are {list(ladders.keys())}. They Will Take You To {list(ladders.values())}
        7. The Position Of Snakes Are {list(snakes.keys())}. They Will Take You To {list(snakes.values())}
        8. The First Person To Get To The Winning Position Wins (Refer To Rule 9)
        9. The Winning Position Is {wining_position}
             """
    print(instructions)

    class Player:
        def __init__(self, name, position):
            self.name = name
            self.position = position

    while True:
        players = input("Enter The Amount Of People Playing: ")
        if players.isdigit() and int(players) > 1:
            players = int(players)
            break
        print("Invalid Input")
    for i in range(players):
        player_name = input(f"Enter Player {list(range(players))[i] + 1}'s Name: ")
        while player_name in players_created:
            print("This Name Already Exist")
            player_name = input(f"Enter Player {list(range(players))[i] + 1}'s Name: ")
        players_created.append(player_name)
        globals()[player_name] = Player(player_name, 0)
    print(f"This Game Will Be Played With: ")
    for i in players_created:
        print("    ", i)
    while True:
        cur_player = players_created[cur]
        if cur < players - 1:
            cur += 1
        else:
            cur = 0
        block = input(f"{cur_player}, Press Enter To Roll The Dice: ")
        del block
        print(f"{cur_player} Is Rolling The Dice...")
        time.sleep(WAIT_TIME)
        dice_role = random.randint(1, 6)
        print(f"{cur_player} Is Moving...")
        time.sleep(WAIT_TIME)
        globals()[cur_player].position += dice_role
        old_position = globals()[cur_player].position
        if globals()[cur_player].position in snakes:
            globals()[cur_player].position = snakes[globals()[cur_player].position]
            print(
                f"{cur_player} Has Landed On A Snake. They Moved {(globals()[cur_player].position - old_position) * -1} Space(s) Down ~~~~~~~~>"
            )
        elif globals()[cur_player].position in ladders:
            globals()[cur_player].position = ladders[globals()[cur_player].position]
            print(
                f"{cur_player} Has Landed On A Ladder. They Moved {globals()[cur_player].position - old_position} Space(s) Up ^^^^^^^^^"
            )
        if globals()[cur_player].position >= wining_position:
            print(f"{cur_player} Wins! They Rolled A {dice_role}")
            main()
        print(
            f"{cur_player} Is At Space {globals()[cur_player].position}. They Rolled A {dice_role}"
        )


main()
