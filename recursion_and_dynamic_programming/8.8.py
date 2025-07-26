def perms_with_dups(s: str) -> list[str]:
    result = []
    s_list = sorted(list(s))
    used = [False] * len(s)
    def backtrack(path: list[str]):
        if len(path) == len(s):
            result.append(''.join(path))
            return
        for i in range(len(s)):
            if used[i]:
                continue
            if i > 0 and s_list[i] == s_list[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(s_list[i])
            backtrack(path)
            path.pop()
            used[i] = False
    backtrack([])
    return result

if __name__ == "__main__":
    print(perms_with_dups("aap"))