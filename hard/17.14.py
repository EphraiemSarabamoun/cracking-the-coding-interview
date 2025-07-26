import heapq

def smallest_k(arr: list[int], k: int) -> list[int]:
    if k <= 0:
        return []
    if k >= len(arr):
        return sorted(arr)
    heap = [-arr[i] for i in range(k)]  # Max heap negate
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        if -heap[0] > arr[i]:
            heapq.heappop(heap)
            heapq.heappush(heap, -arr[i])
    return [-x for x in heap]