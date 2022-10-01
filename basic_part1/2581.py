N = int(input())
M = int(input())
visited = [False] * (M+1)
prime = []

for i in range(2, M+1):
    if not visited[i]:
        if N <= i:
            prime.append(i)
        for j in range(2*i, M+1, i):
            visited[j] = True

if prime == []:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
