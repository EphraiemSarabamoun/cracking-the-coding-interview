def paint_fill(screen: list[list[int]], r: int, c: int, new_color: int) -> bool:
    if not screen or not screen[0]:
        return False
    rows, cols = len(screen), len(screen[0])
    old_color = screen[r][c]
    if old_color == new_color:
        return False
    def dfs(x: int, y: int):
        if x < 0 or x >= rows or y < 0 or y >= cols or screen[x][y] != old_color:
            return
        screen[x][y] = new_color
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
    dfs(r, c)
    return True

if __name__ == "__main__":
    screen = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(paint_fill(screen, 1, 1, 2))