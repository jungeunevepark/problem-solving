import sys
sys.stdin = open("../implement/input.txt", "r")
n, m, h, k = map(int, input().split())
run = []
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

maze = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y, d = map(int, input().split())
    run.append([x-1, y-1, d+1])
for _ in range(h):
    x, y = map(int, input().split())
    maze[x-1][y-1] = 't'

x, y = n // 2, n // 2 # 술래의 위치
idx, v = 1, 0 # 술래의 방향
visited = [[False] * n for _ in range(n)]
visited[x][y] = True
visited[x -1][y] = True
score = 0

for round in range(k):
    """ 도망자 방향 조절 """
    for k in range(len(run)):
        i, j, d = run[k]
        if abs(x-i) + abs(y-j) <= 3:
            ni = i + dx[d]
            nj = j + dy[d]
            if 0<= ni < n and 0<= nj < n:
                if ni != x or nj != y: # 이동
                    run[k] = [ni, nj, d]
            else:
                if d > 0 :
                    d -= 2
                else:
                    d += 2
                ni = i + dx[d]
                nj = j + dy[d]
                if ni != x or nj != y: # 이동
                    run[k] = [ni, nj, d]

    """ 술래 방향 조절 """
    if v == 0: # 안쪽에서 나오는 경우
        x = x + dx[idx]
        y = y + dy[idx]
        nx = x + dx[idx + 1]
        ny = y + dy[idx + 1]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            idx += 1
        else:
            visited[x+dx[idx]][y+dy[idx]] = True
        if x == 0 and y == 0:
            v = 1
            idx = 3
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            visited[1][0] = True
    else: # 안쪽으로 들어가는 경우
        x = x + dx[idx]
        y = y + dy[idx]
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
        else:
            idx -= 1
            visited[x + dx[idx]][y + dy[idx]] = True
        if x == n // 2 and y == n // 2:
            v = 0
            idx = 1
            visited = [[False] * n for _ in range(n)]
            visited[n // 2][n // 2] = True
            visited[n // 2 -1][n//2] = True
    """ 술래가 도망자를 잡는다. """
    move = []
    for u in range(3):
        findx = x + u * dx[idx]
        findy = y + u * dy[idx]
        if 0<= findx < n and 0<= findy < n and not maze[findx][findy] == 't':
            for runx, runy, rund in run:
                if runx == findx and runy == findy:
                    move.append([runx, runy, rund])
                    score += (round+1)
    for runx, runy, rund in move:
        run.remove([runx, runy, rund])
    if v == 0 and idx == 3:
        idx = -1
    elif v == 1 and idx == -1:
        idx = 3
print(score)
