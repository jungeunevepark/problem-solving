import sys
sys.stdin = open("input.txt", "r")


def machine(string):
    array = string.split()
    if array[0] == 'ADD' or array[0] == 'ADDC':
        print('0000', end="")
        if len(array[0]) == 3:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'SUB' or array[0] == 'SUBC':
        print('0001', end="")
        if len(array[0]) == 3:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'MOV' or array[0] == 'MOVC':
        print('0010', end="")
        if len(array[0]) == 3:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        print('000', end="")
        print(last)
    elif array[0] == 'AND' or array[0] == 'ANDC':
        print('0011', end="")
        if len(array[0]) == 3:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'OR' or array[0] == 'ORC':
        print('0100', end="")
        if len(array[0]) == 2:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'NOT':
        print('010100', end="")
        two(array[1])
        print('000', end="")
        two(array[3])
        print('0')
    elif array[0] == 'MULT' or array[0] == 'MULTC':
        print('0110', end="")
        if len(array[0]) == 4:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'LSFTL' or array[0] == 'LSFTLC':
        print('0111', end="")
        if len(array[0]) == 5:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'LSFTR' or array[0] == 'LSFTRC':
        print('1000', end="")
        if len(array[0]) == 5:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'ASFTR' or array[0] == 'ASFTRC':
        print('1001', end="")
        if len(array[0]) == 5:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'RL' or array[0] == 'RLC':
        print('1010', end="")
        if len(array[0]) == 2:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    elif array[0] == 'RR' or array[0] == 'RRC':
        print('1011', end="")
        if len(array[0]) == 2:
            print('00', end="")
            last = last_two(array[3], 0)
        else:
            print('10', end="")
            last = last_two(array[3], 1)
        two(array[1])
        two(array[2])
        print(last)
    else:
        print("error", end="")


def two(string):
    string = int(string)
    result = ""
    while string > 0:
        result = str(string % 2) + result
        string //= 2
    if len(result) == 1:
        result = "00" + result
    elif len(result) == 2:
        result = "0" + result
    print(result, end="")


def last_two(string, num):
    string = int(string)
    result = ""
    while string > 0:
        result = str(string % 2) + result
        string //= 2
    if len(result) == 0:
        result = "000"
    if len(result) == 1:
        result = "00" + result
    elif len(result) == 2:
        result = "0" + result
    if num == 0:
        result += "0"
    else:
        if len(result) != 4:
            result = "0" + result
    return result


for _ in range(int(input())):
    machine(input())
