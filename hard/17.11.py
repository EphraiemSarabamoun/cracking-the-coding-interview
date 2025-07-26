def word_distance(file_text: str, word1: str, word2: str) -> int:
    words = file_text.split()
    pos1 = pos2 = -1
    min_dist = float('inf')
    for i, word in enumerate(words):
        if word == word1:
            pos1 = i
            if pos2 != -1:
                min_dist = min(min_dist, pos1 - pos2)
        elif word == word2:
            pos2 = i
            if pos1 != -1:
                min_dist = min(min_dist, pos2 - pos1)
    return min_dist if min_dist != float('inf') else -1