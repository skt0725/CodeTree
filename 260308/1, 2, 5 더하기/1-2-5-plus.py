n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    temp = 0
    if i >= 1: temp += dp[i-1]
    if i >= 2: temp += dp[i-2]
    if i >= 5: temp += dp[i-5]
    dp[i] = max(dp[i], temp)

print(dp[-1]%10007)


