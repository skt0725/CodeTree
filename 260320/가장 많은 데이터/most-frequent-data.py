n = int(input())

hash = {}
for _ in range(n):
    str = input()
    if str not in hash:
        hash[str] = 1
    else:
        hash[str] += 1
answer = 0
for k in hash:
    answer = max(answer, hash[k])
print(answer)