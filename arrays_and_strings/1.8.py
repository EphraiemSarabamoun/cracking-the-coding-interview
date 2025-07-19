def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    i_set = set()
    j_set = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                i_set.add(i)
                j_set.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in i_set or j in j_set:
                matrix[i][j] = 0
    return matrix


if __name__ == "__main__":
    print(zero_matrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))
