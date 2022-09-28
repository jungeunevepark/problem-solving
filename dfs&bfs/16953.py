from collections import deque
import sys
sys.stdin = open("input.txt", "r")
A, B = map(int, input().split())


def bfs(i):
    q = deque()
    q.append((i, 1))
    result = -1
    while q:
        k, count = q.popleft()
        print(k)
        if k == B:
            result = count
            break
        if 2*k <= B and not 2*k == 0:
            q.append((2*k, count + 1))
        if (k*10+1) <= B:
            q.append((k*10+1, count + 1))
    return result


print(bfs(A))
""" 연산법이 항상 커지는 쪽이기 때문에
A의 연산값이 B보다 커지면 
B로 갈수있는 방법이 없으므로 무시"""
