class Ant:
    def __init__(self):
        self.x = self.y = 0
        self.dir = 0  # 0 up, 1 right, 2 down, 3 left

def langton_ant(k: int) -> list[tuple[int, int]]:
    black = set()
    ant = Ant()
    moves = [(0,1), (1,0), (0,-1), (-1,0)]  # up right down left
    for _ in range(k):
        pos = (ant.x, ant.y)
        if pos in black:
            black.remove(pos)
            ant.dir = (ant.dir - 1) % 4
        else:
            black.add(pos)
            ant.dir = (ant.dir + 1) % 4
        dx, dy = moves[ant.dir]
        ant.x += dx
        ant.y += dy
    return sorted(list(black))