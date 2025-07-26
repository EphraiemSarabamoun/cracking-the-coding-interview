def power_set(s: list) -> list[list]:
    if not s:
        return [[]]
    subsets = []
    first = s[0]
    rest = power_set(s[1:])
    for sub in rest:
        subsets.append(sub)
        subsets.append([first] + sub)
    return subsets

# Bit mask
def power_set_bit(s: list) -> list[list]:
    subsets = []
    for i in range(1 << len(s)):  # 2^len
        sub = []
        for j in range(len(s)):
            if i & (1 << j):
                sub.append(s[j])
        subsets.append(sub)
    return subsets

if __name__ == "__main__":
    print(power_set([1, 2, 3]))
    print(power_set_bit([1, 2, 3]))
