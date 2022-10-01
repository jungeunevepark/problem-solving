d = [0] * (21)
N = int(input())

for x in range(N+1):
    if x == 1 or x == 2:
        d[x] = 1
    else:
        d[x] = d[x-1] + d[x-2]


print(d[N])
