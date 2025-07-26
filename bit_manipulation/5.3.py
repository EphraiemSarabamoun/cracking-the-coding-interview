def flip_bit_to_win(num: int) -> int:
    if ~num == 0:  # All 1s
        return bin(num).count('1')
    prev = current = max_len = 0
    while num:
        if num & 1:
            current += 1
        else:
            prev = current if (num & 2) == 0 else 0  # If next is 0, no merge
            current = 0
        max_len = max(max_len, current + prev + 1)
        num >>= 1
    return max_len

if __name__ == "__main__":
    print(flip_bit_to_win(1775))