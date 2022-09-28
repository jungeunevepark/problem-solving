from collections import deque
import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
m = max(N, M)
length = [[m]*M for _ in range(N)]
dx = [1, -1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
q = deque()


for i in range(N):
    for j in range(M):
        if map[i][j]:
            visited[i][j] = True
            length[i][j] = 1
            for k in range(0, 8):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or nj < 0 or ni >= N or nj >= M or visited[ni][nj]:
                    continue
                visited[ni][nj] = True
                q.append((ni, nj))


while q:
    x, y = q.popleft()
    for k in range(0, 8):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if map[nx][ny]:
            length[x][y] = 1
        length[x][y] = min(length[x][y], length[nx][ny] + 1)
        if not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))

results = 0
for i in range(0, N):
    for j in range(0, M):
        results = max(results, length[i][j])
print(results)
