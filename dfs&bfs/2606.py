from collections import deque
import sys
sys.stdin = open("input.txt", "r")
num = int(input())
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * (num+1)


def bfs(v):
    q = deque([v])
    visited[v] = True
    count = 0                 # 1번을 통해!!
    while q:
        i = q.popleft()
        for x, y in graph:
            if x == i:
                if not visited[y]:
                    visited[y] = True
                    q.append(y)
                    count += 1
            elif y == i:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)
                    count += 1
    return count


print(bfs(1))
