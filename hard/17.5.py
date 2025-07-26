def letters_numbers(arr: list[str]) -> int:
    prefix = 0
    max_len = 0
    sum_to_index = {0: -1}
    for i in range(len(arr)):
        prefix += 1 if arr[i].isalpha() else -1
        if prefix in sum_to_index:
            max_len = max(max_len, i - sum_to_index[prefix])
        else:
            sum_to_index[prefix] = i
    return max_len