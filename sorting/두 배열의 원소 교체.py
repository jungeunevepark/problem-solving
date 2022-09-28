N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(K):
    min_index = max_index = 0
    for i in range(0, N):
        if A[min_index] > A[i]:
            min_index = i
    for i in range(0, N):
        if B[max_index] < B[i]:
            max_index = i
    A[min_index], B[max_index] = B[max_index], A[min_index]

result = 0
for x in A:
    result += x

print(result)

"""배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체
최악의 경우에도 O(NlogN)을 보장하는 정렬 알고리즘을 사용해야함"""

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

    else:
        break
