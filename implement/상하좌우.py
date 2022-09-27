N = int(input())
loute = list(input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
x = y = 1

for i in loute:
    if i == 'R':
        nx = x + dx[1]
        ny = y + dy[1]
    elif i == 'U':
        nx = x + dx[3]
        ny = y + dy[3]
    elif i == 'D':
        nx = x + dx[2]
        ny = y + dy[2]
    else:
        nx = x + dx[0]
        ny = y + dy[0]

    if 0 < nx <= N and 0 < ny <= N:
        x = nx
        y = ny

print(y, x)
