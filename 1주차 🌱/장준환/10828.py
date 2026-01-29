import sys
input = sys.stdin.readline
stack = []

for _ in range(int(input())):
    order = input().strip()

    if order == 'pop':
        print(stack.pop() if stack else -1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        print(0 if stack else 1)
    elif order == 'top':
        print(stack[-1] if stack else -1)
    else:
        num = int(order[5:])
        stack.append(num)