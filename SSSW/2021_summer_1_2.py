from collections import deque
import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(N)]
group = []
def find_group(i, j, number, visited):
    new = [(i, j)]
    q = deque([])
    q.append((i, j))
    visited[i][j] = True
    rainbow = 0
    rainbows = []
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0<=nx<N and 0<=ny<N and (game[nx][ny] == number or game[nx][ny] == 0) and not visited[nx][ny]:
                if game[nx][ny] == 0:
                    rainbow += 1
                    rainbows.append((nx, ny))
                visited[nx][ny] = True
                q.append((nx, ny))
                new.append((nx, ny))

    for x, y in rainbows:
        visited[x][y] = False

    if len(new) >= 2:
        return visited, new, rainbow
    return visited, [], rainbow

def circle(game):
    new_game = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_game[N-1-j][i] = game[i][j]

    return new_game

def down(game):
    for j in range(N):
        stack = []
        for i in range(N):
            if game[i][j] == -1:
                for k in range(i-1, -1, -1):
                    try:
                        game[k][j] = stack.pop()
                    except:
                        break
            elif i == N-1:
                if not game[i][j] == None:
                    stack.append(game[i][j])
                    game[i][j] = None
                for k in range(i, -1, -1):
                    try:
                        game[k][j] = stack.pop()
                    except:
                        break
            elif not game[i][j] == None:
                stack.append(game[i][j])
                game[i][j] = None
    return game


answer = 0
while True:
    visited = [[False] * N for _ in range(N)]
    result_group = []
    result_count = 0
    result_rainbow = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and not game[i][j] == None and game[i][j] > 0:
                visited, group, rainbow = find_group(i, j, game[i][j], visited)
                if len(group) > result_count:
                    result_group = group
                    result_count = len(group)
                    result_rainbow = rainbow
                elif len(group) == result_count:
                    if rainbow < result_rainbow:
                        continue
                    result_group = group
                    result_rainbow = rainbow
    if result_count == 0:
        break
    for x, y in result_group:
        game[x][y] = None
    answer += result_count ** 2
    game = down(game)
    game = circle(game)
    game = down(game)
print(answer)