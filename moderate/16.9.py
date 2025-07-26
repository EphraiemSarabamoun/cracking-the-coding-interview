def negate(n: int) -> int:
    return ~n + 1

def subtract(a: int, b: int) -> int:
    return a + negate(b)

def multiply(a: int, b: int) -> int:
    if b < 0:
        a, b = negate(a), negate(b)
    result = 0
    for _ in range(b):
        result += a
    return result

def divide(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Division by zero")
    if b < 0:
        a, b = negate(a), negate(b)
    count = 0
    while a >= b:
        a = subtract(a, b)
        count += 1
    return count