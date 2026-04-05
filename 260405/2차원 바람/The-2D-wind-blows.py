n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]
direcs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# Please write your code here.
def rotate(x1, y1, x2, y2):
    lenx = x2-x1
    leny = y2-y1
    cur_x, cur_y = x1, y1
    temp = a[x1][y1]
    for idx, direc in enumerate(direcs):
        length = lenx if idx % 2 == 0 else leny
        for l in range(length):
            new_x, new_y = cur_x + direc[0], cur_y + direc[1]
            a[cur_x][cur_y] = a[new_x][new_y]
            cur_x, cur_y = new_x, new_y
    a[cur_x][cur_y+1] = temp 
        

            
    


def average(x1, y1, x2, y2):
    temp = [[0]*(y2-y1+1) for _ in range(x2-x1+1)]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            neigh_sum = a[x][y]
            neigh_count = 1
            for direc in direcs:
                n_x, n_y = x+direc[0], y+direc[1]
                if 0 <= n_x < n and 0 <= n_y < m:
                    neigh_sum += a[n_x][n_y]
                    neigh_count += 1
            neigh_avg = neigh_sum // neigh_count
            temp[x-x1][y-y1] = neigh_avg
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            a[x][y] = temp[x-x1][y-y1]




for wind in winds:
    x1, y1, x2, y2 = wind
    rotate(x1, y1, x2, y2)
    average(x1, y1, x2, y2)
for row in (a):
    print(*row)



