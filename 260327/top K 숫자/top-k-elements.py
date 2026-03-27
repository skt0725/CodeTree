n, k = tuple(map(int, input().split()))

from sortedcontainers import SortedSet

s = SortedSet(list(map(lambda x: -int(x), input().split())))
for i in range(k):
    print(-s[i], end=' ')