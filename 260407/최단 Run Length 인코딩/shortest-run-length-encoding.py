A = input()

# Please write your code here.
n = len(A)
answer = 10000
def incode(arr):
    cur_char = arr[0]
    rep = 1
    incode = ''
    for i in range(1, len(arr)):
        if arr[i] == cur_char:
            rep += 1
        else:
            incode += cur_char+str(rep)
            cur_char = arr[i]
            rep = 1
        if i == len(arr)-1:
            incode += cur_char+str(rep)
    return len(incode)

for i in range(n):
    A = A[n-1]+A[:n-1]
    answer = min(answer, incode(A))
print(answer)
    
