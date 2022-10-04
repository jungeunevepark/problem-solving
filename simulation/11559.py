from collections import deque
import sys
sys.stdin = open("input.txt", "r")
array = [list(input()) for _ in range(12)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bomb(array):
    visited = [[False] * 6 for _ in range(12)]
    flag = 0
    q = deque(())
    for i in range(11, -1, -1):
        for j in range(6):
            if array[i][j] == '.' or visited[i][j]:
                continue
            q.append((i, j))
            stack = [(i, j)]      # 제거할 칸 위치 저장
            count = 1             # 4칸 이상인지 카운트
            color = array[i][j]   # 색
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0 <= nx < 12 and 0 <= ny < 6 and array[nx][ny] == color and not visited[nx][ny]:
                        visited[nx][ny] = True
                        count += 1
                        stack.append((nx, ny))
                        q.append((nx, ny))
            if count >= 4:
                flag = 1
                for x, y in stack:
                    array[x][y] = '.'
    return array, flag


count = 0
while True:
    array, flag = bomb(array)
    if flag == 0:
        break
    count += flag
    for j in range(6):
        for i in range(11, -1, -1):
            if array[i][j] != '.':
                break
        if i == 11 or i == 0:
            continue
        for k in range(i+1):
            array[11 - k][j] = array[i - k][j]
        for u in range(11-i):
            array[u][j] = '.'
print(count)
