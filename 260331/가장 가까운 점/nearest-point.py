n, m = tuple(map(int, input().split()))
nums = [tuple(map(int, input().split())) for _ in range(n)]
arr = []
import heapq

for num in nums:
    heapq.heappush(arr, (num[0]+num[1], num[0], num[1]))
for _ in range(m):
    dist, x, y = heapq.heappop(arr)
    heapq.heappush(arr, (dist+4, x+2, y+2))
print(arr[0][1], arr[0][2])
