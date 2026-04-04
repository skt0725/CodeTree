n, m = tuple(map(int, input().split()))
world = [list(map(int, input().split())) for _ in range(n)]
import sys
answer = -sys.maxsize
def square(x_start, y_start, x_end, y_end):
    temp = 0
    for i in range(x_start, x_end+1):
        for j in range(y_start, y_end+1):
            temp += world[i][j]
    return temp
def duplicate(i_end, j_end, x_start, y_start):
    if x_start < i_end and y_start < j_end: return True
    elif x_start == i_end and y_start <= j_end: return True
    elif y_start == j_end and x_start <= i_end: return True
    return False
for i_start in range(n):
    for j_start in range(m):
        for i_end in range(i_start, n):
            for j_end in range(j_start, m):
                for x_start in range(i_start, n):
                    for y_start in range(j_start, m):
                        for x_end in range(x_start, n):
                            for y_end in range(y_start, m):
                                if duplicate(i_end, j_end, x_start, y_start): break
                                square_ij = square(i_start, j_start, i_end, j_end)
                                square_xy = square(x_start, y_start, x_end, y_end)
                                answer = max(answer, square_ij + square_xy)
print(answer)