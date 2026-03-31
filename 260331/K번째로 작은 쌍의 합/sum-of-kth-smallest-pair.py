n, m, k = tuple(map(int, input().split()))
ns = list(map(int, input().split()))
ms = list(map(int, input().split()))

import heapq
k_arr = []
other_arr = []

for n_ in ns:
    for m_ in ms:
        num = n_+m_
        if len(k_arr) < k-1:
            heapq.heappush(k_arr, -num)
        else:
            # other_arr에 더함
            temp = -k_arr[0]
            if temp > num:
                heapq.heappop(k_arr)
                heapq.heappush(k_arr, -num)
                heapq.heappush(other_arr, temp)
            else:
                heapq.heappush(other_arr, num)
print(other_arr[0])

        
