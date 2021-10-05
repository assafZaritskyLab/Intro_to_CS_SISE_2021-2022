legal = [[0, 1, 0, 0],
         [0, 0, 0, 1],
         [1, 0, 0, 0],
         [0, 0, 1, 0]]
illegal = [[0, 1, 0, 0],
           [0, 0, 1, 0],
           [1, 0, 0, 0],
           [0, 0, 1, 0]]


def is_legal_board(board):
    """
       Summary or Description of the Function
       Parameters:
            board (list):list of lists. Number of rows equal to the number of columns. All cells contain zeroes except the cells with queens, they contain ones.
       Return:
            bool: True for legal queen assignment, False otherwise
   """
    max_col = len(board[0])
    max_row = len(board)
    cols = [[] for x in range(max_col)]
    rows = [[] for x in range(max_row)]
    fdiag = [[] for x in range(max_row + max_col - 1)]
    for col in range(max_col):
        for row in range(max_row):
            cols[col].append(board[row][col])
            rows[row].append(board[row][col])
            fdiag[col + row].append(board[row][col])
    for col in cols:
        if sum(col) >= 2:
            return False
    for row in rows:
        if sum(row) >= 2:
            return False
    for diag in fdiag:
        if sum(diag) >= 2:
            return False

    # board is legal
    return True

print(is_legal_board(illegal))
print(is_legal_board(legal))