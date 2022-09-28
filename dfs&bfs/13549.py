from collections import deque, defaultdict

N, M = map(int, input().split())
q = deque([(N, 0)])
already = defaultdict(int)
result = 100000

while q:
    v, time = q.popleft()
    if time > result:
        continue
    if v == M:
        result = min(result, time)
    if v - 1 >= -1:
        if already[v-1] == 0 or already[v-1] >= time+1:
            already[v-1] = time+1
            q.append((v-1, time + 1))
    if v + 1 <= M+1:
        if already[v+1] == 0 or already[v+1] >= time+1:
            already[v+1] = time + 1
            q.append((v+1, time + 1))
    if 2*v <= 2*M and v > 0:                              # 2배 처리의 경우 time이 증가하지 않음으로 처리 조심
        if already[2*v] == 0 or already[2*v] > time:
            already[2*v] = time
            q.append((2*v, time))
print(result)
