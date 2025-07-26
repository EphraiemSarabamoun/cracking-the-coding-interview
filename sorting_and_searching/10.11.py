def peaks_valleys(arr: list[int]) -> list[int]:
    arr.sort()
    for i in range(1, len(arr), 2):
        arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr