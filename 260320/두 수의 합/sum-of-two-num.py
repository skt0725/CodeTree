n, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

from collections import defaultdict
hash = defaultdict(int)

for i in range(n):
    hash[nums[i]] += 1

answer = 0
for key in hash:
    if k-key in hash:
        if key == k-key: 
            answer += hash[key] * (hash[k-key] - 1)
        else: answer += hash[key] * hash[k-key]
    
print(answer // 2)