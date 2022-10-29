import sys
sys.stdin = open("../greedy/input.txt", "r")
n, m, k, c = map(int, input().split())
treemap = [list(map(int, input().split())) for _ in range(n)]
danger = [[0]*n for _ in range(n)] # 제초제 남은 년 수
dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]

def growtree(treemap, time):
    newtree = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if treemap[i][j] > 0:
                maketree, count = 0, 0
                for ni, nj in [(i+1, j), (i, j+1), (i-1,j), (i, j-1)]:
                    if 0 <= ni < n and 0 <= nj < n and treemap[ni][nj] >= 0:
                        if treemap[ni][nj] == 0 and not danger[ni][nj] >= time:
                            maketree += 1
                        elif treemap[ni][nj] > 0:
                            count += 1
                treemap[i][j] += count
                for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if (0 <= ni < n and 0 <= nj < n) and treemap[ni][nj] == 0 and not danger[ni][nj] >= time:
                        newtree[ni][nj] += treemap[i][j] // maketree
    for i in range(n):
        for j in range(n):
            treemap[i][j] += newtree[i][j]

    return treemap
def print_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end = " ")
        print()
def dietree(treemap, danger, time):
    maxdie = 0
    diex, diey = 0, 0
    for i in range(n):
        for j in range(n):
            nowdie = 0
            if treemap[i][j] > 0:
                nowdie += treemap[i][j]
                for u in range(4):
                    for d in range(1, k+1):
                        ni = i + d * dx[u]
                        nj = j + d * dy[u]
                        if 0> ni or ni >= n or 0> nj or nj >= n or treemap[ni][nj] <= 0:
                            break
                        nowdie += treemap[ni][nj]
            if nowdie > maxdie:
                maxdie = nowdie
                diex, diey = i, j
    danger[diex][diey] = c + time
    treemap[diex][diey] = 0
    for u in range(4):
        for d in range(1, k + 1):
            ni = diex + d * dx[u]
            nj = diey + d * dy[u]
            if 0 > ni or ni >= n or 0 > nj or nj >= n or treemap[ni][nj] < 0:
                break
            if treemap[ni][nj] == 0:
                danger[ni][nj] = c + time
                break
            danger[ni][nj] = c + time
            treemap[ni][nj] = 0
    return treemap, danger, maxdie

answer = 0
for time in range(1, m+1):
    treemap = growtree(treemap, time)
    treemap, danger, nowdie = dietree(treemap, danger, time)
    answer += nowdie
print(answer)