n, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

from collections import defaultdict, Counter

ctr = Counter(nums)
answer = 0
for i in range(n):
    ctr[nums[i]] -= 1
    for j in range(i):
        if k-nums[i]-nums[j] in ctr:
            answer += ctr[k-nums[i]-nums[j]]
print(answer)



