# 스택 수열 (실2)

N = int(input())
numbers = list(int(input()) for _ in range(N))

stack = []
ans = []
cur = 1 
for num in numbers:
    while cur <= num:
        stack.append(cur)
        ans.append('+')
        cur += 1

    if stack[-1] == num :
        ans.append('-')
        stack.pop()
    
    else: 
        print('NO')
        break

else:
    print(*ans, sep = '\n')

