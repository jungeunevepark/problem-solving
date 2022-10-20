import sys
sys.stdin = open("../implement/input.txt", "r")
from collections import deque
"""상어가 지나온 곳은 다시 지나갈 수 있음.. 이때 물고기를 다시 세지 않도록 주의"""

M, S = map(int, input().split())
smell = [[0]*5 for _ in range(5)]
maze = [[0] * 5 for _ in range(5)]  # input 그대로 받기!!!
fishes = [[[] for _ in range(5)] for _ in range(5)]
direction = [0, 1, 2, 3, 4, 5, 6, 7]

for _ in range(M):
    x, y, d = map(int, input().split())
    fishes[x][y].append(8 - d)
    maze[x][y] += 1
sharkx, sharky = map(int, input().split())

dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1] # 8가지 방향 : 왼, 왼위, 위, 오위, 오, 오아래, 아래, 왼아래

def copy():
    new_fishes = [[[] for _ in range(5)] for _ in range(5)]
    for i in range(1, 5):
        for j in range(1, 5):
            new_fishes[i][j] = fishes[i][j][:]
    new_maze = [[0] * 5 for _ in range(5)]
    for i in range(1, 5):
        new_maze[i] = maze[i][:]
    return new_fishes, new_maze

def fish_move(time, sharkx, sharky): # 현재 회차
    remove = []
    insert = [[[] for _ in range(5)] for _ in range(5)]
    for x in range(1, 5) :
        for y in range(1, 5):
            while fishes[x][y]:
                d = fishes[x][y].pop()
                for i in direction[d:] + direction[:d]:
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 1<= nx <= 4 and 1<= ny <= 4 and smell[nx][ny] < time and not (sharkx, sharky) == (nx, ny): # smell 수정 가능성 있
                        maze[x][y] -= 1
                        insert[nx][ny].append(i)
                        maze[nx][ny] += 1
                        break
                    elif i == d-1 or (d == 0 and i == 7):
                        insert[x][y].append(d)

    for i in range(1, 5):
        for j in range(1, 5):
            fishes[i][j] += insert[i][j]

    return fishes, maze

def shark_move(i, j, round):
    q = deque([(i, j, 0, 0, [])])
    result = 0
    result_step = []
    while q:
        x, y, diefish, time, step = q.popleft()
        if time == 3:
            if (result_step == [] and result == diefish) or (result < diefish) :
                result_step = step
                result = diefish
            continue
        for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
            if 1 <= nx <= 4 and 1 <= ny <= 4:
                if (nx, ny) in step:
                    q.append((nx, ny, diefish, time + 1, step + [(nx, ny)]))
                else:
                    q.append((nx, ny, diefish+maze[nx][ny], time+1, step + [(nx, ny)]))

    for stepx, stepy in result_step:
        if maze[stepx][stepy] > 0:
            maze[stepx][stepy] = 0
            smell[stepx][stepy] = round+2
            fishes[stepx][stepy] = []

    return maze, result_step[2][0], result_step[2][1]


for time in range(1, S+1):
    new_fishes, new_maze = copy()
    fishes, maze = fish_move(time, sharkx, sharky)
    maze, sharkx, sharky = shark_move(sharkx, sharky, time)
    for i in range(1, 5):
        for j in range(1, 5):
            fishes[i][j] += new_fishes[i][j]

    for i in range(1, 5):
        for j in range(1, 5):
            maze[i][j] += new_maze[i][j]

print(sum(maze[i][j] for i in range(1, 5) for j in range(1, 5)))