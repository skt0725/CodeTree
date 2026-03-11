n = int(input())
nums = list(map(int, input().split()))
sum_nums = sum(nums)
dp = [0] * (sum_nums//2+1)
dp[0] = 1

for i in range(len(nums)):
    for j in range(sum_nums//2, 0, -1):
        if nums[i] > j or dp[j] == 1: continue
        else:
            if dp[j-nums[i]]:
                dp[j] = 1

k = 0
for i in range(sum(nums)//2, -1, -1):
    if dp[i]:
        k = i
        break
print(sum_nums - 2*k)

