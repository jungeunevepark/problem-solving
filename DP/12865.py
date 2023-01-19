import sys
sys.stdin = open("../basic_part1/input.txt", "r")

N, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * (K+1) for _ in range(N)]

for i in range(N):
    for j in range(len(d[0])):
        if j >= array[i][0]:
            d[i][j] = max(d[i-1][j], d[i-1][j-array[i][0]]+array[i][1])
        else:
            d[i][j] = d[i-1][j]

print(d[N-1][K])
