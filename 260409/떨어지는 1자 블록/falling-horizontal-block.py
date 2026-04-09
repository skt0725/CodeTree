n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
k = k-1
row = 0
for i in range(1, n):
    if any(x > 0 for x in grid[i][k:m+k]):
        break
    else:
        row += 1
grid[row][k:m+k] = [1]*m
for row in grid:
    print(*row)
