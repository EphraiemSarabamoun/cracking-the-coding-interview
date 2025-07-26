def sorted_merge(a,b, len_a):
    i = len_a -1
    j = len(b) - 1 
    k = len(a) - 1
    while i >= 0 and j>=0: 
        if a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1
    while j >= 0:
        a[k] = b[j]
        j -= 1
        k -= 1
    return a

if __name__ == "__main__":
    a = [1,2,3,0,0,0]
    b = [2,5,6]
    print(sorted_merge(a,b,3))
