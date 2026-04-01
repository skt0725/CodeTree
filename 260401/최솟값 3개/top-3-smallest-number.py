n = int(input())
nums = list(map(int, input().split()))
import heapq
arr = []

for i in range(n):
    num = -nums[i]
    heapq.heappush(arr, num)
    if len(arr) < 3: print(-1)
    elif len(arr) == 3:
        print(-arr[0]*arr[1]*arr[2])
    else:
        heapq.heappop(arr)
        print(-arr[0]*arr[1]*arr[2])
