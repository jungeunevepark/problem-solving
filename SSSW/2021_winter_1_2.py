"""
RXC 크기를 가진 집에 온풍기를 설치
(r행, c열)
1. 집에 있는 모든 온풍기에서 바람이 한번 나옴
2. 온도가 조절됨
3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
4. 초콜릿 먹음
5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사.
    모든 칸의 온도가 K이상이면 테스트를 중단하고 아니면 1부터 다시 시작
"""
import sys
sys.stdin = open("../implement/input.txt", "r")
from collections import deque
R, C, K = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

warmers = []
finds = []
partitions = []
direction = [[], [(0, 1), (-1, 1), (1, 1)], [(0, -1), (1, -1), (-1, -1)], [(-1, 0), (-1, -1), (-1, 1)], [(1, 0), (1, -1), (1, 1)]]

for _ in range(int(input())):
    x, y, d = map(int, input().split())
    partitions.append((x-1, y-1, d))      # 0부터 시작하므로 1을 감소시킨다
# print(partitions)
for i in range(R):
    for j in range(C):
        if room[i][j] == 0:
            continue
        if room[i][j] == 5:
            finds.append((i, j))
        elif room[i][j] < 5:
            warmers.append((i,j,room[i][j]))
        room[i][j] = 0
def print_room(array):
    for i in range(R):
        for j in range(C):
            print(array[i][j], end = " ")
        print()
    print()

def warmer(room):
    # print(warmers)
    for x, y, d in warmers:
        visited = [[False] * C for _ in range(R)]
        visited[x + direction[d][0][0]][y+direction[d][0][1]] = True
        q = deque([(x + direction[d][0][0], y+direction[d][0][1], 5)])
        while q:
            i, j, count = q.popleft()
            room[i][j] += count
            if count == 1:
                continue
            for u in range(3):
                ni = i+direction[d][u][0]
                nj = j+direction[d][u][1]
                if 0<=ni<R and 0<=nj<C and not visited[ni][nj]:
                    if direction[d][u] == (0, 1):
                        if (i, j, 1) in partitions:
                            continue
                    elif direction[d][u] == (1, 0):
                        if (ni, nj, 0) in partitions:
                            continue
                    elif direction[d][u] == (1, 1):
                        if d == 1:
                            if (i+1, j, 0) in partitions or (i+1, j, 1) in partitions:
                                continue
                        else:
                            if (i, j, 1) in partitions or (i+1, j+1, 0) in partitions:
                                continue
                    elif direction[d][u] == (0, -1):
                        if (ni, nj, 1) in partitions:
                            continue
                    elif direction[d][u] == (-1, 0):
                        if (i, j, 0) in partitions:
                            continue
                    elif direction[d][u] == (-1, 1):
                        if d == 1:
                            if (i, j, 0) in partitions or (i-1, j, 1) in partitions:
                                continue
                        else:
                            if (i, j, 1) in partitions or (i, j+1, 0) in partitions:
                                continue
                    elif direction[d][u] == (-1, -1):
                        if d == 2:
                            if (i, j, 0) in partitions or (i-1, j-1, 1) in partitions:
                                continue
                        else:
                            if (i, j-1, 1) in partitions or (i, j-1, 0) in partitions:
                                continue
                    elif direction[d][u] == (1, -1):
                        if d == 2:
                            if (i+1, j, 0) in partitions or (i+1, j-1, 1) in partitions:
                                continue
                        else:
                            if (i, j-1, 1) in partitions or (i+1, j-1, 0) in partitions:
                                continue
                    visited[ni][nj] = True
                    q.append((ni, nj, count-1))
        # print_room()
    return room
def chemi(room):
    new = [[0]*C for _ in range(R)]
    d = 0
    for i in range(len(room)):
        for j in range(len(room[0])):
            if not j == len(room[0])-1 and (i, j, 1) not in partitions:
                ni, nj = i, j+1
                d = abs(room[i][j] - room[ni][nj]) // 4
                if room[i][j] > room[i][nj] :
                    new[i][j] += (-1) * d
                    new[i][nj] += d
                else:
                    new[i][j] += d
                    new[i][nj] += (-1) * d

            if not i == len(room) -1 and (i+1, j, 0) not in partitions:
                d = abs(room[i][j] - room[i+1][j]) // 4
                if d == 0:
                    continue
                if room[i][j] > room[i+1][j] :
                    new[i][j] += (-1) * d
                    new[i+1][j] += d
                else:
                    new[i][j] += d
                    new[i+1][j] += (-1) * d

    for i in range(R):
        for j in range(C):
            room[i][j] += new[i][j]

    return room

count = 0
while True:
    room = warmer(room)
    room = chemi(room)
    for i in range(R):
        if not room[i][0] == 0:
            room[i][0] -= 1
        if not room[i][C-1] == 0:
            room[i][C-1] -=1
    for j in range(1, C-1):
        if not room[0][j] == 0:
            room[0][j] -=1
        if not room[R-1][j] == 0:
            room[R-1][j] -= 1
    count += 1
    if count > 100:
        break
    if all(room[x][y] >= K for x, y in finds):
        break
print(count)