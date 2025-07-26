def pairs_with_sum(arr: list[int], target: int) -> list[tuple[int, int]]:
    arr.sort()
    result = []
    left = 0
    right = len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            result.append((arr[left], arr[right]))
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current < target:
            left += 1
        else:
            right -= 1
    return result