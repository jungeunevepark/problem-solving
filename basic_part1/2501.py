N, K = map(int, input().split())
array = []
i, j = 0, 1
while i <= K and j <= N:
    if N % j == 0:
        array.append(j)
        i += 1
    j += 1

if len(array) < K:
    print(0)
else:
    print(array[K-1])
