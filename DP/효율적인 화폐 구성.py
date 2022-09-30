N, M = map(int, input().split())
money = list(int(input()) for _ in range(N))

d = [0] * 10000
for m in money:
    d[m] = 1

for i in range(2, M + 1):
    if not(i < money[0] or d[i - money[0]] == 0 or d[i - money[0]] == -1):
        d[i] = d[i - money[0]] + 1
    for j in range(1, N):
        if i < money[j] or d[i - money[j]] == 0 or d[i - money[j]] == -1:
            continue
        if d[i] == 0:
            d[i] = d[i-money[j]] + 1
        d[i] = min(d[i], d[i-money[j]] + 1)
    if d[i] == 0:
        d[i] = -1
print(d[M])

"Answer"
d = [10001] * (M+1)
d[0] = 0
for i in range(N):
    for j in range(money[i], M+1):
        if d[j-money[i]] != 10001:
            d[j] = min(d[j], d[j-money[i]]+1)
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
