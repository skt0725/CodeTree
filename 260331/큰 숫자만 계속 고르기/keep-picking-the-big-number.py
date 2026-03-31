n, m = tuple(map(int, input().split()))
nums = list(map(lambda x: -int(x), input().split()))

arr = []
import heapq
for num in nums:
    heapq.heappush(arr, num)
for _ in range(m):
    temp = heapq.heappop(arr)
    heapq.heappush(arr, temp+1)
print(-arr[0])