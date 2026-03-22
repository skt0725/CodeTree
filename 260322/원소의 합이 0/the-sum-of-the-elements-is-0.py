n = int(input())

numbers = [list(map(int, input().split())) for _ in range(4)]

from collections import defaultdict

hash = defaultdict(int)

for number in numbers[0]:
    hash[number] += 1

for i in range(1, 4):
    number = numbers[i]
    items = list(hash.items())
    hash = defaultdict(int)
    for key, value in items:
        for j in range(n):
            temp = number[j] + key
            hash[temp] += value
print(hash[0])
        
        