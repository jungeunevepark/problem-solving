import sys
sys.stdin = open("../basic_part1/input.txt", "r")

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * N for _ in range(N)]

d[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        if i + array[i][j] < N:
            d[i + array[i][j]][j] += d[i][j]
        if j + array[i][j] < N:
            d[i][j + array[i][j]] += d[i][j]
print(d[N-1][N-1])
