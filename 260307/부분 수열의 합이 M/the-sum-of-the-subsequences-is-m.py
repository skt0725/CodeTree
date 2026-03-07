import sys

int_max = sys.maxsize

n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

dp = [int_max] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(m, -1, -1):
        if j-nums[i] >= 0 and dp[j-nums[i]] != int_max:
            dp[j] = min(dp[j], dp[j-nums[i]] + 1)

answer = dp[-1] if dp[-1] != int_max else -1
print(answer)