def smallest_diff(a: list[int], b: list[int]) -> int:
    a.sort()
    b.sort()
    i = j = 0
    min_diff = float('inf')
    while i < len(a) and j < len(b):
        min_diff = min(min_diff, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff