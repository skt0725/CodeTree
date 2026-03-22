n = int(input())

from collections import defaultdict

hash = defaultdict(int)

for _ in range(n):
    x, y = tuple(map(int, input().split()))
    if x not in hash: hash[x] = y
    else:
        hash[x] = min(hash[x], y)

print(sum(hash.values()))