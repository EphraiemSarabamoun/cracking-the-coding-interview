def max_submatrix(mat: list[list[int]]) -> int:
    if not mat or not mat[0]:
        return 0
    rows, cols = len(mat), len(mat[0])
    max_sum = float('-inf')
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += mat[i][right]
            # Kadane on temp
            current = max_current = temp[0]
            for num in temp[1:]:
                current = max(num, current + num)
                max_current = max(max_current, current)
            max_sum = max(max_sum, max_current)
    return max_sum