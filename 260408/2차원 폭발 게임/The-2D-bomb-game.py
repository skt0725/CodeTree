n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def bomb():
    for c in range(n):
        column = [numbers_2d[i][c] for i in range(n) if numbers_2d[i][c] != 0]
        if not column: continue
        start = 0
        cur_num = column[0]
        for i in range(1, len(column)):
            if cur_num != column[i]:
                if i-start >= m:
                    column[start:i] = [0]*(i-start)
                start = i
                cur_num = column[i]
        if len(column) - start >= m:
            column[start:] = [0]*(len(column)-start)
        column = list(filter(lambda x: x>0, column))
        column = [0]*(n-len(column))+column
        for i in range(len(column)):
            numbers_2d[i][c] = column[i]


def rotate():
    temp = [[numbers_2d[n-1-i][j] for i in range(n)] for j in range(n)]
    for c in range(n):
        column = [temp[i][c] for i in range(n) if temp[i][c] != 0]
        if not column: break
        column = [0]*(n-len(column)) + column
        for i in range(n):
            temp[i][c] = column[i]
    for i in range(n):
        for j in range(n):
            numbers_2d[i][j] = temp[i][j]

for _ in range(k):
    bomb()
    rotate()
bomb()

answer = 0
for row in numbers_2d:
    answer += sum(1 for i in range(n) if row[i] != 0)
print(answer)