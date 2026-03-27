n, m = tuple(map(int, input().split()))

from sortedcontainers import SortedSet

s = SortedSet(list(map(int, input().split())))
queries = [int(input()) for _ in range(m)]

for i in range(m):
    larger = s.bisect_left(queries[i])
    if larger == len(s):
        print(-1)
    else:
        print(s[larger])
        