n = int(input())
from collections import defaultdict
scent = {}
dose = defaultdict(list)
end = 0
def prepare(*args):
    global end
    for i in range(1, len(args)+1):
        scent[i] = args[i-1]
        dose[args[i-1]].append(i)
    end = len(args) + 1

def add(v):
    global end
    scent[end] = v
    dose[v].append(end)
    end += 1

def delete(idx):
    if idx in scent:
        dosage = scent[idx]
        dose[dosage].remove(idx)
        if not dose[dosage]:
            del dose[dosage]
        return scent.pop(idx)
    else:
        return -1

def blend(k):
    possible = dose.keys()
    result = [4000] * (k+1)
    for p in possible:
        if p <= k:
            result[p] = 1
    for i in range(1, k+1):
        for j in possible:
            if i >= j and result[i-j] != 4000:
                result[i] = min(result[i-j] + 1, result[i])
    return result[-1] if result[-1] != 4000 else -1

def compose(k):
    ans = 0
    freq = [0] * 3001
    possible = list(dose.keys())
    for p in possible:
        freq[p] += len(dose[p])
    acc = [0] * 3002
    for v in range(3000, 0, -1):
        acc[v] = acc[v+1] + freq[v]
    n = len(possible)
    for i in range(n):
        for j in range(n):
            remainder = k - possible[i] - possible[j]
            if remainder <= 0:
                ans += freq[possible[i]] * freq[possible[j]] * acc[1]
            else:
                ans += freq[possible[i]] * freq[possible[j]] * acc[remainder]
    return ans

for _ in range(n):
    num, *oper = list(map(int, input().split()))
    if num == 1:
        prepare(*oper[1:])
    elif num == 2:
        add(oper[0])
    elif num == 3:
        print(delete(oper[0]))
    elif num == 4:
        print(blend(oper[0]))
    else:
        print(compose(oper[0]))

