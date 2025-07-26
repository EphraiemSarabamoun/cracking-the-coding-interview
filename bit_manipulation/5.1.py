def insertion(n: int, m: int, i: int, j: int) -> int:
    all_ones = ~0 
    left = all_ones << (j + 1)
    right = (1 << i) - 1
    mask = left | right
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted

if __name__ == "__main__":
    print(insertion(1024, 19, 2, 6))
