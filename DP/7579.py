import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
app = list(map(int, input().split()))
cost = list(map(int, input().split()))
d = [[] for _ in range(N)]
result = 1e6


for idx, memory in enumerate(app):
    d[idx][0] = sum(d[idx-1])     # 전에 것과 더하는 경우

print(result)
