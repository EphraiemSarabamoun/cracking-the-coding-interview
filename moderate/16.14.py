from collections import defaultdict
from math import gcd

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def best_line(points: list[Point]) -> tuple[Point, Point]:
    if len(points) < 2:
        return None
    max_count = 1
    best_p1 = best_p2 = None
    for i in range(len(points)):
        slopes = defaultdict(int)
        dup = 1
        for j in range(i + 1, len(points)):
            if points[i].x == points[j].x and points[i].y == points[j].y:
                dup += 1
                continue
            dx = points[j].x - points[i].x
            dy = points[j].y - points[i].y
            g = gcd(dx, dy)
            slope = (dy // g, dx // g) if dx >= 0 else (-dy // g, -dx // g)  # Normalize
            slopes[slope] += 1
        if slopes:
            max_slope = max(slopes, key=slopes.get)
            count = slopes[max_slope] + dup
            if count > max_count:
                max_count = count
                best_p1 = points[i]
                # Find p2 on that slope
                for j in range(i + 1, len(points)):
                    dx = points[j].x - points[i].x
                    dy = points[j].y - points[i].y
                    g = gcd(dx, dy)
                    s = (dy // g, dx // g) if dx >= 0 else (-dy // g, -dx // g)
                    if s == max_slope:
                        best_p2 = points[j]
                        break
    return (best_p1, best_p2) if best_p1 else None