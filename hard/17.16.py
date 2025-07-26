def masseuse(arr: list[int]) -> int:
    if not arr:
        return 0
    if len(arr) <= 2:
        return max(arr or [0])
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    return dp[-1]