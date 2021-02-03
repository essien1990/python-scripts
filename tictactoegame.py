# Need a board
# display board
# play game
# handle turn(inputs)
# check win -># check rows, # check columns, # check diagonals
# check tie
# flip player

# ------------------------Global variables-----------------------

# Need a game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game is still going
game_still_going = True

# Who won? or tie?
winner = None

# whose turn is it?
current_player = 'X'


# Display board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# play a game of Tic tac toe
def play_game():

    # display initial board
    display_board()

    # while the game is still going
    while game_still_going:

        # handle a single turn of an arbituary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to other play
        flip_player()

    # The game is ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won....!')
    elif winner == None:
        print("Is a tie...!")


# Handle a single turn
def handle_turn(player):
    print(player + '\'s turn.')

    position = input('Choose a position from 1 - 9: ')

    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            positon = input('Choose a position from 1 - 9: ')

        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print('You cannot go there. Go again!')

    board[position] = player

    display_board()


# Check if game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Check if there is a win
def check_for_winner():

    # global variable
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


# check rows
def check_rows():
    # Set up global variables
    global game_still_going
    # check if any of the rows are all the same  value (and is not  empty)
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    # if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
        # return the winner(X or O)
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        return


# check columns
def check_columns():
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    # if any columns does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner(X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


# check diagonals
def check_diagonals():
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'
    # if any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
        # return the winner(X or O)
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[6]
        return


# check if is a tie
def check_if_tie():
    # global variables
    global game_still_going
    # if dash(-) is not in board, stop game
    if '-' not in board:
        game_still_going = False
    return


# flip player from x - o
def flip_player():
    # global variables
    global current_player

    # if current player was x, then change to o
    if current_player == "X":
        current_player = "O"
    # if current player was o, then change to x
    elif current_player == "O":
        current_player = "X"
    return


play_game()
