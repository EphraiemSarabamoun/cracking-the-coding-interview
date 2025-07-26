class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []  # List if multiple

def multi_search(big: str, smalls: list[str]) -> dict[str, list[int]]:
    root = TrieNode()
    for word in smalls:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.words.append(word)
    result = {word: [] for word in smalls}
    for i in range(len(big)):
        node = root
        for j in range(i, len(big)):
            char = big[j]
            if char not in node.children:
                break
            node = node.children[char]
            for word in node.words:
                result[word].append(i)
    return result