from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]


def bfs(x, y, now):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    count = 1
    while q:
        (i, j) = q.popleft()
        for k in range(0, 4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 > ni or ni >= M or 0 > nj or nj >= N:
                continue
            if not visited[ni][nj] and graph[ni][nj] == now:
                visited[ni][nj] = True
                q.append((ni, nj))
                count += 1
    return count


dict = {'W': 0, 'B': 0}

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            now = graph[i][j]
            power = bfs(i, j, now)
            dict[now] += (power ** 2)
print(dict['W'], dict['B'])
