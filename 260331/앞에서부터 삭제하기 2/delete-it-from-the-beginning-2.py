n = int(input())
nums = list(map(int, input().split()))
import heapq
answer = 0
arr = [nums[n-1]]
for k in range(n-2, 0, -1):
    heapq.heappush(arr, nums[k])
    avg = (sum(arr)-arr[0])/(len(arr)-1)
    answer = max(answer, avg)
print(f'{answer:.2f}')
