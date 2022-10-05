d = [[0] * 15 for _ in range(15)]
d[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for i in range(0, 14):           # 층
    for j in range(1, 15):       # 호
        for k in range(j, 15):
            d[i+1][k] += d[i][j]

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(d[k][n])
