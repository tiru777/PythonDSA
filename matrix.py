def read_matrix(m):
    list_matrix = []
    for i in range(m):
        temp_l = [int(i) for i in input().split()]
        list_matrix.append(temp_l)
    return list_matrix


m_rows = int(input("Enter number of rows:"))
n_cols = int(input("Enter number of cols:"))
matrix = read_matrix(m_rows)  # [[1, 2, 3], [3, 4, 5]]
# print("matrix:", matrix)


def display_matrix_format(matrix, m, n):
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()


# display_matrix_format(matrix, m_rows, n_cols)


def sum_matrix(matrix, m, n):
    s = 0
    for i in range(m):
        s = s + sum(matrix[i])
    return s


# print(sum_matrix(matrix, m_rows, n_cols))

matrix2 = read_matrix(m_rows)


def sum_two_matrix(m, n, matrix, matrix2):
    matrix3 = [[0,0,0] for i in range(m)]
    for i in range(m):
        for j in range(n):
            matrix3[i][j] = matrix[i][j] + matrix2[i][j]
            # sum +, subtract -,multiplication *
    return matrix3


matrix3 = sum_two_matrix(m_rows, n_cols, matrix, matrix2)

display_matrix_format(matrix, m_rows, n_cols)
display_matrix_format(matrix2, m_rows, n_cols)
display_matrix_format(matrix3, m_rows, n_cols)
