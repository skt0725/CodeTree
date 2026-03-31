import heapq
arr = []
num = int(input())
for i in range(num):
    oper = int(input())
    match oper:
        case 0:
            if not arr:
                print(0)
            else:
                print(heapq.heappop(arr))
        case _:
            heapq.heappush(arr, oper)
