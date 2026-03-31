T = int(input())
import heapq
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    min_heap = []
    max_heap = []
    for idx, num in enumerate(nums):
        if not min_heap:
            heapq.heappush(min_heap, -num)
        else:
            if len(min_heap) == len(max_heap):
                temp = max_heap[0]
                if num > temp:
                    heapq.heappop(max_heap)
                    heapq.heappush(min_heap, -temp)
                    heapq.heappush(max_heap, num)
                else:
                    heapq.heappush(min_heap, -num)
            else:
                temp = -min_heap[0]
                if num < temp:
                    heapq.heappop(min_heap)
                    heapq.heappush(max_heap, temp)
                    heapq.heappush(min_heap, -num)
                else:
                    heapq.heappush(max_heap, num)
    
        if idx % 2 == 0: print(-min_heap[0], end = ' ')
    print()

