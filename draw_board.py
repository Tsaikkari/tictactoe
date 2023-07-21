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