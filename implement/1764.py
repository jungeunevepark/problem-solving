import sys
sys.stdin = open("../greedy/input.txt", "r")
N, M = map(int, input().split())
noheard = list(input() for _ in range(N))
nolook = list(input() for _ in range(M))
noheard.sort(reverse=True)
nolook.sort(reverse=True)
answer = []
count,i,j = 0, 0, 0
A = nolook.pop()
B = noheard.pop()
while True:
    test = []
    if A == B:
        answer.append(A)
        count+=1
        if not nolook:
            break
        A = nolook.pop()
        B = noheard.pop()
    else:
        test.append(A)
        test.append(B)
        if sorted(test)[0] == A:
            if not nolook:
                break
            A = nolook.pop()
        else:
            if not noheard:
                break
            B = noheard.pop()
print(count)
print("\n".join(sorted(answer)))