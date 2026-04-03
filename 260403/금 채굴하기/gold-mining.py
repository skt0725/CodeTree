n, m = tuple(map(int, input().split()))
world = [list(map(int, input().split())) for _ in range(n)]

answer = 1

for i in range(n):
    for j in range(n):
        for k in range(2, n+1):
            temp = 0
            mine = 0
            for l in range(-k+1, k): # -k+1, -k+2, ..., k-2. k-1 => 0 (-1 0 1) (-2 -1 0 1 2)
                length = k-abs(l)-1
                for o in range(-length, length+1):
                    if 0<=i+o<n and 0<=j+l<n:
                        if world[i+o][j+l] == 1:
                            temp += 1
            mine = (k*k + (k-1)*(k-1))
            if temp*m >= mine:
                answer = max(answer, temp)
print(answer)

        
