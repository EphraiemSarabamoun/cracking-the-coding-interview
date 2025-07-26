def group_anagrams(strings):
    return sorted(strings, key=lambda s: ''.join(sorted(s)))

if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))