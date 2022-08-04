import random

# The board that will be used to insert the "X" and "O"


def board(rows):
    print(f'''
       |   |
     {rows[0][0]} | {rows[0][1]} | {rows[0][2]}
       |   |
    -----------
       |   |
     {rows[1][0]} | {rows[1][1]} | {rows[1][2]}
       |   |
    -----------
       |   |
     {rows[2][0]} | {rows[2][1]} | {rows[2][2]}
       |   |      ''')

# selects in which row the users "X" or the computers "O" should be placed according to the position number chosen.


def rowSelector(choice):
    row = 0
    if 0 < choice <= 3:
        row = 0
    elif 3 < choice <= 6:
        row = 1
    elif 6 < choice <= 9:
        row = 2

    return row

# Selects in which column the users "X" or computers "O" should be placed according to the position number chosen


def columnSelector(choice):
    column = 0
    if choice == 2 or choice == 5 or choice == 8:
        column = 1

    elif choice == 3 or choice == 6 or choice == 9:
        column = 2

    return column

# A function created to check if the user has won or lost according to the rows multi-dimensional array


def winCheck(rows):
    global repeat
    start = 0
    for i in range(3):
        if rows[start][0] == "X" and rows[start][1] == "X" and rows[start][2] == "X":
            print("You Win!")
            repeat = False
            return repeat

        elif rows[0][start] == "X" and rows[1][start] == "X" and rows[2][start] == "X":
            print("You Win!")
            repeat = False
            return repeat

        elif rows[start][0] == "O" and rows[start][1] == "O" and rows[start][2] == "O":
            print("You Lose!")
            repeat = False
            return repeat

        elif rows[0][start] == "O" and rows[1][start] == "O" and rows[2][start] == "O":
            print("You Lose!")
            repeat = False
            return repeat

        elif rows[0][0] == "X" and rows[1][1] == "X" and rows[2][2] == "X":
            print("You Win!")
            repeat = False
            return repeat

        elif rows[0][0] == "O" and rows[1][1] == "O" and rows[2][2] == "O":
            print("You Lose!")
            repeat = False
            return repeat

        elif rows[2][0] == "X" and rows[1][1] == "X" and rows[0][2] == "X":
            print("You Win!")
            repeat = False
            return repeat

        elif rows[2][0] == "O" and rows[1][1] == "O" and rows[0][2] == "O":
            print("You Lose!")
            repeat = False
            return repeat

        start += 1


# main Game loop
playGame = True
while playGame:
    availableOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    rows = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Loop that is used to play the game and stops when there is a tie, win or lose scenario.
    while len(availableOptions) > 0:
        repeat = True

        # makes sure the users enter a number or a valid postion according to the available list.
        while True:
            try:
                userChoice = int(input(
                    "Please choose a number between the numbers of 1 to 9: "))

                if userChoice in availableOptions:
                    rows[rowSelector(userChoice)][columnSelector(
                        userChoice)] = "X"
                    availableOptions.remove(userChoice)
                    break

                else:
                    print("Please choose a valid position!")

            except ValueError:
                print("Please make sure you enter a NUMBER!")

        board(rows)
        winCheck(rows)
        if not repeat:
            break

        if len(availableOptions) > 0:
            computerChoice = random.choice(availableOptions)
            if computerChoice in availableOptions:
                rows[rowSelector(computerChoice)][columnSelector(
                    computerChoice)] = "O"
                availableOptions.remove(computerChoice)

            print(f"The computer placed an 'O' at position {computerChoice}")

            board(rows)
            winCheck(rows)
            if not repeat:
                break

        if len(availableOptions) == 0:
            print("Tie!")
            break

    replay = input("Do you want to play again? Y/n ").lower()
    if replay == "n":
        playGame = False
