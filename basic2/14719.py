# 입력
H, W = map(int, input().split())
heights = list(map(int, input().split()))
map = [[0]*W for _ in range(H)]

# 블록 지도 표현
for i in range(len(heights)):
    for j in range(H-heights[i], H):
        map[j][i] = 1

# 총 빗물
total = 0
# 블럭 사이 빗물
rain = 0

for i in range(H-1, -1, -1):
    open = 0
    close = 0
    rain = 0
    for j in range(W):
        if map[i][j] == 1:
            if open == 1:
                close = 1
            else:
                open = 1
        else:
            if open == 1:
                rain += 1

        if (open, close) == (1, 1):
            total += rain
            rain = 0
            close = 0
print(total)
