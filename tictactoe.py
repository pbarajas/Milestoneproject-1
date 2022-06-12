# STEP 1
# Write a function that can print out a board
def display_board(board):
    print('\n'*100)

    print(f"{board[1]}|{board[2]}|{board[3]}")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print(f"{board[7]}|{board[8]}|{board[9]}")


# TEST Step 1:
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)

# STEP 2
# Write a function that can take in a player input


def player_input():
    letter_X = 'X'
    letter_O = 'O'

    while True:
        choice = input("please pick a marker 'X or O' ")
        if choice in letter_O:
            return choice
        elif choice in letter_X:
            return choice
        else:
            if choice not in letter_O or choice not in letter_X:
                print("Sorry, I didn't understand. Please make sure to choose X or O ")


# TEST Step 2:
player_input()


# STEP 3
# Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.


def place_marker(board, marker, position):

    board[position] = marker

    return board


# TEST Step 3:
place_marker(test_board, '$', 8)
display_board(test_board)


# STEP 4
#  Write a function that takes in a board and a mark (X or O)
# and then checks to see if that mark has won.
def win_check(board, mark):

    pass


win_check(test_board, 'X')
