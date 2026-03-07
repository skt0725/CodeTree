n, m = tuple(map(int, input().split()))
coins = list(map(int, input().split()))
import sys
int_min = -sys.maxsize
dp = [int_min]*(m+1)
dp[0] = 0

for i in range(1, m+1):
    for j in range(n):
        if i >= coins[j] and dp[i-coins[j]] != int_min:
            dp[i] = max(dp[i], dp[i-coins[j]]+1)

answer = dp[-1] if dp[-1] != int_min else -1
print(answer)