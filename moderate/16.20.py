class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def t9(dictionary: list[str], digits: str) -> list[str]:
    if not digits:
        return []
    key_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    result = []
    def dfs(node: TrieNode, index: int, path: str):
        if index == len(digits):
            if node.word:
                result.append(node.word)
            return
        for char in key_map[digits[index]]:
            if char in node.children:
                dfs(node.children[char], index + 1, path + char)
    dfs(root, 0, '')
    return result