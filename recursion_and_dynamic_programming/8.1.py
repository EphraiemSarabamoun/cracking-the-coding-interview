def triple_step(n: int) -> int:
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] += dp[i-1] if i-1 >= 0 else 0
        dp[i] += dp[i-2] if i-2 >= 0 else 0
        dp[i] += dp[i-3] if i-3 >= 0 else 0
    return dp[n]

def triple_step_memo(n: int, memo={}) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = triple_step_memo(n-1, memo) + triple_step_memo(n-2, memo) + triple_step_memo(n-3, memo)
    return memo[n]

if __name__ == "__main__":
    print(triple_step(5))
    print(triple_step_memo(5))
