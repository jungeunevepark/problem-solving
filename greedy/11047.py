import sys
sys.stdin = open("../implement/input.txt", "r")
# input = sys.stdin.readline

N, K = map(int, input().split())
A = list(int(input()) for _ in range(N))
A.reverse()
count = 0
for a in A:
    if a > K:
        continue
    count += K // a
    K = K % a
print(count)