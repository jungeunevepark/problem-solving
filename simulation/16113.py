import sys
sys.stdin = open("input.txt", "r")
N = int(input())
array = list(input())
maximum = N // 5

one = array[:maximum]
two = array[maximum: 2*maximum]
three = array[2*maximum: 3*maximum]
four = array[3*maximum: 4*maximum]
five = array[4*maximum: 5*maximum]
flag = 0
result = []

for i in range(maximum):
    if [one[i], two[i], three[i], four[i], five[i]] == ['.', '.', '.', '.', '.']:
        flag = 0
        continue
    if flag == 1:
        continue
    if result == [6, 8]:
        if [one[i], two[i], three[i], four[i], five[i]] == ['#', '.', '#', '.', '#']:
            continue
        elif [one[i], two[i], three[i], four[i], five[i]] == ['#', '#', '#', '#', '#']:
            print(8, end="")
        else:
            print(6, end="")
        result = []
    else:
        if [one[i], two[i], three[i], four[i], five[i]] == ['#', '.', '#', '#', '#']:
            print(2, end="")
            flag = 1
        if [one[i], two[i], three[i], four[i], five[i]] == ['#', '.', '#', '.', '#']:
            print(3, end="")
            flag = 1
        if [one[i], two[i], three[i], four[i], five[i]] == ['#', '#', '#', '.', '.']:
            print(4, end="")
            flag = 1
        if [one[i], two[i], three[i], four[i], five[i]] == ['#', '.', '.', '.', '.']:
            print(7, end="")
            flag = 1
        if [one[i], two[i], three[i], four[i], five[i]] == ['#', '#', '#', '.', '#']:
            if [one[i+2], two[i+2], three[i+2], four[i+2], five[i+2]] == ['#', '#', '#', '#', '#']:
                print(9, end="")
            else:
                print(5, end="")
            flag = 1
        if [one[i], two[i], three[i], four[i], five[i]] == ['#', '#', '#', '#', '#']:
            if i == maximum - 1 or [one[i+1], two[i+1], three[i+1], four[i+1], five[i+1]] == ['.', '.', '.', '.', '.']:
                print(1, end="")
                flag = 1
            elif [one[i+1], two[i+1], three[i+1], four[i+1], five[i+1]] == ['#', '.', '.', '.', '#']:
                print(0, end="")
                flag = 1
            else:
                result = [6, 8]
