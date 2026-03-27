n = int(input())
nums = list(map(int, input().split()))
from sortedcontainers import SortedSet
s = SortedSet([0])

min_dist = 0

for i in range(n):
    num = nums[i]
    if i == 0:
        min_dist = num
    else:
        temp_ind = s.bisect_right(num)
        if temp_ind == len(s):
            temp_min = num-s[-1]
        elif temp_ind == 0:
            temp_min = s[0]-num
        else:
            temp_min = min(s[temp_ind]-num, num-s[temp_ind-1])
        min_dist = min(temp_min, min_dist)
    s.add(num)
    print(min_dist)