import random

array = ["1", "2", "3"]
while True:
    user_input = input("Action 1. Rock 2. Paper 3. Scissors: ")
    while user_input not in array:
        print("Invalid Input")
        user_input = input("Action 1. Rock 2. Paper 3. Scissors: ")
    bot_input = random.choice(array)
    bot_action = ["Rock", "Paper", "Scissors"][int(bot_input) - 1]
    if user_input == bot_input:
        print("Tie")
    elif (
        user_input == "1"
        and bot_input == "2"
        or user_input == "2"
        and bot_input == "3"
        or user_input == "3"
        and bot_input == "1"
    ):
        print(f"You Lose. The Bot Chose {bot_input} ({bot_action})")
    else:
        print(f"You Win. The Bot Chose {bot_input} ({bot_action})")


# this code is used to run out automatic games
# the wins, ties, and losses are according to the first user


# import random

# ties, losses, wins = 0, 0, 0
# for i in range(10000):
#     user1_input = [1, 2, 3][random.randint(0, 2)]
#     user2_input = [1, 2, 3][random.randint(0, 2)]
#     if user1_input == user2_input:
#         ties += 1
#     elif (
#         user1_input == 1
#         and user2_input == 2
#         or user1_input == 2
#         and user2_input == 3
#         or user1_input == 3
#         and user2_input == 1
#     ):
#         losses += 1
#     else:
#         wins += 1
# print("ties", ties, "wins", wins, "losses", losses)
