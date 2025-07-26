def missing_number(arr: list[int]) -> int:
    n = len(arr) + 1  # Since one missing
    missing = 0
    for i in range(n):
        missing ^= i
        if i < len(arr):
            missing ^= arr[i]
    return missing