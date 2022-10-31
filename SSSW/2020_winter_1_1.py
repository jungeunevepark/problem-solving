import sys
sys.stdin = open("../implement/input.txt", "r")
from collections import deque

N, K = map(int, input().split())
d = list(map(int, input().split()))

robots = []
start, end = 0, N-1
count = 0
number = 0
while True:
    count += 1
    start -= 1
    end -= 1
    if start < 0:
        start += 2*N
    if end < 0:
        end += 2*N
    q = deque(robots[:])
    robots = []
    while q:
        j = q.popleft()
        next = j+1
        if next >= 2*N:
            next -= 2*N
        if j == end :
            continue
        elif next not in robots and d[next] >= 1:
            d[next] -= 1
            if d[next] == 0:
                number += 1
            if not next == end:
                robots.append(next)
        else:
            robots.append(j)
    if d[start] > 0:
        robots.append(start)
        d[start] -= 1
        if d[start] == 0:
            number += 1
    if number >= K:
        break
print(count)

