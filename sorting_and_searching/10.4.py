class Listy:
    def __init__(self,arr):
        self.arr = arr
    def element_at(self,i):
        return self.arr[i] if 0 <= i < len(self.arr) else -1

def search_no_size(listy,target):
    idx = 1
    while listy.element_at(idx) != -1 and listy.element_at(idx) < target:
        idx *= 2
    low, high = idx // 2, idx
    while low <= high:
        mid = (low + high) // 2
        mid_val = listy.element_at(mid)
        if mid_val == target:
            return mid
        if mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    listy = Listy([1,2,3,4,5,6,7,8,9,10])
    print(search_no_size(listy, 7))

