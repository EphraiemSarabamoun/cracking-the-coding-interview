def parens(n: int) -> list[str]:
    result = []
    def backtrack(s: str, open_c: int, close_c: int):
        if len(s) == 2 * n:
            result.append(s)
            return
        if open_c < n:
            backtrack(s + '(', open_c + 1, close_c)
        if close_c < open_c:
            backtrack(s + ')', open_c, close_c + 1)
    backtrack('', 0, 0)
    return result

if __name__ == "__main__":
    print(parens(3))