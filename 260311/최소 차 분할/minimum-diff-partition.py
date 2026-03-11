n = int(input())
nums = list(map(int, input().split()))
sum_nums = sum(nums)
dp = [0] * (sum_nums//2+1)
dp[0] = 1

for i in range(len(nums)):
    for j in range(1, sum_nums//2+1):
        if nums[i] > j or dp[j] == 1: continue
        else:
            dp[j] = 1 if dp[j-nums[i]] else 0

k = 0
for i in range(sum(nums)//2, -1, -1):
    if dp[i]:
        k = i
        break
print(sum_nums - 2*k)

