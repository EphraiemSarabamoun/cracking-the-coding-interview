def master_mind(solution: str, guess: str) -> tuple[int, int]:
    if len(solution) != len(guess):
        return (0, 0)
    hits = 0
    freq = [0] * 26  # Assume letters A-Z
    for i in range(len(solution)):
        if solution[i] == guess[i]:
            hits += 1
        else:
            freq[ord(solution[i]) - ord('A')] += 1
    pseudo = 0
    for i in range(len(guess)):
        if solution[i] != guess[i]:
            if freq[ord(guess[i]) - ord('A')] > 0:
                pseudo += 1
                freq[ord(guess[i]) - ord('A')] -= 1
    return (hits, pseudo)