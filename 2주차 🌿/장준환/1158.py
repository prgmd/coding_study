n, k = map(int, input().split())
number = [i for i in range(1, n+1)]
answer = []
pos = k-1

for _ in range(n):
    if pos >= len(number):
        pos = pos % len(number)
    answer.append(number.pop(pos))
    pos += k-1

print('<', end = '')
for i in range(n):
    print(answer[i], end = '')
    if i == n-1:
        break
    else:
        print(', ', end = '')
print('>')