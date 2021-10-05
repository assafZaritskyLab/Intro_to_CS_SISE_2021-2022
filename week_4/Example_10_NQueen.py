legal = [[0, 1, 0, 0],
         [0, 0, 0, 1],
         [1, 0, 0, 0],
         [0, 0, 1, 0]]
illegal = [[0, 1, 0, 0],
           [0, 0, 1, 0],
           [1, 0, 0, 0],
           [0, 0, 1, 0]]


def is_legal_board(board):
    max_col = len(board[0])
    max_row = len(board)
    cols = []
    for x in range(max_col):
        cols.append([])
    rows = [[] for x in range(max_row)]

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(board[y][x])
            print(board[y][x])



    return True



print(is_legal_board(illegal))
print(is_legal_board(legal))
