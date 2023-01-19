import sys
sys.stdin = open("../basic_part1/input.txt", "r")
N = int(input())
step = [0] + [int(input()) for _ in range(N)]

d = [[0] * 2 for _ in range(N+1)]
d[1] = [step[1], 0]

for i in range(2, N+1):
    d[i][0] = max(d[i-2][0], d[i-2][1]) + step[i]   # 바로 전 계단을 안 밟는 경우
    d[i][1] = d[i-1][0] + step[i]     # 밟는 경우
print(max(d[N][0], d[N][1]))
