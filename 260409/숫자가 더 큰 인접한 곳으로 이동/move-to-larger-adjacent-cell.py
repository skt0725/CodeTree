n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
def inrange(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False
direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cur_x, cur_y = r, c
while True:
    print(a[cur_x][cur_y], end=' ')
    move = False
    for direc in direcs:
        new_x, new_y = cur_x + direc[0], cur_y + direc[1]
        if inrange(new_x, new_y) and a[new_x][new_y] > a[cur_x][cur_y]:
            cur_x, cur_y = new_x, new_y
            move = True
            break
    if not move: break


