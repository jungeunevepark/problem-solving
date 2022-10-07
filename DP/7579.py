import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
app = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
d = [[0]*(sum(cost)+1) for _ in range(N+1)]
result = sum(cost)

for i in range(1, N+1):
    for j in range(1, sum(cost)+1):
        if j >= cost[i]:
            d[i][j] = max(d[i-1][j], d[i-1][j-cost[i]]+app[i])
        else:
            d[i][j] = d[i-1][j]
        if d[i][j] >= M:
            result = min(result, j)
if M != 0:
    print(result)
else:
    print(0)
