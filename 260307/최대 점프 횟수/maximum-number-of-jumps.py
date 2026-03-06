n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    for j in range(i):
        if nums[j] >= i-j:
            if j == 0 or dp[j] > 0:
                dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))