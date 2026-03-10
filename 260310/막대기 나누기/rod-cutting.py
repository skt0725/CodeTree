n = int(input())
cost = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for index in range(1,n+1):
    for length in range(1, n+1):
        if length < index:
            dp[index][length] = dp[index-1][length]
        else:
            dp[index][length] = max(max(dp[index-1][length-index], dp[index][length-index]) + cost[index-1], dp[index-1][length])
print(dp[-1][-1])