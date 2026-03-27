n, m = tuple(map(int, input().split()))
nums = [int(input()) for _ in range(n)]

from sortedcontainers import SortedSet

s = SortedSet()
answer = -1

for i in range(n):
    if not s:
        s.add(nums[i])
    else:
        index = s.bisect_right(nums[i])
        if index == len(s):
            diff = nums[i]-s[-1]
        elif index == 0:
            diff = s[0]-nums[i]
        else:
            diff = min(s[index]-nums[i], nums[i]-s[index-1])
        if diff >= m:
            if answer == -1:
                answer = diff
            else:
                answer = min(answer, diff)

print(answer)
