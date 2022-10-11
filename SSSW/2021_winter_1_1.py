from collections import deque
N, M, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice_number = [3, 5, 4, 2, 1]
dice = [0, 0, 0, 6]
def find_move_number(x, y, number):
    q = deque([(x, y)])
    result = 1
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    while q:
        i, j = q.popleft()
        for ni, nj in [(i-1, j), (i+1,j), (i, j+1), (i, j-1)]:
            if 0<= ni < N and 0<= nj < M and maze[ni][nj] == number and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
                result += 1

    return result

def move_dice(dice):
    """ dice를 정해진 방향으로 이동시킴, 칸의 숫자와 비교하여 이동방향 갱신, 점수 계산"""
    """ dice 이동 """
    dicex, dicey, dic, base = dice
    movex, movey = dicex+dx[dic], dicey+dy[dic]
    if 0 > movex or 0> movey or movey >= M or movex >= N:
        dic = dic + 2
        if dic > 3:
            dic -= 4
        movex, movey = dicex + dx[dic], dicey + dy[dic]
    dice[0], dice[1] = movex, movey
    dnumber = dice_number[dic]
    dice[3] = dnumber
    if dic == 0:
        dice_number[0], dice_number[1], dice_number[2], dice_number[3], dice_number[4] = dice_number[4], \
                                                                                             dice_number[1], \
                                                                                             base, \
                                                                                             dice_number[3], \
                                                                                             dice_number[2]
    elif dic == 1:
        dice_number[0], dice_number[1], dice_number[2], dice_number[3], dice_number[4] = dice_number[0], \
                                                                                             dice_number[4], \
                                                                                             dice_number[2], \
                                                                                             base, \
                                                                                             dice_number[3]
    elif dic == 2:
        dice_number[0], dice_number[1], dice_number[2], dice_number[3], dice_number[4] = base, \
                                                                                             dice_number[1], \
                                                                                             dice_number[4], \
                                                                                             dice_number[3], \
                                                                                             dice_number[0]
    elif dic == 3:
        dice_number[0], dice_number[1], dice_number[2], dice_number[3], dice_number[4] = dice_number[0], \
                                                                                             base, \
                                                                                             dice_number[2], \
                                                                                             dice_number[4], \
                                                                                             dice_number[1]
    """ 점수 계산 """
    score = maze[movex][movey] * find_move_number(movex, movey, maze[movex][movey])
    """ 다음 방향 결정 """
    if maze[movex][movey] < dnumber:
        dic += 1
    elif maze[movex][movey] > dnumber:
        dic -= 1
    if dic > 3:
        dic -= 4
    elif dic < 0:
        dic += 4
    dice[2] = dic
    return dice, score

score = 0
for round in range(K):
    dice, new = move_dice(dice)
    score += new
print(score)