import sys
sys.stdin = open("../basic_part1/input.txt", "r")
for _ in range(int(input())):
    n = int(input())
    d = [1, 1, 2] + [0] * (n-2)
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])