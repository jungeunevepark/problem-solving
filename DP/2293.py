n, k = map(int, input().split())
array = list(int(input()) for _ in range(n))
d = [0] * (k+1)  # 가치가 k일 때 가능한 경우의 수
d[min(array)] = 1
for i in range(min(array) + 1, k+1):
    for j in array:
        if i > j:
            d[i] += d[i-j]
