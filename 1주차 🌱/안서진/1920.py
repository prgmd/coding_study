# 여기에 코드를 입력해주세요
N = int(input())
A_numbers = set(map(int, input().split()))

M = int(input())
find_numbers = list(map(int, input().split()))

for num in find_numbers:
    if num in A_numbers:
        print(1)
    else:
        print(0)