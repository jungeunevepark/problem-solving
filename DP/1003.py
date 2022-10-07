import sys
sys.stdin = open("input.txt", "r")
d = [[0] * 2 for _ in range(41)]

for x in range(41):
    if x == 0:
        d[x][0] = 1
    elif x == 1:
        d[x][1] = 1
    else:
        d[x] = [d[x-1][0] + d[x-2][0], d[x-1][1] + d[x-2][1]]
for _ in range(int(input())):
    print(*d[int(input())])
