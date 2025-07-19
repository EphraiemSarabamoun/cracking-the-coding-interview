def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)



if __name__ == "__main__":
    print(check_permutation("abc", "bca"))