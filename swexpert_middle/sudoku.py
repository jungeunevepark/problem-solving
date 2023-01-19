import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    print("#", end="")
    print(test_case, end=" ")
    # 가로줄
    for i in range(9):
        check = set()
        for j in range(9):
            check.add(sudoku[i][j])
        if len(check) < 9:
            result=0
            break
    # 세로줄
    if result == 1:
        for i in range(9):
            check = set()
            for j in range(9):
                check.add(sudoku[j][i])
            if len(check) < 9:
                result=0
                break
    # 칸
    if result == 1:
        for x in range(0, 8, 3):
            for y in range(0, 8, 3):
                check = set()
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        check.add(sudoku[i][j])
                if len(check) < 9:
                    result=0
                    break
    if result == 1:
        print(1)
    else:
        print(0)