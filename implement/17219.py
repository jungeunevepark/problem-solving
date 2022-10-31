import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
password = {}
for _ in range(N):
    site, pwd = input().split()
    password[site] = pwd
for _ in range(M):
    print(password[input()])