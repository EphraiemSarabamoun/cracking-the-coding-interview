def diving_board(shorter: int, longer: int, k: int) -> list[int]:
    if k == 0:
        return []
    if shorter == longer:
        return [k * shorter]
    lengths = set()
    for i in range(k + 1):
        lengths.add(i * shorter + (k - i) * longer)
    return sorted(lengths)