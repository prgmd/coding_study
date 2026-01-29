# 15649번 (N과 M(1)) - 백트래킹 

N, M = map(int,input().split())
visited = [False] * (N+1)
ans = []
# 1부터 number까지, 길이 length인 수열 찾기 
def add_num(number, length):
    if len(ans) == length:
        print(*ans)
        return 
    
    for i in range(1, number+1):
        if visited[i]:
            continue

        visited[i] = True
        ans.append(i)

        add_num(N, M)

        ans.pop()
        visited[i] = False

add_num(N, M)