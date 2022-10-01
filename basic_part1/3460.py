def fine_two(x):
    result = ""
    while x > 0:
        result += str(x % 2)
        x = x // 2
    return result


for _ in range(int(input())):
    array = list(fine_two(int(input())))
    for i in range(len(array)):
        if array[i] == '1':
            print(i, end=" ")
    print()
