import random
import time

print("\nWelcome to TicTacToe\n")


def valid_square(given_input):
    try:
        given_input = int(given_input)
        if 0 < given_input < 10:
            return True
        else:
            return False
    except ValueError:
        return False


def valid_choice(choice):
    return choice == 'X' or choice == 'O'


player = 'X'
while True:
    player = input("Do you want to be X or O ? ").strip().upper()
    if not valid_choice(player):
        print("Invalid choice.")
        time.sleep(1)
    else:
        break

print(f"You are {player}.")

nextPlayer = 'X'
while True:
    nextPlayer = input("Does X or O begin? ").strip().upper()
    if not valid_choice(nextPlayer):
        print("Invalid choice.")
        time.sleep(2)
    else:
        break

print(f"{nextPlayer} begins.")

cpu = None
if player.strip().upper() == 'X':
    cpu = 'O'
elif player.strip().upper() == 'O':
    cpu = 'X'

game = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]


def draw():
    print()
    print(f"----------------------------------------------------")
    print(f"   |               |               |               |")
    print(f"   |       {game[0]}       |       {game[1]}       |       {game[2]}       |")
    print(f"   |               |               |               |")
    print(f"----------------------------------------------------")
    print(f"   |               |               |               |")
    print(f"   |       {game[3]}       |       {game[4]}       |       {game[5]}       |")
    print(f"   |               |               |               |")
    print(f"----------------------------------------------------")
    print(f"   |               |               |               |")
    print(f"   |       {game[6]}       |       {game[7]}       |       {game[8]}       |")
    print(f"   |               |               |               |")
    print(f"----------------------------------------------------")
    print()


def next_player():
    global nextPlayer
    if nextPlayer.strip().upper() == 'X':
        nextPlayer = 'O'
    else:
        nextPlayer = 'X'


def cpu_play():
    free = []
    index = 0
    for i in game:
        if i == " ":
            free.append(index)
        index += 1
    to_place = random.choice(free)
    game[to_place] = cpu


winner = None


def handle_win():
    horizontals = [[game[0], game[1], game[2]], [game[3], game[4], game[5]], [game[6], game[7], game[8]]]
    verticals = [[game[0], game[3], game[6]], [game[1], game[4], game[7]], [game[2], game[5], game[8]]]
    diagonals = [[game[0], game[4], game[8]], [game[2], game[4], game[6]]]
    global winner
    for i in horizontals:
        if i.count(player) == 3:
            winner = player
            draw()
        elif i.count(cpu) == 3:
            winner = cpu
            draw()
    for i in verticals:
        if i.count(player) == 3:
            winner = player
            draw()
        elif i.count(cpu) == 3:
            winner = cpu
            draw()
    for i in diagonals:
        if i.count(player) == 3:
            winner = player
            draw()
        elif i.count(cpu) == 3:
            winner = cpu
            draw()


while winner is None:
    draw()
    time.sleep(2)
    if nextPlayer == player:
        place = input(f"Choose a square to place your {player}: ")
        while not valid_square(place):
            place = input("Invalid choice. Please try again with a number from 1 to 9: ")
        place = int(place)
        game[place - 1] = player
    else:
        cpu_play()

    handle_win()
    next_player()

print(f"{winner} is the winner!")
