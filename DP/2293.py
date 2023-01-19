import sys
sys.stdin = open("../basic_part1/input.txt", "r")

n, k = map(int, input().split())
array = list(int(input()) for _ in range(n))
d = [0] * (k+1)
d[0] = 1

for coin in array:
    for value in range(coin, k+1):
        d[value] += d[value-coin]
print(d[k])
