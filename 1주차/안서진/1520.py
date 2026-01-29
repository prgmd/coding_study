M, N = map(int, input().split())

arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(M)]

dx = [1, 0]   # 아래, 오른쪽
dy = [0, 1]

def dfs(x, y):
    visited[x][y] = True

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < M and 0 <= ny < N:
            if not visited[nx][ny] and arr[nx][ny] < arr[x][y]:
                dfs(nx, ny)

# 시작점이 길이면 탐색
if arr[0][0] == 1:
    dfs(0, 0)

# 방문 배열 출력(연습용)
for row in visited:
    print(*row)
