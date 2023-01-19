import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    time = int(input())
    check = list(map(int, input().split()))
    check.sort()
    most = check[0]
    many = 1
    now_many = 1
    now = check[0]
    for i in range(1, len(check)):
        if now != check[i]:
            if now_many >= many:
                most = check[i-1]
                many = now_many
            now = check[i]
            now_many = 1
        else:
            now_many += 1
    print("#", end="")
    print(test_case, end=" ")
    print(most)