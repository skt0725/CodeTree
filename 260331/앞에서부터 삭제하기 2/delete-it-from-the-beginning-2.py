n = int(input())
nums = list(map(int, input().split()))
import heapq
answer = 0
for k in range(1, n-1):
    arr = []
    for num in nums[k:]:
        heapq.heappush(arr, num)
    heapq.heappop(arr)
    avg = sum(arr)/len(arr)
    answer = max(answer, avg)
print(f'{answer:.2f}')
