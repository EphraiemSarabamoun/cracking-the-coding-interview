def random_set(arr: list[int], m: int) -> list[int]:
    if m > len(arr):
        raise ValueError
    shuffle_deck(arr)  # From 17.2
    return arr[:m]