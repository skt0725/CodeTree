n, m = tuple(map(int, input().split()))
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]

for index in range(1,n+1):
    for length in range(1, m+1):
        if length < cost[index-1][0]:
            dp[index][length] = dp[index-1][length]
        else:
            dp[index][length] = max(max(dp[index-1][length-cost[index-1][0]], dp[index][length-cost[index-1][0]]) + cost[index-1][1], dp[index-1][length])
print(dp[-1][-1])