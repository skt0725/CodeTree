n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

# Please write your code here.
def inrange(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False
def bomb(r, c):
    length = grid[r][c]-1
    grid[r][c] = 0
    if length == 0:
        return
    direcs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    for direc in direcs:
        r_cur, c_cur = r, c
        for _ in range(length):
            r_new, c_new = r_cur+direc[0], c_cur+direc[1]
            if inrange(r_new, c_new):
                grid[r_new][c_new] = 0
                r_cur, c_cur = r_new, c_new
            else:
                break
def move():
    for col in range(n):
        column = [grid[i][col] for i in range(n)]
        temp = list(filter(lambda x: x>0, column))
        temp = [0] * (n-len(temp)) + temp
        for i in range(n):
            grid[i][col] = temp[i]
for column in commands:
    column -= 1
    row = -1
    for i in range(n):
        if grid[i][column]:
            row = i
            break
    if row == -1:
        continue
    else:
        bomb(row, column)
        move()
for row in grid:
    print(*row)