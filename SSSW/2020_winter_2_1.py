"""
NxN 격자 (r행, c열) A[r][c]는 (r,c)에 있는 모래의 양
"""
import sys
sys.stdin = open("../greedy/input.txt", "r")
# from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
x, y = N//2, N//2
d = 0
line = [(N//2, N//2)]
visited[N//2][N//2] = True

while not (x == 0 and y == 0):
    x = x + dx[d]
    y = y + dy[d]
    visited[x][y] = True
    line.append((x, y))
    if 0<= x+dx[d+1] < N and 0<= y+dy[d+1] < N and not visited[x+dx[d+1]][y+dy[d+1]]:
        d += 1
    if d == 3:
        d -= 4

vx = [1, -1, 1, -1, -1, 1, -2, 2, 0]
vy = [0, 0, -1, -1, 1, 1, 0, 0, -2]
out = 0
for idx, (x, y) in enumerate(line):
    nowx = vx[:]
    nowy = vy[:]
    max = maze[x][y]
    remainx = x
    remainy = y-1
    if max == 0:
        continue
    if y-line[idx-1][1] == 1:
        nowy = list(map(lambda x: -x, nowy))
        remainy = y+1
    elif x-line[idx-1][0] == -1:
        nowx = vy[:]
        nowy = vx[:]
        remainx = x-1
        remainy = y
    elif x-line[idx-1][0] == 1:
        nowx = list(map(lambda x: -x, nowy))
        nowy = vx[:]
        remainx = x+1
        remainy = y

    for k in range(9):
        nx = x + nowx[k]
        ny = y + nowy[k]
        if k < 2 :
            remain = int(maze[x][y] * (0.07))
        elif k < 4:
            remain = int(maze[x][y] * (0.1))
        elif k < 6:
            remain = int(maze[x][y] * (0.01))
        elif k < 8:
            remain = int(maze[x][y] * (0.02))
        else:
            remain = int(maze[x][y] * (0.05))
        max -= remain
        if 0<= nx < N and 0<= ny < N :
            maze[nx][ny] += remain
        else:
            out += remain
    if 0<= remainx < N and 0<= remainy < N:
        maze[remainx][remainy] += max
    else:
        out += max
    maze[x][y] = 0
print(out)