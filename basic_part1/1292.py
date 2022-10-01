N, M = map(int, input().split())
i, count = 1, 0
array = []
while count < M:
    count += i
    array += [i] * i
    i += 1

result = 0
for i in array[N-1:M]:
    result += i
print(result)
