import sys
from collections import deque
sys.stdin = open("input.txt", "r")
N, M, K = map(int, input().split())

trash = [[0]*M for _ in range(N)]
trash_can = [list(map(int, input().split())) for _ in range(K)]
for x, y in trash_can:
    trash[x-1][y-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * M for _ in range(N)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 0
    while q:
        i, j = q.popleft()
        for k in range(0, 4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            if trash[ni][nj] == 1:
                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    count += 1
                    q.append((ni, nj))
    return count


result = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and trash[i][j] == 1:
            count = bfs(i, j)
            result = max(result, count)

print(result)
