from collections import deque
import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
know = 'acint'
unknown = 'abcdefghijklmnopqrstuvwxyz'
strings = [input() for _ in range(N)]


def is_ok(list):
    count = 0
    for string in strings:
        flag = 0
        for s in string:
            if s not in list:
                flag = 1
                # break
        if flag == 0:
            count += 1
    return count


K = K-5
q = deque()
visited = []
if K > 0:
    q.append((know, K))
maximum = 0

while q:
    result, k = q.popleft()
    if k == 0:
        maximum = max(maximum, is_ok(result))
    else:
        for i in unknown:
            if i not in result:
                visited.append(result+i)
                q.append((result+i, k-1))
print(maximum)
