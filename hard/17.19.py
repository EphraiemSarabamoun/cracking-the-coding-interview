def missing_two(arr: list[int]) -> list[int]:
    n = len(arr) + 2
    miss_xor = 0
    for i in range(1, n + 1):
        miss_xor ^= i
    for num in arr:
        miss_xor ^= num
    least_bit = miss_xor & -miss_xor
    x = y = 0
    for i in range(1, n + 1):
        if i & least_bit:
            x ^= i
        else:
            y ^= i
    for num in arr:
        if num & least_bit:
            x ^= num
        else:
            y ^= num
    return [x, y]