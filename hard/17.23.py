def max_black_square(mat: list[list[int]]) -> int:
    if not mat or not mat[0]:
        return 0
    rows, cols = len(mat), len(mat[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side ** 2