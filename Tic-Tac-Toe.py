import random

player = ""
com = ""
current_player = ""
board = ["" for _ in range(9)]


def init_game():
    print("TIC-TAC-TOE")
    print("The board is numbered:")
    print("1-2-3\n4-5-6\n7-8-9\n")

    global player, com
    while True:
        player = input("Do you want to play X or O?: ").upper()
        if player == "X":
            com = "O"
            print("Player is X, computer is O.")
            break
        elif player == "O":
            com = "X"
            print("Player is O, computer is X.")
            break
        else:
            print("Invalid input. Please enter X or O.")

    choose_player()


def choose_player():
    global current_player
    if random.randint(0, 1) == 0:
        current_player = "X"
        print("It's Player X's turn.\n")
    else:
        current_player = "O"
        print("It's Player O's turn.\n")


def player_move(board):
    while True:
        try:
            field = int(input("Choose a field of the board (1-9): "))
            if field < 1 or field > 9:
                print("Choose a number between 1-9.")
                print("The board is numbered:")
                print("1-2-3\n4-5-6\n7-8-9\n")
            else:
                if is_legal(board, field):
                    break
        except ValueError:
            print("Please enter a valid integer.\n")

    global player
    board[field-1] = player

    print_board(board)
    switch_current()


def com_move(board):
    empty_indexes = []
    for i in range(len(board)):
        if board[i] == "":
            empty_indexes.append(i)
    field = random.choice(empty_indexes)

    print(f"Computer has chosen {field+1}.")
    global com
    board[field] = com

    print_board(board)
    switch_current()


def print_board(board):
    print("-------------------")
    for i in range(0, 9, 3):
        row = "|"
        for j in range(3):
            row += " {:^3s} |".format(board[i+j])
        print(row)
        print("-------------------")
    print("")


def is_legal(board, field):
    if board[field-1] in {"X", "O"}:
        print(f"The field at index {field} is already taken.\n")
        return False
    else:
        return True


def check_state(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]  # diagonal
    ]

    for combo in winning_combinations:
        if all(board[i] == "X" for i in combo):
            print("X is the winner!")
            return True
        elif all(board[i] == "O" for i in combo):
            print("O is the winner!")
            return True
   
    if "" not in board:
        print("Draw, there's no winner.")
        return True
        
    return False


def switch_current():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def game():
    init_game()
    while not check_state(board):
        if current_player == player:
            player_move(board)
        else:
            com_move(board)
    input()

if __name__ == "__main__":
    game()
