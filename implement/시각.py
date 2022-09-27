from itertools import product
from re import L

N = int(input())
hour = [i for i in range((N % 10) + 1)]

if N < 10:
    a = list(i for i in product([0], hour,
                                [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
elif N < 20:
    a = list(i for i in product([0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    b = list(i for i in product([1], hour,
                                [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    a = a + b
else:
    a = list(i for i in product([0, 1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    b = list(i for i in product([2], hour,
                                [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    a = a + b


count = 0
for item in a:
    if 3 in item:
        count += 1
print(count)

"""가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인"""

count = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)
