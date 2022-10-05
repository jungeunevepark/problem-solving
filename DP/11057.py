N = int(input())
d = [[0] * 10 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(10):
        if i == 1:
            d[i][j] = 1
        else:
            d[i][j] = sum(d[i-1][:j+1])
print(sum(d[N]) % 10007)
