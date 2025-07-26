def robot_path(grid: list[list[bool]]) -> list[tuple[int, int]]:  # True=off-limits
    if not grid or not grid[0]:
        return []
    path = []
    failed = set()
    def dfs(r: int, c: int) -> bool:
        if r < 0 or c < 0 or grid[r][c] or (r, c) in failed:
            return False
        if r == 0 and c == 0 or dfs(r-1, c) or dfs(r, c-1):
            path.append((r, c))
            return True
        failed.add((r, c))
        return False
    if dfs(len(grid)-1, len(grid[0])-1):
        return path[::-1]  # Reverse to start->end
    return None

if __name__ == "__main__":
    grid = [[False, False, False], [True, True, False], [False, False, False]]
    print(robot_path(grid))
    