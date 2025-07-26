from collections import Counter

def shortest_supersequence(big: list[int], small: list[int]) -> tuple[int, int]:
    if not small:
        return (0, -1)
    need = Counter(small)
    missing = len(small)
    left = i = j = 0
    min_len = float('inf')
    start = end = -1
    for right in range(len(big)):
        if big[right] in need:
            need[big[right]] -= 1
            if need[big[right]] >= 0:
                missing -= 1
        while missing == 0 and left <= right:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start, end = left, right
            if big[left] in need:
                need[big[left]] += 1
                if need[big[left]] > 0:
                    missing += 1
            left += 1
    return (start, end) if start != -1 else (-1, -1)