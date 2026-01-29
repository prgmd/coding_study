# 좌표 정렬하기 (실5)

N = int(input())
number_list = []

for _ in range(N):
    x, y = map(int, input().split())
    number_list.append((x,y))

number_list.sort(key = lambda x: (x[0], x[1]))

for number in number_list:
    print(*number)