# If an element in an MxN matrix is 0, its entire row and column are set to 0.


# Space O(n²) (all zeros). Time O(n²) (n³)
def zero_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zeros = []
    # find zero elements positions
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeros.append([i, j])

    # zero columns and rows
    for pos in zeros:
        x = pos[0]
        y = pos[1]
        for i in range(cols):
            matrix[x][i] = 0
        for i in range(rows):
            matrix[i][y] = 0

    return matrix


m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 0, 11, 12],
     [13, 14, 0, 16],
     [17, 18, 19, 20]]
print(zero_matrix(m))

