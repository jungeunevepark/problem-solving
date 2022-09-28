from collections import deque, defaultdict

N, M = map(int, input().split())
q = deque([(N, 0)])
already = defaultdict(int)

while q:
    v, time = q.popleft()
    if v == M:
        result = time
        break
    if v - 1 >= -1:
        if already[v-1] == 0 or already[v-1] >= time+1:
            already[v-1] = time+1
            q.append((v-1, time + 1))
    if v + 1 <= M+1:
        if already[v+1] == 0 or already[v+1] >= time+1:
            already[v+1] = time + 1
            q.append((v+1, time + 1))
    if 2*v <= 2*M:
        if already[2*v] == 0 or already[2*v] >= time+1:
            already[2*v] = time+1
            q.append((2*v, time + 1))

print(result)
count = 1
while q:
    v, time = q.popleft()
    if time > result:
        continue
    if v == M:
        if result == time:
            count += 1
    if not (v == M + 1 or v == M - 1 or v == (1/2)*M):
        continue
    if v - 1 >= -1:
        if already[v-1] == 0 or already[v-1] >= time+1:
            already[v-1] = time+1
            q.append((v-1, time + 1))
    if v + 1 <= M+1:
        if already[v+1] or already[v+1] >= time+1:
            already[v+1] = time + 1
            q.append((v+1, time + 1))
    if 2*v <= 2*M:
        if already[2*v] or already[v-1] >= time+1:
            already[2*v] = time+1
            q.append((2*v, time + 1))
print(count)
