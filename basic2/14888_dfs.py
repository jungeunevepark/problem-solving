N = int(input())
num = list(map(int, input().split()))
result = list(map(int, input().split()))
option = [0] * result[0] + [1] * result[1] + [2] * result[2] + [3] * result[3]
maximum = -1e9
minimum = 1e9


def dfs(result, option, i):
    global minimum, maximum
    if option == []:  # 깊이 탐색 종료
        minimum = min(minimum, result)
        maximum = max(maximum, result)
    for j in range(len(option)):
        sum = result
        if option[j] == 0:
            sum += num[i]
        elif option[j] == 1:
            sum -= num[i]
        elif option[j] == 2:
            sum *= num[i]
        else:
            if sum < 0:
                sum = (-1)*((-1) * sum // num[i])
            else:
                sum //= num[i]
        dfs(sum, option[:j]+option[j+1:], i+1)


dfs(num[0], option, 1)
print(maximum)
print(minimum)
