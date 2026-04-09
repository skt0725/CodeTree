n, m, r, c = map(int, input().split())

# Please write your code here.
r -= 1
c -= 1
direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
bombs = {(r, c)}
def inrange(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False
for t in range(1, m+1):
    temp = set()
    for bomb in bombs:
        r_, c_ = bomb
        for direc in direcs:
            n_r, n_c = r_ + direc[0]* 2**(t-1), c_ + direc[1]* 2**(t-1)
            if inrange(n_r, n_c):
                temp.add((n_r, n_c))
    bombs |= temp
print(len(bombs))



        
