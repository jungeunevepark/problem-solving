import sys
sys.stdin = open("input.txt", "r")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# def square(stack):
#     minw, minh = 1e9, 1e9
#     maxw, maxh = -1e9, -1e9
#     for x, y in stack:
#         minw = min(x, minw)
#         maxw = max(x, maxw)
#         minh = min(y, minh)
#         maxh = max(y, maxh)
#     return (maxw-minw) * (maxh-minh)


for _ in range(int(input())):
    x, y, k = 0, 0, 0
    minw, minh = 0, 0
    maxw, maxh = 0, 0
    for s in list(input()):
        if s == 'F':
            x = x + dx[k]
            y = y + dy[k]
            minw = min(x, minw)
            maxw = max(x, maxw)
            minh = min(y, minh)
            maxh = max(y, maxh)
        elif s == 'B':
            x = x - dx[k]
            y = y - dy[k]
            minw = min(x, minw)
            maxw = max(x, maxw)
            minh = min(y, minh)
            maxh = max(y, maxh)
        elif s == 'L':
            if k == 0:
                k = 3
            else:
                k -= 1
        else:
            if k == 3:
                k = 0
            else:
                k += 1
    print((maxw-minw) * (maxh-minh))
