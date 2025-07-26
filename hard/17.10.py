def majority_element(arr: list[int]) -> int:
    if not arr:
        return None
    cand = count = 0
    for num in arr:
        if count == 0:
            cand = num
        count += 1 if num == cand else -1
    actual = sum(1 for num in arr if num == cand)
    return cand if actual > len(arr) // 2 else None