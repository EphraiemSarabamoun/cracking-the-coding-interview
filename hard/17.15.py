def longest_word(words: list[str]) -> str:
    word_set = set(words)
    words.sort(key=lambda w: -len(w))
    memo = {}
    def can_build(word: str) -> bool:
        if word in memo:
            return memo[word]
        if not word:
            return True
        for i in range(1, len(word)):
            prefix = word[:i]
            if prefix in word_set and can_build(word[i:]):
                memo[word] = True
                return True
        memo[word] = False
        return False
    for word in words:
        word_set.remove(word)
        if can_build(word):
            return word
        word_set.add(word)
    return ""