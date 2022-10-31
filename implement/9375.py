from collections import defaultdict
import sys
sys.stdin = open("input.txt", "r")
for _ in range(int(input())):
    wear = defaultdict(list)
    answer = 1
    for _ in range(int(input())):
        n, m = input().split()
        wear[m].append(n)
    for k in wear.keys():
        answer *= len(wear[k]) + 1
    print(answer-1)