str = input()
n = int(input())
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
cur = Node(str)
for _ in range(n):
    oper = input().split()
    match oper[0]:
        case '1':
            new = Node(oper[1])
            new.next = cur
            new.prev = cur.prev
            if cur.prev:
                cur.prev.next = new
            cur.prev = new
        case '2':
            new = Node(oper[1])
            new.prev = cur
            new.next = cur.next
            if cur.next:
                cur.next.prev = new
            cur.next = new
        case '3':
            if cur.prev:
                cur = cur.prev
        case '4':
            if cur.next:
                cur = cur.next
    print(cur.prev.data if cur.prev else '(Null)', end=' ')
    print(cur.data, end=' ')
    print(cur.next.data if cur.next else '(Null)')

