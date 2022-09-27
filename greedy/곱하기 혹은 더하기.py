"Fail"
a = list(map(int, input()))

result = a[0]
for i in range(1, len(a)):
    if a <= 1 or result <= 1:     # 1도 더하는 것이 더 효율적!!!!
        result += a[i]
    else:
        result *= a[i]

print(result)

"""대부분 '+'보다는 'x'가 더 값을 크게 만듦
다만 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적
그러므로 두 수에 대해 하나라도 1이하인 경우에는 더하고 나머지는 곱함"""
