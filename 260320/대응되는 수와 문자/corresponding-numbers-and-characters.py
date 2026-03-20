n, m = tuple(map(int, input().split()))
hash = {}
hash_ = {}

for i in range(n):
    str = input()
    hash[str] = i+1
    hash_[i+1] = str
    
for i in range(m):
    target = input()
    if target.isnumeric():
        print(hash_[int(target)])
    else:
        print(hash[target])
