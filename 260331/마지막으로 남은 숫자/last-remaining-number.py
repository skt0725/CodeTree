n = int(input())
nums = list(map(int, input().split()))
arr = []
import heapq
for num in nums:
    heapq.heappush(arr, -num)
while len(arr) >= 2:
    num1 = heapq.heappop(arr)
    num2 = heapq.heappop(arr)
    if num1 != num2:
        heapq.heappush(arr, num1-num2)
print(heapq.heappop(arr) if arr else -1)