from collections import deque
import sys
sys.stdin = open("input.txt", "r")
array = [list(input()) for _ in range(12)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bomb(array):
    flag = 0
    q = deque(())
    for i in range(12):
        for j in range(6):
            if array[i][j] == '.':
                continue
            visited = [[False] * 6 for _ in range(12)]
            q.append((i, j))
            stack = [(i, j)]      # 제거할 칸 위치 저장
            count = 1             # 4칸 이상인지 카운트
            color = array[i][j]   # 색
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
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
    else:
        count += 1
    for j in range(6):
        queue = deque()
        for i in range(11, -1, -1):
            if array[i][j] != '.':
                queue.append(array[i][j])
        for k in range(11, -1, -1):
            if queue:
                array[k][j] = queue.popleft()
            else:
                array[k][j] = '.'
print(count)
