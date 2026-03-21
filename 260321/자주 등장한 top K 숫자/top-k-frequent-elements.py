n, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

from collections import defaultdict
hash = defaultdict(int)

for num in nums:
    hash[num] += 1

hash = sorted(hash.items(), key = lambda x: (-x[1], -x[0]))
for i in hash[:k]:
    print(i[0], end = ' ')