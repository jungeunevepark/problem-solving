import sys

sys.stdin = open("input.txt", "r")

T = int(input())
graph = [[] for _ in range(T + 1)]

for i in range(T - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b)
    graph[b - 1].append(a)


def dfs(n):
    for k in graph[n]:
        if visited[k] == False:
            visited[k] = n
            dfs(k)


visited = [False] * (T + 1)
visited[1] = 1
dfs(1)

print(graph)
print(visited)
for i in range(2, T + 1):
    print(visited[i])
