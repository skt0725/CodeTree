letter = list(input())

answer = 'None'

from collections import defaultdict

hash = defaultdict(int)

for l in letter:
    hash[l] += 1

for key in hash:
    if hash[key] == 1:
        answer = key
        break
        
print(answer)