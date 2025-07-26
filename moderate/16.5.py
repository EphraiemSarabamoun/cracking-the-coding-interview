def factorial_zeros(n: int) -> int:
    zeros = 0
    while n > 0:
        n //= 5
        zeros += n
    return zeros