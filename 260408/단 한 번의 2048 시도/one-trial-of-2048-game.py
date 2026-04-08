# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
def process(row):
    row = list(filter(lambda x: x>0, row))
    if not row: return [0, 0, 0, 0]
    temp = []
    cur_num = row[0]
    for i in range(1, len(row)):
        if row[i] == cur_num:
            temp.append(cur_num*2)
            cur_num = 0
        else:
            if cur_num:
                temp.append(cur_num)
            cur_num = row[i]
    if cur_num: temp.append(cur_num)
    temp += [0]*(4-len(temp))
    return temp
def press(dir, arr):
    if dir == 'R':
        for i in range(4):
            temp = process(arr[i][::-1])
            arr[i] = temp[::-1]
    if dir == 'L':
        for i in range(4):
            temp = process(arr[i])
            arr[i] = temp

if dir == 'R' or dir == 'L':
    press(dir, grid)
else:
    temp = [[grid[i][j] for i in range(4)] for j in range(4)]

    if dir == 'D': dir = 'R'
    else: dir = 'L'
    press(dir, temp)
    for i in range(4):
        for j in range(4):
            grid[j][i] = temp[i][j]

for row in grid:
    print(*row)
