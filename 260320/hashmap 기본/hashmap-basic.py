n = int(input())
hash = dict()
for _ in range(n):
    operation = list(input().split())
    if operation[0] == 'add':
        hash[int(operation[1])] = int(operation[2])
    elif operation[0] == 'find':
        if int(operation[1]) in hash:
            print(hash[int(operation[1])])
        else:
            print('None')
    else:
        hash.pop(int(operation[1]))
