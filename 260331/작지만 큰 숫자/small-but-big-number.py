n, m = tuple(map(int, input().split()))
from sortedcontainers import SortedSet
s = SortedSet(list(map(int, input().split())))
queries = list(map(int, input().split()))

for query in queries:
    index = s.bisect_right(query)
    if index == 0:
        print(-1)
    else:
        print(s[index-1])
        s.remove(s[index-1])
        