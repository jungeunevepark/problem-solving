import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    A = [list(map(int, input().split())) for _ in range(size)]
    # 90도
    j90 = 0
    i180 = size-1
    j270 = size-1
    print("#", end = "")
    print(test_case)
    for _ in range(size):
        for i in range(size-1, -1, -1):
            print(A[i][j90], end="")
        print("", end=" ")
        # 180도
        for j in range(size-1, -1, -1):
            print(A[i180][j], end = "")
        print("", end=" ")
        # 270도
        for i in range(size):
            print(A[i][j270], end = "")
        print()
        j90 += 1
        i180 -= 1
        j270 -= 1
