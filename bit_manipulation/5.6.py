def bit_flip_count(a: int, b: int) -> int:
    diff = a ^ b
    count = 0
    while diff:
        count += diff & 1
        diff >>= 1
    return count

if __name__ == "__main__":
    print(bit_flip_count(31, 14))