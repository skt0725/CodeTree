n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

dp = [-1] * (m+1)
dp[0] = 1

for i in range(n):
    for j in range(m, -1, -1):
        if j >= nums[i] and dp[j-nums[i]] != -1:
            dp[j] = 1

answer = "Yes" if dp[m] != -1 else "No"
print(answer)