import copy

matrix = []
board = ['', '', '', '', '', '', '', '', '']
char = ''

def win(board, char):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [2, 4, 6],
        [0, 4, 8],
    ]

    # check if line is the winning line
    for i in range(len(lines)):
        [a, b, c] = lines[i]

        if board[a] != '' and board[a] == board[b] and board[a] == board[c]:
            return True
        i += 1

    if board.index('') == -1:
        print("It's a draw")
    else: 
        if char == 'X':
            char = 'O'
            next(board, char)
        else:
            # update player
            char = 'X' 
            next(board, char)

def turn(matrix, board_copy, char):
    for i in range(3):
        for j in range(len(board_copy)):
            if len(board_copy[j]) == 3:
                # put char to the board
                board_copy[j] = char
            j += 3
        i += 1

    matrix = create_board(board_copy, 3)
    print(matrix)

    # announce the winner and end game
    if win(board_copy, char):
        print(f"The winner is: {char}")
        return 

def create_board(arr, length):
    game_board = []
    index = 0
    while index < len(arr):
        game_board.append(arr[index:index+3])
        index += length
    return game_board

def get_char():
    pos = input("Enter the square position, for example 1.1 :")
    return pos

def insert_input(pos, board):
    board_copy = copy.deepcopy(board)
    for i in range(len(board_copy)):
        if i == 0 and pos == '1.1':
            board_copy[i] = '1.1'
        elif i == 1 and pos == '1.2':
            board_copy[i] = '1.2'
        elif i == 2 and pos == '1.3':
            board_copy[i] = '1.3'
        elif i == 3 and pos == '2.1':
            board_copy[i] = '2.1'
        elif i == 4 and pos == '2.2':
            board_copy[i] = '2.2'
        elif i == 5 and pos == '2.3':
            board_copy[i] = '2.3'
        elif i == 6 and pos == '3.1':
            board_copy[i] = '3.1'
        elif i == 7 and pos == '3.2':
            board_copy[i] = '3.2'
        elif i == 8 and pos == '3.3':
            board_copy[i] = '3.3'
    return board_copy

def next(board, char):
    pos = get_char()
    board_copy = insert_input(pos, board)
    if board_copy != []:
        turn(matrix, board_copy, char)

next(board, 'X')

####### TIC TAC TOE #######
###########################
##  [                    ##
##    ['X', 'O', 'X'],   ##
##    ['O', 'X', 'X'],   ##
##    ['X', 'O', 'O']    ##
##  ]                    ##
###########################
###########################
     





