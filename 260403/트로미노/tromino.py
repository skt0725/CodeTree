n, m = tuple(map(int, input().split()))
world = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if i <= n-2 and j <= m-2:
            square = [world[i+k][j+l] for k in range(2) for l in range(2)]
            min_square = min(square)
            answer = max(answer, sum(square)-min_square)
        if j <= m-3:
            row = [world[i][j+k] for k in range(3)]
            answer = max(answer, sum(row))
        if i <= n-3:
            column = [world[i+k][j] for k in range(3)]
            answer = max(answer, sum(column))
print(answer)
        


    