def check_permutation(string: str) -> bool:
    s = string.lower().replace(" ", "")
    count = [0] * 128  
    for char in s:
        count[ord(char)] += 1
    odd_count = sum(1 for c in count if c % 2 == 1)
    if len(s) % 2 != 0:
        return odd_count == 1
    else:
        return odd_count == 0

if __name__ == "__main__":
    print(check_permutation("Tact Coa"))
    print(check_permutation("Anna ")) 
    print(check_permutation("Able was I ere I saw Elba"))
    print(check_permutation("No 'x' in Nixon"))

