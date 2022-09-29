from collections import deque, defaultdict
import sys
sys.stdin = open("input.txt", "r")
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M, K = map(int, input().split())
gym = [list(input()) for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())

already = [[0] * M for _ in range(N)]
q = deque()
q.append((x1, y1, 0))

while q:
    x, y, time = q.popleft()
    if (x, y) == (x2, y2):
        break
    for k in range(0, 4):
        nx = x + dx[k]
        ny = y + dy[k]
        i = 1
        while i <= K and 0 < nx <= N and 0 < ny <= M and not gym[nx-1][ny-1] == '#':
            if already[nx - 1][ny - 1] == 0 or already[nx-1][ny-1] > time + 1:
                already[nx-1][ny-1] = time + 1
                q.append((nx, ny, time+1))
            nx += dx[k]
            ny += dy[k]
            i += 1

if already[x2-1][y2-1] == 0:
    print(-1)
else:
    print(time)
