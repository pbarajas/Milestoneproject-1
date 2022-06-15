import random
# STEP 1
# Write a function that can print out a board
def display_board(board):
    print('\n'*100)

    print(f"{board[1]}|{board[2]}|{board[3]}")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print(f"{board[7]}|{board[8]}|{board[9]}")


# TEST Step 1:
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
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
    
    random_player = random.randint(1,2)
    if random_player == 1:
        player1 = 'Player 1'
        return player1
    else:
        player2 = 'Player 2'
        return player2


print(choose_first())

def choose_first():
    players = ['player 1', 'player 2']
    players = random.choice(players)
    return players

print(choose_first())