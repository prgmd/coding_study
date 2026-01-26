# 회의실 배정 (골5)

arr = []
N = int(input())

# 모든 회의실에 대해서 [시작 시간, 종료 시간] 입력받기 
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x,y])

sorted_arr = sorted(arr, key = lambda x: x[1])

cnt = 1
now_x, now_y = sorted_arr[0]


for i in range(1,N):
    new_x, new_y = sorted_arr[i]
    if new_x >= now_y:
        cnt+=1
        now_x, now_y = new_x, new_y

print(cnt)



# cnt = 1
# now_x, now_y = sorted_arr.pop(0)

# while sorted_arr :
#     new_x, new_y = sorted_arr.pop(0)
#     if new_x >= now_y : 
#         cnt += 1
#         now_x, now_y = new_x, new_y
