import sys
input = sys.stdin.readline

n = int(input())
numbers = sorted(list(map(int, input().split())))

m = int(input())
checklist = list(map(int, input().split()))

def find_number(c):
    high = n
    low = 0
    cnt = 0

    while cnt < 18:
        mid = (high + low)//2
        cnt += 1
        if numbers[mid] == c:
            return 1
        elif numbers[mid] > c:
            high = mid
        else:
            low = mid
    return 0

for c in checklist:
    print(find_number(c))