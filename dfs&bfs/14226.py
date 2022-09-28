from collections import deque, defaultdict
import sys

S = int(sys.stdin.readline())
q = deque([(1, 1, 1)])  # 화면 이모티콘 개수, 시간, 복사 개수
already = defaultdict(int)
while q:
    now, time, copies = q.popleft()
    if now == S:
        break
    else:
        if now + copies < 2*S and already[(now+copies, copies)] == 0:
            already[(now+copies, copies)] = time + 1
            q.append((now+copies, time + 1, copies))    # print
        if now <= S and not now == copies and already[(now, now)] == 0:
            already[(now, now)] = time + 1
            q.append((now, time + 1, now))       # copy
        if now > 0 and now < S and already[(now-1, copies)] == 0:
            already[(now-1, copies)] = time + 1
            q.append((now - 1, time+1, copies))  # delete
print(time)
