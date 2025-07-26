
def get_next(num: int) -> int:
    temp = num
    c0 = c1 = 0
    while temp & 1 == 0 and temp != 0:
        c0 += 1
        temp >>= 1
    while temp & 1 == 1:
        c1 += 1
        temp >>= 1
    if c0 + c1 == 0 or c0 + c1 == 31:  
        return -1
    p = c0 + c1
    num |= (1 << p) 
    num &= ~((1 << p) - 1)  
    num |= (1 << (c1 - 1)) - 1 
    return num

def get_prev(num: int) -> int:
    temp = num
    c1 = c0 = 0
    while temp & 1 == 1:
        c1 += 1
        temp >>= 1
    if temp == 0:
        return -1
    while temp & 1 == 0 and temp != 0:
        c0 += 1
        temp >>= 1
    p = c1 + c0
    num &= ~((1 << (p + 1)) - 1)  
    mask = (1 << (c1 + 1)) - 1
    num |= mask << (c0 - 1)
    return num

if __name__ == "__main__":
    print(get_next(10))
    print(get_prev(10))