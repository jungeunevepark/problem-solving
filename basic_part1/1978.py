def is_prime(x):
    if x == 1:
        return 0
    for i in range(2, x):
        if not visited[i]:
            if x % i == 0:
                return 0
            else:
                for j in range(i, x, i):
                    visited[j] = True
    return 1


count = 0
N = int(input())
array = list(map(int, input().split()))

for ele in array:
    visited = [False] * 1000
    count += is_prime(ele)
print(count)
