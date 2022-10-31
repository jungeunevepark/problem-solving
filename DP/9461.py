for _ in range(int(input())):
    n = int(input())
    d = [0, 1, 1, 1, 2, 2] + [0] * (n-4)
    for i in range(6, n+1):
        d[i] = d[i-1]
        if i >= 6:
            d[i] += d[i-5]
    print(d[n])