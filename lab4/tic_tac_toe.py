import math

board = [" "] * 9


def print_board():

    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner():

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(is_maximizing):

    result = check_winner()

    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "Draw":
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def best_move():

    best_score = -math.inf
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


print("TIC-TAC-TOE")
print("Positions are 0 to 8")

print_board()

while True:

    # Human move
    position = int(input("Enter your move (0-8): "))

    if board[position] != " ":
        print("Position already occupied!")
        continue

    board[position] = "X"

    print_board()

    result = check_winner()

    if result:
        print("Result:", result)
        break

    # Computer move
    computer_move = best_move()
    board[computer_move] = "O"

    print("Computer selected:", computer_move)

    print_board()

    result = check_winner()

    if result:
        print("Result:", result)
        break