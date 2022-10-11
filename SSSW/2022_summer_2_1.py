from collections import deque
import sys
sys.stdin = open("input.txt", "r")

n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
team_line = [[] for _ in range(m)]
head_tail = [[] for _ in range(m)]
direction = [1] * m

def find_team_line(count, x, y):
    visited = [[False] * n for _ in range(n)]
    q = deque([(x, y)])
    team_line[count].append((x, y))
    head_tail[count].append(x)
    head_tail[count].append(y)
    visited[x][y] = True
    while q:
        i, j = q.popleft()
        for ni, nj in [(i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1)]:
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] == 4 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
                team_line[count].append((ni, nj))
                break
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for ni, nj in [(i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1)]:
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] == 3 and not visited[ni][nj]:
                head_tail[count].append(ni)
                head_tail[count].append(nj)
                visited[ni][nj] = True
                team_line[count].append((ni, nj))
                i, j = ni, nj
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < n and 0 <= nj < n and 0< maze[ni][nj] <= 2 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
                team_line[count].append((ni, nj))
                break
    if len(head_tail[count]) == 2:
        head_tail[count].append(head_tail[count][0])
        head_tail[count].append(head_tail[count][1])
        print(head_tail)

def move_team(maze, head_tail, direction):
    """팀의 head, tail 바꿔주기, maze 값 바꿔주기"""
    for i in range(len(head_tail)):
        headx, heady, tailx, taily = head_tail[i]
        head = team_line[i].index((headx, heady))
        tail = team_line[i].index((tailx, taily))
        if direction[i] == 1:
            if head == len(team_line[i]) - 1:
                head = -1
            if tail == len(team_line[i]) - 1:
                tail = -1
        else:
            if head == 0:
                head = len(team_line[i])
            if tail == 0:
                tail = len(team_line[i])
        head_tail[i] = [team_line[i][head+direction[i]][0], team_line[i][head+direction[i]][1], team_line[i][tail+direction[i]][0],  team_line[i][tail+direction[i]][1]]

    for i in range(m):
        headx, heady, tailx, taily = head_tail[i]
        head = team_line[i].index((headx, heady))
        tail = team_line[i].index((tailx, taily))
        if (direction[i] == 1 and head < tail) or (direction[i] == -1 and head > tail):
            if direction[i] == 1:
                people = team_line[i][:head] + team_line[i][tail:]
                line = team_line[i][head:tail]
            else:
                people = team_line[i][:head] + team_line[i][tail:]
                line = team_line[i][tail:head]

            for i, j in people:
                maze[i][j] = 2
            for i, j in line:
                maze[i][j] = 4
        else:
            if direction[i] == -1:
                people = team_line[i][head:tail]
                line = team_line[i][:head] + team_line[i][tail:]
            else:
                people = team_line[i][tail:head]
                line = team_line[i][head:] + team_line[i][:tail]
            for i, j in people:
                maze[i][j] = 2
            for i, j in line:
                maze[i][j] = 4
        maze[headx][heady] = 1
        maze[tailx][taily] = 3
    return maze, head_tail

""" 팀의 진행 라인, 팀의 머리 꼬리 저장"""
count = 0
for i in range(n):
    for j in range(n):
        if maze[i][j] == 1:
            find_team_line(count, i, j)  # (i,j)를 머리사람으로 두고 있는 곳의 이동 라인
            count += 1

def print_maze():
    for i in range(n):
        for j in range(n):
            print(maze[i][j], end = " ")
        print()
    print()
"""라운드 진행"""
answer = 0
ball = 0
for round in range(k):
    move_team(maze, head_tail, direction)
    dic = (round-ball) // n
    line = (round-ball) % n
    findx, findy = -1, -1
    if dic == 0:
        for j in range(n):
            if 0 < maze[line][j] < 4:
                findx, findy = line, j
                break
    elif dic == 1:
        for i in range(n-1, -1, -1):
            if 0< maze[i][line] < 4:
                findx, findy = i, line
                break
    elif dic == 2:
        for j in range(n-1, -1, -1):
            if 0< maze[n-1-line][j] < 4:
                findx, findy = n-1-line, j
                break
    elif dic == 3:
        for i in range(n):
            if 0< maze[i][n-line-1] < 4:
                findx, findy = i, n-line-1
                break
    if dic == 3 and line == n-1 :
        ball += 4*(n)
    for team_number in range(m):
        if (findx, findy) in team_line[team_number]:
            headx, heady, tailx,taily = head_tail[team_number]
            head = team_line[team_number].index((headx, heady))
            tail = team_line[team_number].index((tailx, taily))
            catch = team_line[team_number].index((findx, findy))
            head_tail[team_number] = [tailx, taily, headx, heady]
            if head > catch and direction[team_number] == 1:
                direction[team_number] = -1
                answer += (head-catch+1) ** 2
            elif head < catch and direction[team_number] == 1:
                direction[team_number] = -1
                answer += (len(team_line[team_number]) - catch + head + 1) ** 2
            elif head > catch and direction[team_number] == -1:
                direction[team_number] = 1
                answer += (len(team_line[team_number]) - head + catch + 1) ** 2
            elif head < catch and direction[team_number] == -1:
                answer += (catch - head + 1) ** 2
                direction[team_number] = 1
            else:
                direction[team_number] = -1 * direction[team_number]
                answer += 1
print(answer)