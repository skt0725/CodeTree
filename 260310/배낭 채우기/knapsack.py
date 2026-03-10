n, m = tuple(map(int, input().split()))
jewels = [tuple(map(int, input().split())) for _ in range(n)]
jewels.sort()

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m+1):
        if jewels[i][0] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j-jewels[i][0]] + jewels[i][1], dp[i][j])
print(dp[-1][-1])

        