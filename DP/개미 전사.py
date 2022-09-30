N = int(input())
array1 = list(map(int, input().split()))
array = array1[:]
count = 0

while True:
    maximum = max(array)
    start = array.index(maximum)
    count += maximum
    if start <= 1 and start >= len(array) - 1:
        break
    elif start <= 1:
        array = array[start+2:]
    elif start >= len(array) - 1:
        array = array[:start-1]
    else:
        array = array[:start-1]+array[start+2:]
print(count)

"""점화식을 작성한다고 생각하기(점점 i의 값이 커지게 설계)"""
array = array1[:]
d = [0] * N
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + array[i])
print(d[N-1])
