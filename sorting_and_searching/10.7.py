import struct

def find_missing_int(file_path: str) -> int:
    RANGE_SIZE = 1 << 22  # 4M
    NUM_BUCKETS = 1 << 10  # 1024
    buckets = [0] * NUM_BUCKETS
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(4)
            if len(data) < 4:
                break
            num = struct.unpack('<I', data)[0]
            bucket = num // RANGE_SIZE
            if bucket < NUM_BUCKETS:  # Prevent index errors for out-of-range nums
                buckets[bucket] += 1
    for bucket in range(NUM_BUCKETS):
        if buckets[bucket] < RANGE_SIZE:
            break
    else:
        return -1  # No missing number found
    start = bucket * RANGE_SIZE
    bits = [0] * ((RANGE_SIZE + 31) // 32)  # Bit array
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(4)
            if len(data) < 4:
                break
            num = struct.unpack('<I', data)[0]
            if start <= num < start + RANGE_SIZE:
                i = num - start
                bits[i // 32] |= (1 << (i % 32))
    for i in range(RANGE_SIZE):
        if not (bits[i // 32] & (1 << (i % 32))):
            return start + i
    return -1