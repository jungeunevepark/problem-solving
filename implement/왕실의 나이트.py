a, b = input()
b = int(b)

com = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(com)):
    if com[i] == a:
        break

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

count = 0

for j in range(8):
    next = i + dx[j]
    nx = com[next]
    ny = b + dy[j]
    if nx in com and 1 <= ny <= 8:
        count += 1
print(count)
