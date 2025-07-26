def eight_queens() -> list[list[int]]:
    result = []
    queens = [-1] * 8 
    def is_valid(row: int) -> bool:
        for i in range(row):
            if queens[i] == queens[row] or abs(queens[row] - queens[i]) == row - i:
                return False
        return True

    def backtrack(row: int):
        if row == 8:
            result.append(queens[:])
            return
        for col in range(8):
            queens[row] = col
            if is_valid(row):
                backtrack(row + 1)

    backtrack(0)
    return result

if __name__ == "__main__":
    print(eight_queens())
