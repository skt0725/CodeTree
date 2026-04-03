n = int(input())
world = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n-2):
    for j in range(n-2):
        temp = sum(world[i+k][j+l] for k in range(3) for l in range(3))
        answer = max(answer, temp)
print(answer)