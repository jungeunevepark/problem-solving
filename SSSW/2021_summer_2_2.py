"""
NxN인 격자, (r행, c열)
"""
import sys
sys.stdin = open("../greedy/input.txt", "r")
from collections import deque

N, M = map(int, input().split())
circle_map = [list(map(int, input().split())) for _ in range(N)]
round = []
for _ in range(M):
    d, s = map(int, input().split())
    round.append((d, s))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

vx = [0, 1, 0, -1]
vy = [-1, 0, 1, 0]
d = 0

i, j = N//2, N//2
line = [(N//2, N//2)]
visited = [[False]*N for _ in range(N)]
visited[N//2][N//2] = True

while not (i == 0 and j == 0) :
    i = i+vx[d]
    j = j+vy[d]
    visited[i][j] = True
    line.append((i, j))
    if 0<= i+vx[d+1] < N and 0<= j+vy[d+1] < N and not visited[i+vx[d+1]][j+vy[d+1]]:
        d += 1
    if d >=3:
        d -= 4


def move_circle(circle_map, idx):
    """
    구슬이 폭발했을 때 빈 공간에 구슬을 옮겨준다.
    :param circle_map: NxN 격자
    :param idx: 폭발이 있는 곳중 가장 상어에 가까운 곳의 line index
    :return: NxN격자
    """
    q = deque([])
    for x, y in line[idx:]:
        if circle_map[x][y] != 0:
            q.append(circle_map[x][y])
            circle_map[x][y] = 0

    for x, y in line[idx:]:
        try:
            circle_map[x][y] = q.popleft()
        except:
            circle_map[x][y] = 0

    return circle_map

def bomb_circle(circle_map):
    score = 0
    while True:
        count = 0
        number = 0
        flag = 0
        for idx, (x, y) in enumerate(line):
            if circle_map[x][y] != number:
                if count >= 4:
                    flag = 1
                    for x, y in line[idx-1:idx-count-1:-1]:
                        circle_map[x][y] = 0
                    score += number * count
                number = circle_map[x][y]
                count = 1
            else:
                count += 1
        if flag == 0:
            break

        circle_map = move_circle(circle_map, 1)

    return circle_map, score

def new_circle(circle_map):
    q = deque([])
    count = 1
    number = circle_map[line[1][0]][line[1][1]]
    for idx, (x, y) in enumerate(line[2:]):
        if circle_map[x][y] != number:
            q.append(count)
            q.append(number)
            number = circle_map[x][y]
            count = 1
        else:
            count += 1

    for x, y in line[1:]:
        try:
            circle_map[x][y] = q.popleft()
        except:
            circle_map[x][y] = 0
    return circle_map

answer = 0
for d, s in round:
    """구슬 파괴"""
    for u in range(1, s+1):
        nx = N//2+ u*dx[d]
        ny = N//2+ u*dy[d]
        circle_map[nx][ny] = 0
        if u == 1:
            idx = line.index((nx, ny))
    circle_map = move_circle(circle_map, idx)
    circle_map, score = bomb_circle(circle_map)
    circle_map = new_circle(circle_map)
    answer += score
print(answer)