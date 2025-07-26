# Assume impl with tries for efficiency
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

def word_rectangle(dictionary: list[str]) -> int:
    groups = defaultdict(list)
    for word in dictionary:
        groups[len(word)].append(word)
    max_area = 0
    max_len = max(groups.keys())
    for w in range(max_len, 0, -1):
        if w * w <= max_area:
            continue
        if w not in groups:
            continue
        for h in range(max_len // w, 0, -1):
            if h * w <= max_area:
                continue
            if h not in groups:
                continue

            col_trie = TrieNode()
            for word in groups[h]:
                node = col_trie
                for c in word:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                    node = node.children[c]
                node.end = True

    return max_area