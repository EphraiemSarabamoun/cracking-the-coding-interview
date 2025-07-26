def sub_sort(arr: list[int]) -> tuple[int, int]:
    if not arr:
        return (-1, -1)
    min_right = arr[-1]
    end_left = -1
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > min_right:
            end_left = i
        min_right = min(min_right, arr[i])
    if end_left == -1:
        return (0, 0)  
    max_left = arr[0]
    start_right = -1
    for i in range(1, len(arr)):
        if arr[i] < max_left:
            start_right = i
        max_left = max(max_left, arr[i])
    return (end_left, start_right)

def sub_sort_correct(arr: list[int]) -> tuple[int, int]:
    max_so_far = float('-inf')
    right_bound = -1
    for i in range(len(arr)):
        max_so_far = max(max_so_far, arr[i])
        if arr[i] < max_so_far:
            right_bound = i
    if right_bound == -1:
        return (-1, -1)
    min_so_far = float('inf')
    left_bound = -1
    for i in range(len(arr) - 1, -1, -1):
        min_so_far = min(min_so_far, arr[i])
        if arr[i] > min_so_far:
            left_bound = i
    return (left_bound, right_bound)