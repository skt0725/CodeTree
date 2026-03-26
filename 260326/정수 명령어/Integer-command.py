T = int(input())
from sortedcontainers import SortedSet

s = SortedSet()

for _ in range(T):
    K = int(input())
    s.clear()
    for _ in range(K):
        oper, num = tuple(input().split())
        if oper == 'I':
            s.add(int(num))
        else:
            if not s: continue
            if int(num) == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])
    if not s:
        print('EMPTY')
    else:
        print(s[-1], s[0])
        