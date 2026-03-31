import heapq
arr = []

n = int(input())
for _ in range(n):
    oper = input().split()
    match oper[0]:
        case 'push':
            heapq.heappush(arr, -int(oper[1]))
        case 'size':
            print(len(arr))
        case 'empty':
            if arr:
                print(0)
            else:
                print(1)

        case 'pop':
            print(-heapq.heappop(arr))
        case _:
            print(-arr[0])
        