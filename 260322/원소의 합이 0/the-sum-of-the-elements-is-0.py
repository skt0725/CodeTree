n = int(input())

numbers = [list(map(int, input().split())) for _ in range(4)]

from collections import defaultdict

hash = defaultdict(int)

for number in numbers[0]:
    hash[number] += 1

for i in range(1, 4):
    number = numbers[i]
    keys = list(hash.keys())
    
    for key in keys:
        for j in range(n):
            temp = number[j] + key
            hash[temp] += 1
print(hash[0])
        
        