import random

score = {"X": 0, "O": 0}


def main():
    values = [" " for value in range(9)]
    player_pos = {"X": [], "O": []}
    current_player = "X"

    def win(player_pos, current_player):
        possibilities = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]
        for x in possibilities:
            if all(y in player_pos[current_player] for y in x):
                return True
        return False

    def tie(player_pos):
        if len(player_pos["X"]) + len(player_pos["O"]) == 9:
            return True
        return False

    def draw_playing_field():
        cur = 0
        print("\n")
        for i in range(3):
            print("\t     |     |")
            print(f"\t  {values[cur]}  |  {values[cur+1]}  |  {values[cur+2]}")
            cur += 3
            if i == 2:
                print("\t     |     |")
            else:
                print("\t_____|_____|_____")
        print("\n")

    def draw_scoreboard(scoreboard):
        print("\t------------------------------")
        print("\t          SCOREBOARD          ")
        print("\t------------------------------")

        players = list(scoreboard.keys())
        print("\t   ", players[0], "\t    ", scoreboard[players[0]])
        print("\t   ", players[1], "\t    ", scoreboard[players[1]])

        print("\t------------------------------\n")

    def conditions():
        if win(player_pos, current_player):
            draw_playing_field()
            print(f"{current_player} Wins")
            score[current_player] += 1
            return True
        if tie(player_pos):
            draw_playing_field()
            print("Tie")
            return True
        return False

    while True:
        if game_option == "3":
            draw_scoreboard(score)
            break
        if game_option == "1" or current_player == "X":
            draw_playing_field()
        if game_option == "1":
            user_input = input(f"Player {current_player}, Enter Your Position: ")
        elif current_player == "X":
            user_input = input("Enter Your Position: ")
        if game_option == "1" or current_player == "X":
            if user_input not in str(list(range(1, 10))):
                print("Invalid Position")
            else:
                user_input = int(user_input)
                if values[user_input - 1] != " ":
                    print("This Move Has Already Been Made")
                else:
                    values[user_input - 1] = current_player
                    player_pos[current_player].append(user_input)
                    if conditions():
                        break
                    if current_player == "X":
                        current_player = "O"
                    else:
                        current_player = "X"
        else:
            bot_input = list(range(1, 10))[random.randint(0, 8)]
            while values[bot_input - 1] != " ":
                bot_input = list(range(1, 10))[random.randint(0, 8)]
            values[bot_input - 1] = current_player
            player_pos[current_player].append(bot_input)
            if conditions():
                break
            current_player = "X"


while True:
    game_option = input(
        "Action 1. Play Against Person Or 2. A Bot [Enter 3 For Scoreboard]: "
    )
    if game_option in ["1", "2", "3"]:
        main()
    else:
        print("Invalid Input")
