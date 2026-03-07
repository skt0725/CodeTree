n = int(input())
albeits = [tuple(map(int, input().split())) for _ in range(n)]

dp = [albeits[i][2] for i in range(n)]

for i in range(1, n):
    for j in range(i):
        cur_start, cur_end = albeits[i][0], albeits[i][1]
        prev_start, prev_end = albeits[j][0], albeits[j][1]

        if prev_end < cur_start:
            dp[i] = max(dp[j] + albeits[i][2], dp[i])

print(max(dp))