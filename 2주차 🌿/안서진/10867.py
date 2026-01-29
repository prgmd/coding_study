# 중복 빼고 정렬하기 (실5)

N = int(input())

numbers = list(set(list(map(int, input().split()))))

numbers.sort()
print(*numbers)