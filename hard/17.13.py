def re_space(sentence: str, dictionary: set[str]) -> str:
    n = len(sentence)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    prev = [-1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if sentence[j:i] in dictionary:
                if dp[j] + 0 < dp[i]:
                    dp[i] = dp[j]
                    prev[i] = j
            else:
                if dp[j] + (i - j) < dp[i]:
                    dp[i] = dp[j] + (i - j)
                    prev[i] = -2  # Mark unrecognized
    # Reconstruct
    result = []
    i = n
    while i > 0:
        j = prev[i]
        if j == -2:
            result.append(sentence[i - (i - j):i])  # Unrecognized
        else:
            result.append(sentence[j:i])
        i = j
    return ' '.join(reversed(result))  # But unrecognized not marked, problem to add spaces, but min unrecognized.