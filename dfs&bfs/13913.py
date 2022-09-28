from collections import deque, defaultdict

N, M = map(int, input().split())
q = deque([(N, 0)])
already = defaultdict(int)
route = {}
count = 0
result = 100000                 # 0 100000의 입력이 들어와도 100000초 내에는 만날수 있음

while q:
    v, time = q.popleft()
    if time > result:
        continue
    if v == M:
        result = time
        break
    if v - 1 >= -1:
        if already[v-1] == 0 or already[v-1] >= time+1:
            already[v-1] = time+1
            route[v-1] = v
            q.append((v-1, time + 1))
    if v + 1 <= M+1:
        if already[v+1] == 0 or already[v+1] >= time+1:
            already[v+1] = time + 1
            route[v+1] = v
            q.append((v+1, time + 1))
    if 2*v <= 2*M and v > 0:
        if already[2*v] == 0 or already[2*v] >= time+1:
            already[2*v] = time+1
            route[2*v] = v
            q.append((2*v, time + 1))
a = []
for _ in range(result):
    a.append(M)
    M = route[M]
print(result)
print(N, end=" ")
for route in a[::-1]:
    print(route, end=" ")
