import sys
sys.stdin = open("input.txt", "r")
array = list(int(input()) for _ in range(9))
want = sum(array) - 100
stack = []

for i in range(len(array)):
    for j in range(len(array)):
        if i == j:
            continue
        if (j, i) in stack:
            continue
        if array[i] + array[j] == want:
            x, y = i, j
            break


answer = []
for i in array:
    if i == array[x] or i == array[y]:
        continue
    answer.append(i)
answer.sort()
for i in range(len(answer)):
    if i == len(answer) - 1:
        print(answer[i], end="")
    else:
        print(answer[i])
