class Square:
    def __init__(self, x: float, y: float, size: float):
        self.x = x  # Bottom left
        self.y = y
        self.size = size

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

def bisect_squares(s1: Square, s2: Square) -> Line:
    c1 = Point(s1.x + s1.size / 2, s1.y + s1.size / 2)
    c2 = Point(s2.x + s2.size / 2, s2.y + s2.size / 2)
    return Line(c1, c2)