n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    for j in range(i):
        prev_start, prev_end = lines[j][0], lines[j][1]
        cur_start, cur_end = lines[i][0], lines[i][1]
        if prev_end < cur_start: 
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
