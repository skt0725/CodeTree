N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# Please write your code here.
def inrange(x, y):
    if 1 <= x <= N and 1 <= y <= N:
        return True
    return False
direcs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
direc = 0
cur_x, cur_y = x, y
answer = 0
while True:
    new_x, new_y = cur_x + direcs[direc][0], cur_y + direcs[direc][1]
    if inrange(new_x, new_y):
        if grid[new_x][new_y] == '#':
            direc = (direc+1) % 4
        else:
            temp_direc = (direc+3) % 4
            temp_x, temp_y = new_x + direcs[temp_direc][0], new_y + direcs[temp_direc][1]
            if inrange(temp_x,temp_y):
                if grid[temp_x][temp_y] == '#':
                    cur_x, cur_y = new_x, new_y
                    answer += 1
                else:
                    cur_x, cur_y = temp_x, temp_y
                    direc = temp_direc
                    answer += 2
    else:
        answer += 1
        break
    if cur_x == x and cur_y == y:
        answer = -1
        break
print(answer)


