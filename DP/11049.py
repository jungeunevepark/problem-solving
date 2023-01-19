import sys
sys.stdin = open("../basic_part1/input.txt", "r")

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
d = [[0]*N for _ in range(N)]
"""대각선에서 적게 떨어져있는 순서대로 계산해야됨!
    i열부터~ 계산하게 되면 0, 4에 있는 매트릭스 계산을 초반에 하게 되어서 오류!"""

for term in range(1, N):              # 대각선에서 얼마나 떨어져 있는지
    for i in range(N):                # 몇번째 대각선인지
        if i+term >= N:
            continue
        j = i + term            # col
        if term == 1:
            d[i][j] = array[i][0] * array[i][1] * array[j][1]
        else:
            d[i][j] = d[i][j-1] + array[i][0] * array[j-1][1] * array[j][1]
            for idx in range(i, j-1):
                d[i][j] = min(d[i][j], d[i][idx] + d[idx+1][j] +
                              array[i][0] * array[idx][1] * array[j][1])
print(d[0][N-1])
