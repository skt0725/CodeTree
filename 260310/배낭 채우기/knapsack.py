n, m = tuple(map(int, input().split()))
jewels = [tuple(map(int, input().split())) for _ in range(n)]
jewels.sort()

dp = [[0] * (m+1) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m+1):
        if jewels[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-jewels[i][0]] + jewels[i][1], dp[i-1][j])
            answer = max(answer, dp[i][j])
print(dp[-1][-1])

        