import sys
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
noheard = list(input() for _ in range(N))
nolook = list(input() for _ in range(M))
answer = []
count = 0
for h in noheard:
    if h in nolook:
        count+=1
        answer.append(h)
print(count)
print("\n".join(sorted(answer)))