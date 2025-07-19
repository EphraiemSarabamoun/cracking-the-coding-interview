def one_away(s1: str, s2: str) -> bool:
    if len(s1) == len(s2):
        difference = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                difference += 1
        return difference == 1
    if abs(len(s1)-len(s2)) > 1:
        return False
    else:
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        i,j = 0,0
        is_inserted = False
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i,j = i+1,j+1
            else:
                i += 1
                is_inserted = True
                return s1[i:] == s2[j:]
        if i == len(s1) and j == len(s2) and is_inserted:
            return True
        if j == len(s2) and not is_inserted:
            return True
        return False




if __name__ == "__main__":
    print(one_away("hello", "helo"))
    print(one_away("pale", "ple"))
    print(one_away("pales", "pale"))
    print(one_away("pale", "bale"))
    print(one_away("pale", "bake"))