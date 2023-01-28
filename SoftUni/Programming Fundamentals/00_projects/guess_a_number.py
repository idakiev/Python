import random

computer_number = random.randint(1, 100)

player_move = input(f"Guess the number between 1 and 100. \n Please type a number:")

is_player_win = False


while not is_player_win:
    if not player_move.isdigit():
        print("Invalid input! Try again...")
        player_move = input(f"Please type a number:")
        continue

    if int(player_move) == computer_number:
        print("You guess it!")
        is_player_win = True
    elif int(player_move) > computer_number:
        print("Too high!")
        player_move = input("Try again... \n Please type a number:")
    else:
        print("Too low!")
        player_move = input("Try again... \n Please type a number:")
