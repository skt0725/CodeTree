n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(lambda x: int(x)-1, input().split())

# Please write your code here.
def inrange(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False
def explode(r, c):
    direcs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    length = grid[r][c]-1
    grid[r][c] = 0
    for idx, direc in enumerate(direcs):
        r_c, c_c = r, c
        for _ in range(length):
            r_n, c_n = r_c + direc[0], c_c + direc[1]
            if inrange(r_n, c_n):
                grid[r_n][c_n] = 0
                r_c, c_c = r_n, c_n
            else: break
def collapse():
    for col in range(n):
        temp = [grid[i][col] for i in range(n)]
        temp.sort(key = lambda x: x != 0)
        for i in range(n):
            grid[i][col] = temp[i]


explode(r, c)

collapse()
for row in grid:
    print(*row)