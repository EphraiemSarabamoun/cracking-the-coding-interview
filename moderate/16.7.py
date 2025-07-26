def number_max(a: int, b: int) -> int:
    return (a + b + abs(a - b)) // 2


def number_max_bit(a: int, b: int) -> int:
    diff = a - b
    k = (diff >> 31) & 1 
    return a - k * diff