N = int(input())
people = list(map(int, input().split()))

people.sort()
answer = 0
nowtime = 0
for p in people:
    nowtime += p
    answer += nowtime
print(answer)