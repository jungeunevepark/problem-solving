N, M = map(int, input().split())


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


if N > M:
    G = gcd(N, M)
else:
    G = gcd(M, N)

L = int((N / G) * M)
print(G)
print(L)
