from collections import deque
import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
map = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        (i, j) = q.popleft()
        for k in range(0, 4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            if map[ni][nj] == 1 and not(ni == 0 and nj == 0):
                map[ni][nj] = map[i][j] + 1
                q.append((ni, nj))

    return map[N-1][M-1]


print(bfs(0, 0))
