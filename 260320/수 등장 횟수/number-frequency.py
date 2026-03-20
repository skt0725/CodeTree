n, m = tuple(map(int, input().split()))
n_s = list(map(int, input().split()))
m_s = list(map(int, input().split()))

hash = dict()
for n_ in n_s:
    if n_ not in hash:
        hash[n_] = 1
    else:
        hash[n_] += 1

for m_ in m_s:
    print(hash[m_] if m_ in hash else 0, end=' ')