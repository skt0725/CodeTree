n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
def check():
    temp = []
    rep = 0
    cur_num = 0
    for number in numbers:
        if number == cur_num:
            rep += 1
        else:
            if rep < m:
                for _ in range(rep):
                    temp.append(cur_num)
            cur_num = number
            rep = 1
    if rep < m:
        for _ in range(rep):
            temp.append(cur_num)
    return temp

while True:
    temp = check()
    if len(temp) == len(numbers):
        numbers = temp
        break
    else:
        numbers = temp

print(len(numbers))
if numbers:
    for number in numbers:
        print(number)
    
