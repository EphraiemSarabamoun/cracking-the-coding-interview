def sum_swap(a: list[int], b: list[int]) -> tuple[int, int]:
    sum_a = sum(a)
    sum_b = sum(b)
    if (sum_a - sum_b) % 2 != 0:
        return None
    target = (sum_a - sum_b) // 2
    set_b = set(b)
    for val in a:
        if val - target in set_b:
            return (val, val - target)
    return None