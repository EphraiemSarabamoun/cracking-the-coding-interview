def add_without_plus(a: int, b: int) -> int:
    while b != 0:
        sum_no_carry = a ^ b
        carry = (a & b) << 1
        a = sum_no_carry
        b = carry
    return a