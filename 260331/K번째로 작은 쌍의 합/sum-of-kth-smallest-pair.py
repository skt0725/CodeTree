n, m, k = tuple(map(int, input().split()))
ns = sorted(list(map(int, input().split())))
ms = sorted(list(map(int, input().split())))

import heapq
k_arr = []

for n_ in ns:
    for m_ in ms:
        num = n_+m_
        if len(k_arr) < k:
            heapq.heappush(k_arr, -num)
        else:
            temp = -k_arr[0]
            if num > temp:
                break
            else:
                heapq.heappop(k_arr)
                heapq.heappush(k_arr, -num) 
print(-k_arr[0])

        
