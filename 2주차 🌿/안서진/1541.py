# 잃어버린 괄호 (실2) - Greedy

sentence = input().split('-')
new_arr = []
for num in sentence:
    a = num.split('+')
    new_arr.append(list(map(int, a)))
    
ans = sum(new_arr[0])
for i in range(1, len(new_arr)):
    ans -= sum(new_arr[i])

print(ans)