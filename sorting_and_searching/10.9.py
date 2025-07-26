def matrix_search(matrix: list[list[int]], target: int) -> tuple[int, int]:
    if not matrix or not matrix[0]:
        return (-1, -1)
    rows, cols = len(matrix), len(matrix[0])
    r, c = rows - 1, 0
    while r >= 0 and c < cols:
        if matrix[r][c] == target:
            return (r, c)
        elif matrix[r][c] > target:
            r -= 1
        else:
            c += 1
    return (-1, -1)