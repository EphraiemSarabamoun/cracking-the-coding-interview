from collections import deque

def word_transformer(start: str, end: str, dictionary: set[str]) -> int:
    if start == end:
        return 0
    dictionary.add(end)
    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in dictionary and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    return -1