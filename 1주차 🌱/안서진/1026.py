# 보물 (실4)
N = int(input())

numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))

numbers1.sort()
numbers2.sort()

ans = 0
for i in range(N):
  ans += numbers1[i] * numbers2[N-i-1]

print(ans)