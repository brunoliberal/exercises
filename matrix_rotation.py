# Rotate a matrix [][] 90 degrees. Each pixel represents 4 bytes.


# Space O(n²). Time O(n²)
def rotate_matrix(matrix):
    m_len = len(matrix)
    m = [[0 for x in range(m_len)] for y in range(m_len)]

    for i in range(m_len):
        for j in range(m_len):
            m[j][m_len - 1 - i] = matrix[i][j]
    return m


m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
print(rotate_matrix(m))

