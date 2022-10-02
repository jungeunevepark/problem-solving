from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
result = list(map(int, input().split()))
option = [0] * result[0] + [1] * result[1] + [2] * result[2] + [3] * result[3]
a = list(permutations(option, len(option)))
maximum = -1e9
minimum = 1e9

for ele in a:
    result = num[0]
    for i in range(len(option)):
        if ele[i] == 0:
            result += num[i+1]
        elif ele[i] == 1:
            result -= num[i+1]
        elif ele[i] == 2:
            result *= num[i+1]
        else:
            if result < 0:
                result = (-1)*((-1) * result // num[i+1])
            else:
                result //= num[i+1]
    maximum = max(maximum, result)
    minimum = min(minimum, result)
print(maximum)
print(minimum)
