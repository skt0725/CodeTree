import sys
n, m = tuple(map(int, input().split()))
coins = list(map(int, input().split()))
int_max = sys.maxsize
dp = [int_max] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for j in range(n):
        if coins[j] <= i and dp[i-coins[j]] != int_max:
            dp[i] = min(dp[i], dp[i-coins[j]] + 1)
print(dp[-1])
