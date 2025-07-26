def coins(n: int) -> int:
    if n < 0:
        return -1
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    denominations = [1, 5, 10, 25]
    for i in range(1, n + 1):
        for coin in denominations:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[n] if dp[n] != float('inf') else -1

if __name__ == "__main__":
    print(coins(11))