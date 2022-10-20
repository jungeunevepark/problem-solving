import sys
sys.stdin = open("input.txt", "r")
input= sys.stdin.readline
S = set()
for _ in range(int(input().rstrip())):
    comment = list(input().rstrip().split())

    if comment[0] == 'add':
        S.add(int(comment[1]))
    elif comment[0] == 'remove':
        if int(comment[1]) in S:
            S.remove(int(comment[1]))
    elif comment[0] == 'check':
        if int(comment[1]) in S:
            print(1)
        else:
            print(0)
    elif comment[0] == 'toggle':
        if int(comment[1]) in S:
            S.remove(int(comment[1]))
        else:
            S.add(int(comment[1]))
    elif comment[0] == 'all':
        S = set(range(1, 21))
    elif comment[0] == 'empty':
        S = set()