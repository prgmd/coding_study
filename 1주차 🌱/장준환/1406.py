from collections import deque
import sys
input = sys.stdin.readline
q = deque()
left_words = list(input().strip())
right_words = []

for _ in range(int(input())):
    order = input().strip()

    if order == 'L':
        if left_words:
            right_words.append(left_words.pop())
    elif order == 'D':
        if right_words:
            left_words.append(right_words.pop())
    elif order == 'B':
        if left_words:
            left_words.pop()
    else:
        left_words.append(order[2])

print(''.join(left_words+right_words[::-1]))