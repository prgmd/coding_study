from collections import deque
import sys
input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
    order = input().strip()

    if order == 'size':
        print(len(q))
    elif order == 'empty':
        print(0 if q else 1)
    elif order == 'front':
        print(q[0] if q else -1)
    elif order == 'back':
        print(q[-1] if q else -1)
    else:
        if order[1] == 'o':
            if order[4] == 'f':
                print(q.popleft() if q else -1)
            else:
                print(q.pop() if q else -1)
        else:
            if order[5] == 'f':
                num = int(order[11:])
                q.appendleft(num)
            else:
                num = int(order[10:])
                q.append(num)              