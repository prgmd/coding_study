from collections import deque
import sys
input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
    order = input().strip()

    if order == 'pop':
        print(q.popleft() if q else -1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        print(0 if q else 1)
    elif order == 'front':
        print(q[0] if q else -1)
    elif order == 'back':
        print(q[-1] if q else -1)
    else:
        num = int(order[5:])
        q.append(num)