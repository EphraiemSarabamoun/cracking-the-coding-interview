def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix


if __name__ == "__main__":
    print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
