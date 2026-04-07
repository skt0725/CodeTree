n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.
r -= 1
c -= 1

if dir == 1:
    direcs = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
    m = [m1, m2, m3, m4]
else:
    direcs = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    m = [m4, m3, m2, m1]

temp = grid[r][c]
x_cur, y_cur = r, c
for i in range(4):
    length = m[i]
    direc = direcs[i]
    for l in range(length):
        x_new, y_new = x_cur + direc[0], y_cur + direc[1]
        grid[x_cur][y_cur] = grid[x_new][y_new]
        x_cur, y_cur = x_new, y_new
    if i == 3:
        x_cur -= direc[0]
        y_cur -= direc[1]
        grid[x_cur][y_cur] = temp
for row in grid:
    print(*row)




