n, m = tuple(map(int, input().split()))
world = [list(map(int, input().split())) for _ in range(n)]

answer = -1
def rectangle(i_start, j_start, i_end, j_end):
    num = 0
    for i in range(i_start, i_end + 1):
        for j in range(j_start, j_end + 1):
            if world[i][j] <= 0: return -1
            num += 1
    return num
for i_start in range(n):
    for j_start in range(m):
        for i_end in range(i_start, n):
            for j_end in range(j_start, n):
                num_square = rectangle(i_start, j_start, i_end, j_end)
                answer = max(answer, num_square)
print(answer)