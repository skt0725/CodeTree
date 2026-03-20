n = int(input())
nums = list(map(int, input().split()))
sum_nums = sum(nums)
if sum_nums % 2:
    print('No')
else:
    dp = [0] * (sum_nums//2 + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(len(dp)-1, nums[i]-1, -1):
            dp[j] = max(dp[j-nums[i]], dp[j])

    print('Yes' if dp[-1] == 1 else 'No')
