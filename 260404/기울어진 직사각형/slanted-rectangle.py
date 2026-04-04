n = int(input())
world = [list(map(int, input().split())) for _ in range(n)]

direcs = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
answer = 0
def inrange(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else: return False

def rectangle(i, j, x, y):
    arr = []
    cur_x, cur_y = i, j
    for direc in range(4):
        length = x if not direc % 2 else y
        for i in range(length):
            new_x, new_y = cur_x + direcs[direc][0], cur_y + direcs[direc][1]
            if inrange(new_x, new_y):
                cur_x, cur_y = new_x, new_y
                arr.append((cur_x, cur_y))
            else:
                return []
    return arr
for i in range(2, n):
    for j in range(1, n-1):
        for x in range(1, n):
            for y in range(1, n):
                temp = 0
                points = rectangle(i, j, x, y)
                if points:
                    for point in points:
                        temp += world[point[0]][point[1]]
                answer = max(temp, answer)
print(answer)

                

