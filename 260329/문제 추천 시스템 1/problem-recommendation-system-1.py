n = int(input())
from sortedcontainers import SortedSet
s = SortedSet([tuple(map(int, input().split()[::-1])) for _ in range(n)])

m = int(input())
for i in range(m):
    operation = input().split()
    oper = operation[0]
    if oper == 'ad':
        num1, num2 = int(operation[2]), int(operation[1])
        s.add((num1, num2))
    elif oper == 'sv':
        num1, num2 = int(operation[2]), int(operation[1])
        s.remove((num1, num2))
    else:
        if int(operation[1]) == 1:
            print(s[-1][1])
        else:
            print(s[0][1])

