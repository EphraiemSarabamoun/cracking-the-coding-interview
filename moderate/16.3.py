class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def orientation(p: Point, q: Point, r: Point) -> int:
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0: return 0  # Collinear
    return 1 if val > 0 else 2  # Clock/counter

def on_segment(p: Point, q: Point, r: Point) -> bool:
    return (min(p.x, r.x) <= q.x <= max(p.x, r.x) and min(p.y, r.y) <= q.y <= max(p.y, r.y))

def do_intersect(p1: Point, q1: Point, p2: Point, q2: Point) -> bool:
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True
    return False

def intersection_point(p1: Point, q1: Point, p2: Point, q2: Point) -> Point:
    # Line eq solve
    a1 = q1.y - p1.y
    b1 = p1.x - q1.x
    c1 = a1 * p1.x + b1 * p1.y
    a2 = q2.y - p2.y
    b2 = p2.x - q2.x
    c2 = a2 * p2.x + b2 * p2.y
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None  # Parallel
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    return Point(x, y) if do_intersect(p1, q1, p2, q2) else None