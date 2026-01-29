n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
checklist = list(map(int, input().split()))

def find(a):
    high, low, cnt = n, 0, 0

    while cnt < 20:
        cnt += 1
        mid = (high + low) // 2
        if arr[mid] == a:
            return 1
        elif arr[mid] > a:
            high = mid
        else:
            low = mid
    return 0

answer = []
for c in checklist:
    answer.append(find(c))

print(*answer)