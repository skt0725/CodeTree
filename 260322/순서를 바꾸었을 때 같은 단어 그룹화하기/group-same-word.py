n = int(input())
from collections import defaultdict
hash = defaultdict(int)

for _ in range(n):
    word = ''.join(sorted(list(input())))
    hash[word] += 1

print(max(hash.values()))

