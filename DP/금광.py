import sys
sys.stdin = open("input.txt", "r")

for T in range(int(input())):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    d = []
    index = 0
    for i in range(N):
        d.append(array[index:index+M])
        index += M
    for j in range(1, M):
        for i in range(N):
            if i == 0:
                left_up = 0
            else:
                left_up = d[i-1][j-1]
            if i == N-1:
                left_down = 0
            else:
                left_down = d[i+1][j-1]
            left = d[i][j-1]
            d[i][j] = d[i][j] + max(left_up, left_down, left)
        result = 0
        for i in range(N):
            result = max(result, d[i][M-1])
    print(result)
