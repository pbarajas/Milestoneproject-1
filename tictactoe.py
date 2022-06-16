import random
# STEP 1
# Write a function that can print out a board
def display_board(board):
    print('\n'*100)

    print(f"{board[1]}|{board[2]}|{board[3]}")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print(f"{board[7]}|{board[8]}|{board[9]}")


# TEST Step 1:
# test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# STEP 2
# Write a function that can take in a player input

# player_input() assigns a marker x or o
def player_input(): 
    letter_X = 'X'
    letter_O = 'O'

    while True:
        marker = input("please pick a marker 'X or O' ")
        if marker == letter_O:
            return marker
        elif marker == letter_X:
            return marker
        else:
            if marker not in letter_O or marker not in letter_X:
                print("Sorry, I didn't understand. Please make sure to choose X or O ")


# TEST Step 2:
# player_input()


# STEP 3
# Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.


def place_marker(board, marker, position):

    board[position] = marker

    return board


# TEST Step 3:
# place_marker(test_board, '$', 8)
# display_board(test_board)


# STEP 4
#  Write a function that takes in a board and a mark (X or O)
# and then checks to see if that mark has won.
def win_check(board, mark):
    if board[1] == mark and board[2] ==mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] ==  mark:
        return True 
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] ==  mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    else:
        return False



# print(win_check(test_board,'X'))

# STEP 5
# Write a function that uses the random module to randomly decide which player goes first. 


def choose_first():
    players = ['player 1', 'player 2']
    players = random.choice(players)
    return players

# print(choose_first())

# STEP 6
# Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    if board[position] == ' ':
        return True 
    else:
        return False


# Check Step
# print(space_check(test_board, 1))

# STEP 7 
#  Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    if ' ' in board:
        return False
    return True
# print(full_board_check(test_board))


# STEP 8
#  Write a function that asks for a player's next position (as a number 1-9)
# and then uses the function from step 6 to check if it's a free position. If it is, 
# then return the position for later use.

def player_choice(board):
    player_next_position = int(input('Choose next position (1-9): '))
    return space_check(board, player_next_position)
    


# print(player_choice(test_board))


# STEP 9
#  Write a function that asks the player if they want to play again
#  and returns a boolean True if they do want to play again.

def replay():
    play_again = input('Play again? (Yes/No): ').lower()
    if play_again == 'yes':
        return True


# STEP 10
#  Here comes the hard part! Use while loops and the functions you've made to run the game!

# print('Welcome to Tic Tac Toe!')
# test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# while True:
#     display_board(test_board)
#     pass

