# 괄호 (9012)
T = int(input())

for _ in range(T):
  stack = []  
  input_string = list(input().strip())

  for i in input_string:
    if i == '(':
      stack.append(i)

    else:
      if not stack:
        print('NO')
        break
      else:
        stack.pop()
  else:
    print('NO' if stack else 'YES')