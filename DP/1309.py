N = int(input())
d = [[0]*3 for _ in range(N+1)]        # idx명의 사자를 배치하는 방법의 수(첫째줄에 사자가 있는 것만)

d[1] = [1, 1, 1]

for i in range(2, N+1):
    d[i][0] = sum(d[i-1]) % 9901
    d[i][1] = (d[i-1][0] + d[i-1][2]) % 9901
    d[i][2] = (d[i-1][0] + d[i-1][1]) % 9901
print(sum(d[N]) % 9901)
