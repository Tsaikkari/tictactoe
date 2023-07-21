import copy

board_list = ['', '', '', '', '', '', '', '', '']
board  = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

####### TIC TAC TOE #######
###########################
#        0    1    2      #
#      ---------------    #
#   0  | X    O    X |    #
#   1  | O    X    X |    #
#   2  | X    O    O |    #
#      ---------------    #
###########################
###########################

char = ''

# winning lines
def win(board_list, char):
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

    # check if there is a winning line
    for i in range(len(lines)):
        [a, b, c] = lines[i]

        if board_list[a] != '_' and board_list[a] == board_list[b] and board_list[a] == board_list[c]:
            # print out the final board and end game
            print_board(board)
            print(f"The winner is: {char}")
            return
        i += 1
    # if it's not a win it might be a draw
    if board_list.count('_') == 0:
        # print out the final board and end game
        print_board(board)
        print("It's a draw")
        return
    else: 
        # or switch turns and continue
        switch_turn(board, board_list, char)

# modify the board list to include 'X' or 'O' on the user defined position on the board
def modify_list(board, board_list, board_list_copy, char):
    modified_list = []
    for item in board_list_copy:
        if len(item) > 1:
            add_char(item, board, board_list, char, modified_list)
            win(modified_list, char)
            
def add_char(item, board, board_list, char, modified_list):
    row_no = int(item[0])
    column_no = int(item[2])
    # loop over the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == row_no and j == column_no:
                if board[i][j] != '_':
                    print('A char already exists on that position')
                    if char == board[i][j]:
                        next(board, board_list, char)
                    else:
                        switch_turn(board, board_list, char=board[i][j])
                else:
                    # add char to the board 
                    board[i][j] = char
            # add every item to the list including the underscores
            modified_list.append(board[i][j])
            j += 1
        i += 1

def print_board(board):
    result = ""
    for i in range(len(board)):
        if i % 3 == 0:
            result += "\n"
        for j in range(len(board[i])):
            result += f" {(board[i][j])} "
            j += 1
        result += "\n"
        i += 1
    print(result)
     
def get_char():
    coord = input("Enter the coordinate, for example 1.1 :")
    return coord

# insert user input (position of the character) to a copy of the board_list
def insert_input(pos, board_list):
    board_list_copy = copy.deepcopy(board_list)
    for i in range(len(board_list_copy)):
        if i == 0 and pos == '0.0':
            board_list_copy[i] = '0.0'
        elif i == 1 and pos == '0.1':
            board_list_copy[i] = '0.1'
        elif i == 2 and pos == '0.2':
            board_list_copy[i] = '0.2'
        elif i == 3 and pos == '1.0':
            board_list_copy[i] = '1.0'
        elif i == 4 and pos == '1.1':
            board_list_copy[i] = '1.1'
        elif i == 5 and pos == '1.2':
            board_list_copy[i] = '1.2'
        elif i == 6 and pos == '2.0':
            board_list_copy[i] = '2.0'
        elif i == 7 and pos == '2.1':
            board_list_copy[i] = '2.1'
        elif i == 8 and pos == '2.2':
            board_list_copy[i] = '2.2'
    return board_list_copy

def switch_turn(board, board_list, char):
    if char == 'X':
        char = 'O'
    else:
        char = 'X' 
    next(board, board_list, char)


# main function
def next(board, board_list, char):
    print_board(board)
    position = get_char()
    b_list = insert_input(position, board_list)
    modify_list(board, board_list, b_list, char)

# start the game
next(board, board_list, 'X')



     





