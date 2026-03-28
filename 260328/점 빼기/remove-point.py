n, m = tuple(map(int, input().split()))
points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [int(input()) for _ in range(m)]
from sortedcontainers import SortedSet
s = SortedSet(points)

for query in queries:
    index = s.bisect_left((query, 0))
    if index == len(s):
        print(-1, -1)
    else:
        print(*s[index])
        s.remove(s[index])

