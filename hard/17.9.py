import heapq

def kth_multiple(k: int) -> int:
    if k <= 0:
        return 0
    heap = [1]
    seen = {1}
    factors = [3, 5, 7]
    for _ in range(k):
        min_val = heapq.heappop(heap)
        for f in factors:
            next_val = min_val * f
            if next_val not in seen:
                seen.add(next_val)
                heapq.heappush(heap, next_val)
    return min_val