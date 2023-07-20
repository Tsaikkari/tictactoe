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

    # check if line is the winning line
    for i in range(len(lines)):
        [a, b, c] = lines[i]

        if board_list[a] != '_' and board_list[a] == board_list[b] and board_list[a] == board_list[c]:
            return True
        i += 1

    if board_list.index('_') == -1:
        print("It's a draw")
    else: 
        if char == 'X':
            char = 'O'
            next(board_list, char)
        else:
            # switch player
            char = 'X' 
            next(board_list, char)

def add_char(board, board_list_copy, char):
    modified_list = []
    for item in board_list_copy:
        if len(item) > 1:
            row_no = int(item[0])
            column_no = int(item[2])

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if i == row_no and j == column_no:
                        board[i][j] = char
                    modified_list.append(board[i][j])
                    j += 1
                i += 1

    if win(modified_list, char):
        print(f"The winner is: {char}")
        return 

def print_board(board):
    result = ""
    for i in range(len(board)):
        if i % 3 == 0:
            result += "\n"
        for j in range(len(board[i])):
            if type(board[i][j]) == str:
                if j % 3 == 0 and j != "_":
                    result += f" {str(board[i][j])} "
                else:
                    result += f"{str(board[i][j])} "
            else: 
                if j % 3 == 0:
                    result += " "
                result += "_ "
            j += 1
        result += "\n"
        i += 1
    print(result)
     
def get_char():
    pos = input("Enter the square position, for example 1.1 :")
    return pos

def insert_input(pos, board):
    board_list_copy = copy.deepcopy(board)
    for i in range(len(board_list_copy)):
        if i == 0 and pos == '0.0':
            board_list_copy[i] = '0.0'
        elif i == 1 and pos == '0.1':
            board_list_copy[i] = '0.1'
        elif i == 2 and pos == '0.2':
            board_list_copy[i] = '0.2'
        elif i == 3 and pos == '1.1':
            board_list_copy[i] = '1.1'
        elif i == 4 and pos == '1.2':
            board_list_copy[i] = '1.2'
        elif i == 5 and pos == '1.3':
            board_list_copy[i] = '1.3'
        elif i == 6 and pos == '2.1':
            board_list_copy[i] = '2.1'
        elif i == 7 and pos == '2.2':
            board_list_copy[i] = '2.2'
        elif i == 8 and pos == '2.3':
            board_list_copy[i] = '2.3'
    return board_list_copy

def next(board_list, char):
    print_board(board)
    pos = get_char()
    board_list_copy = insert_input(pos, board_list)
    if board_list_copy != []:
        add_char(board, board_list_copy, char)

next(board_list, 'X')



     





