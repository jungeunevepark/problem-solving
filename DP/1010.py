d = [[0]*30 for _ in range(30)]

for i in range(30):
    for j in range(i, 30):
        if i == j:
            d[i][j] = 1
        else:
            d[i][j] = int(d[i][j-1] * j / (j - i))

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(d[N][M])
