import sys
sys.stdin = open("input.txt", "r")

N = int(input())
array = list(map(int, input().split()))
d = [[0, 0] for _ in range(N)]

for idx in range(N):
    for j in range(0, idx):
        if array[j] < array[idx]:
            d[idx][0] = max(d[idx][0], d[j][0] + 1)
for idx in range(N-1, -1, -1):
    for j in range(N-1, idx, - 1):
        if array[j] < array[idx]:
            d[idx][1] = max(d[idx][1], d[j][1] + 1)

print(max(sum(d[i]) for i in range(N)) + 1)
