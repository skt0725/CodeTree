n = int(input())
from sortedcontainers import SortedSet

sd = SortedSet()

for _ in range(n):
    operations = list(input().split())
    oper = operations[0]
    if oper == 'add':
        num = int(operations[1])
        sd.add(num)
    elif oper == 'remove':
        num = int(operations[1])
        sd.remove(num)
    elif oper == 'find':
        num = int(operations[1])
        if num in sd:
            print('true')
        else:
            print('false')
    elif oper == 'lower_bound':
        num = int(operations[1])
        temp = sd.bisect_left(num)
        if temp == len(sd):
            print('None')
        else:
            print(sd[temp])
    elif oper == 'upper_bound':
        num = int(operations[1])
        temp = sd.bisect_right(num)
        if temp == len(sd):
            print('None')
        else:
            print(sd[temp])
    elif oper == 'largest':
        print(sd[-1]) if sd else print('None')
    else:
        print(sd[0]) if sd else print('None')
