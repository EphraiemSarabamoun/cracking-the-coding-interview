def pairwise_swap(n: int) -> int:
    even_mask = 0xAAAAAAAA  # 1010... 
    odd_mask = 0x55555555   # 0101...
    return ((n & even_mask) >> 1) | ((n & odd_mask) << 1)

if __name__ == "__main__":
    print(pairwise_swap(10))