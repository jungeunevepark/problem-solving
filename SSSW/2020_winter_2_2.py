import sys
sys.stdin = open("input.txt", "r")
from collections import deque

N, Q = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2**N)]
step = list(map(int, input().split()))

def circle(ice, L):
    """
    :param ice: array
    :param i: array 가장 첫번쨰 행의 숫자
    :param j: array 가장 첫번쨰 열의 숫자
    :param L: 격자의 크기
    :return: ice
    """
    new = [[0]*len(ice) for _ in range(len(ice))]
    for i in range(0, 2**N, L):
        for j in range(0, 2**N, L):
            for x in range(L):
                for y in range(L):
                    new[y+i][j+L-1-x] = ice[i+x][j+y]
    return new

def reduce_ice(ice):
    new_ice = [[0]*len(ice) for _ in range(len(ice))]
    for i in range(len(ice)):
        new_ice[i] = ice[i][:]

    for i in range(len(ice)):
        for j in range(len(ice)):
            if ice[i][j] == 0:
                continue
            count = 0
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<= ni< len(ice) and 0<= nj < len(ice) and ice[ni][nj] > 0:
                    count += 1
            if count < 3:
                new_ice[i][j] -= 1

    return new_ice

for L in step:
    ice = circle(ice, 2**L)
    ice = reduce_ice(ice)


def group(ice, visited, i, j):
    visited[i][j] = True
    count = 1
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0<= nx < 2**N and 0<= ny < 2**N and ice[nx][ny] > 0 and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return visited, count

visited = [[False] * len(ice) for _ in range(2**N)]
how = 0
result = 0
for i in range(2**N):
    for j in range(2**N):
        if ice[i][j] == 0:
            visited[i][j] = True
        how += ice[i][j]
        if not ice[i][j] == 0 and not visited[i][j]:
            vistied, count = group(ice, visited, i, j)
            if result < count :
                result = count
print(how)
print(result)