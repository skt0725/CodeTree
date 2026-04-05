n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
def check_propagate(row1, row2):
    for i in range(m):
        if a[row1][i] == a[row2][i]:
            return True
    return False

def shift(index, direc):
    if direc == 'R':
        temp = a[index][0]
        for i in range(m-1):
            a[index][i] = a[index][i+1]
        a[index][-1] = temp
    else:
        temp = a[index][-1]
        for i in range(m-1, 0, -1):
            a[index][i] = a[index][i-1]
        a[index][0] = temp


for wind in winds:
    row, direc = wind
    row = int(row)-1
    shift(row, direc)
    up_direc, low_direc = direc, direc
    for i in range(row-1, -1, -1):
        if low_direc == 'R': low_direc = 'L'
        else: low_direc = 'R'
        if check_propagate(i, i+1):
            shift(i, low_direc)
        else: break
    for j in range(row+1, n):
        if up_direc == 'R': up_direc = 'L'
        else: up_direc = 'R'
        if check_propagate(j, j-1):
            shift(j, up_direc)
        else: break

for row in a:
    print(*row)
   

