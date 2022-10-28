import sys
input = sys.stdin.readline
N, M = map(int, input().split())

Ddogam = {}
Ndogam = {}
for i in range(N):
    a = input()
    Ddogam[a] = i+1
    Ndogam[i+1] = a
for _ in range(M):
    k = input()
    if k.isdigit():
        print(Ndogam[int(k)])
    else:
        print(Ddogam[k])