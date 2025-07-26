def magic_index(arr: list[int]) -> int:
    def search(low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid
        if arr[mid] > mid:
            return search(low, mid - 1)
        return search(mid + 1, high)
    return search(0, len(arr) - 1)

def magic_index_dups(arr: list[int]) -> int:
    def search(low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid
        left_end = min(mid - 1, arr[mid])
        left = search(low, left_end)
        if left >= 0:
            return left
        right_start = max(mid + 1, arr[mid])
        return search(right_start, high)
    return search(0, len(arr) - 1)

if __name__ == "__main__":
    print(magic_index([1, 2, 3, 4, 5]))
    print(magic_index_dups([1, 2, 2, 3, 4, 5]))