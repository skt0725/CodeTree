n = int(input())
arr = []
import heapq
for _ in range(n):
    x = int(input())
    match x:
        case 0:
            if not arr: print(0)
            else:
                print(-heapq.heappop(arr))
        case _:
            heapq.heappush(arr, -x)