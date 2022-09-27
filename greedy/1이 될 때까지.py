a, b = map(int, input().split())
n, k = a, b
count = 0

# O(n)
while a > 1:
    if a % b == 0:
        a = a / b
        count += 1
    else:
        a -= 1
        count += 1

# O(logn)
result = 0
while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)

print(count)
print(result)

"""최대한 많이 나누기를 수행하면 됨
N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1을 빼는 작업보다
수를 훨씬 많이 줄일 수 있음"""
