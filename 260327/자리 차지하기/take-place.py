n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

from sortedcontainers import SortedSet

s = SortedSet()

answer = 0
for num in nums:
    if not s:
        s.add(num)
    else:
        while num in s:
            num -= 1
        if num == 0:
            break
        else:
            s.add(num)
    answer += 1
print(answer)