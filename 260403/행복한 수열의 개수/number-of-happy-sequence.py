n, m = tuple(map(int, input().split()))
world = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def check(arr):
    temp = 1
    max_len = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            temp += 1
            max_len = max(max_len, temp)
        else:
            temp = 1
    return 1 if max_len >= m else 0

for i in range(n):
    row = world[i]
    answer += check(row)
    column = [world[j][i] for j in range(n)]
    answer += check(column)

print(answer)


