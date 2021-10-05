
#### Question 2 - Sparse matrix

def get_sparse_matrix(matrix):
    """
    :matrix: An NxN matrix implemented using list of lists.
    :return: A dictionary with tuples as keys for the non-zero entrences in the matrix, and the value is the non-zero value

    """
    ans = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                ans[(i, j)] = matrix[i][j]
    return ans


li = [[0, 0, 3], [4, 0, 0], [0, 6, 0]]
get_sparse_matrix(li)

