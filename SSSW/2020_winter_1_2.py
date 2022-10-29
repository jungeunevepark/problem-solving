import sys
sys.stdin = open("../greedy/input.txt", "r")
N, M, K = map(int, input().split())
firemap = [[0]*N for _ in range(N)]
fireballs = {}
for i in range(N):
    for j in range(N):
        fireballs[(i, j)] = []
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    firemap[x-1][y-1] += 1
    fireballs[(x-1, j-1)].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move_fireballs(firemap, fireballs):
    plus = []
    for key, value in fireballs.items():
        for [m, s, d] in value:
            (x, y) = key
            nx = (x + s*dx[d])%N
            ny = (y + s*dy[d])%N
            if nx >= N :
                nx -= N
            elif nx < 0:
                nx += N
            if ny >= N:
                ny -= N
            elif ny < 0 :
                ny += N
            firemap[x][y] -= 1
            firemap[nx][ny] += 1
            fireballs[(x, y)].remove([m,s,d])
            plus.append([nx,ny,m,s,d])
    for i, j, m, s, d in plus:
        fireballs[(i, j)].append([m,s,d])
    return firemap
def crush_fireballs(firemap, fireballs):
    for i in range(N):
        for j in range(N):
            if len(fireballs[(i, j)]) > 1:
                M = 0
                S = 0
                D = 1
                flag = 0
                firecheck = fireballs[(i,j)][:]
                for x, y, m, s, d in firecheck:
                    if x == i and y == j:
                        fireballs[(i,j)].remove([x, y, m, s, d])
                        M += m
                        S += s
                        D *= d
                        if d % 2 == 1:
                            flag = 1
                M = M // 5
                S = S // len(firecheck)
                if not M == 0 :
                    firemap[i][j] = 4
                    if flag == 1 and D % 2 == 0:
                        base = 1
                    else:
                        base = 0
                    for u in range(base, 8, 2):
                        fireballs[(i,j)].append([M, S, u])
    return firemap, fireballs

for _ in range(K):
    firemap = move_fireballs(firemap, fireballs)
    firemap, fireballs = crush_fireballs(firemap, fireballs)
print(sum(x[0] for x in fireballs[(i, j)] for i in range(N) for j in range(N)))