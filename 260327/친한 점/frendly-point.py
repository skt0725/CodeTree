n, m = tuple(map(int, input().split()))
from sortedcontainers import SortedSet
s = SortedSet([tuple(map(int, input().split())) for _ in range(n)])
queries = [tuple(map(int, input().split())) for _ in range(m)]

for x, y in queries:
    x_ind = s.bisect_left((x, y))
    if x_ind == n:
        print(-1, -1)
    else:
        print(*s[x_ind])

