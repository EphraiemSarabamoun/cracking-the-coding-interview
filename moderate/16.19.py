def pond_sizes(land: list[list[int]]) -> list[int]:
    if not land or not land[0]:
        return []
    rows, cols = len(land), len(land[0])
    visited = [[False] * cols for _ in range(rows)]
    sizes = []
    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or land[r][c] != 0:
            return 0
        visited[r][c] = True
        size = 1
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dr, dc in directions:
            size += dfs(r + dr, c + dc)
        return size
    for r in range(rows):
        for c in range(cols):
            if land[r][c] == 0 and not visited[r][c]:
                sizes.append(dfs(r, c))
    return sorted(sizes)