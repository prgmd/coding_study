import sys
input = sys.stdin.readline

n = int(input())
number = [i for i in range(n, 0, -1)]
ideal = []

for _ in range(n):
    ideal.append(int(input()))

ideal_stack = []
stack = []
answer = []
idx = 0

while number:
    now = number.pop()
    if now == ideal[idx]:
        idx += 1
        ideal_stack.append(now)
        answer.append('+')
        answer.append('-')
        while stack:
            if stack[-1] == ideal[idx]:
                ideal_stack.append(stack.pop())
                idx += 1
                answer.append('-')
            else:
                break
    else:
        stack.append(now)
        answer.append('+')

if ideal == ideal_stack:
    for a in answer:
        print(a)
else:
    print('NO')