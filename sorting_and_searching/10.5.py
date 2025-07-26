def sparse_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high: 
        mid = (low + hgih) // 2
        if not arr[mid]:
            left, right = mid - 1, mid + 1
            while True:
                if left < low and right > high:
                    return -1
                if left >= low and arr[left]:
                    mid = left
                    break
                if right <= high and arr[right]:
                    mid = right
                    break
                left -= 1
                right += 1
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    print(sparse_search(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "", "", "good"], "ball"))