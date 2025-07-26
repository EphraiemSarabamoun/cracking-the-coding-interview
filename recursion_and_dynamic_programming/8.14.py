def bool_eval(expr: str, target: bool) -> int:
    if not expr:
        return 0
    n = len(expr)
    dp_true = [[0] * n for _ in range(n)]
    dp_false = [[0] * n for _ in range(n)]
    for i in range(0, n, 2):  # Digits
        dp_true[i][i] = 1 if expr[i] == '1' else 0
        dp_false[i][i] = 1 - dp_true[i][i]
    for length in range(3, n + 1, 2):
        for i in range(0, n - length + 1, 2):
            j = i + length - 1
            for k in range(i + 1, j, 2):  # Op at k
                op = expr[k]
                left_t, left_f = dp_true[i][k-1], dp_false[i][k-1]
                right_t, right_f = dp_true[k+1][j], dp_false[k+1][j]
                if op == '&':
                    dp_true[i][j] += left_t * right_t
                    dp_false[i][j] += left_t * right_f + left_f * right_t + left_f * right_f
                elif op == '|':
                    dp_true[i][j] += left_t * right_t + left_t * right_f + left_f * right_t
                    dp_false[i][j] += left_f * right_f
                elif op == '^':
                    dp_true[i][j] += left_t * right_f + left_f * right_t
                    dp_false[i][j] += left_t * right_t + left_f * right_f
    return dp_true[0][n-1] if target else dp_false[0][n-1]

if __name__ == "__main__":
    print(bool_eval("1^0|0|1", True))