"""
어항정리 순서
1. 물고기 수가 가장 적은 어항들에 물고기를 1마리씩 넣어준다
2. 어항을 규칙에 맞게 정리한다.
    1) 가장 왼쪽에 있는 어항을 그 옆의 어항 위에 올린다.
    2) 높이가 2이상인 어항을 공중에 띄워서 시계방향으로 90도 회전시킨다.
    3) 그 어항을 바닥 어항 가장 왼쪽부터 차례로 올린다. (즉 가장 위의 것이 가장 왼쪽....?)
    4) 2~4의 과정은 공중부향한 어항을 바닥에 놓을 때 밑에 어항이 있는 경우에만 가능
3. 어항의 물고기 수 조절
    1) 모든 인접한 두 칸의 차를 5로 나누어 그 값만큼 많은 곳에서 적은 곳으로 물고기를 옮긴다
    2) 가장 왼쪽, 아랫쪽을 순서로 어항을 일렬로 놓는다
4. 다시 공중부향 작업
    1) 어항 N/2개를 공중에 띄운 후 180도 돌려서 윗줄에 놓는다.
    2) 한번 더
5. 물고기 수 조절 다시 함
6. 다시 일렬로 놓기
"""
import sys
sys.stdin = open("../greedy/input.txt", "r")
N, K = map(int, input().split()) # N개의 어항, K개 이하의 차이
fishhouse = list(map(int, input().split()))
fishmap = [[-1] * N for _ in range(N)]

for idx, x in enumerate(fishhouse):
    fishmap[N-1][idx] = x

def print_map(array):
    for i in range(N):
        for j in range(N):
            if array[i][j] == -1:
                print(" ", end = " ")
            else:
                print(array[i][j], end= " ")
        print()
    print()

# print_map()


def plus_fish(fishhouse):
    plus = [0]
    smallest = fishhouse[0]
    for i in range(1, N):
        if fishhouse[i] < smallest:
            smallest = fishhouse[i]
            plus = [i]
        elif fishhouse[i] == smallest:
            plus.append(i)

    for p in plus:
        fishhouse[p] += 1

    return fishhouse
def roll_fishhouse_first(fishmap):
    fishmap[N-2][1] = fishmap[N-1][0]
    fishmap[N-1][0] = -1
    while True:
        first = N
        last = 0
        for j in range(N):
            base = 0
            if fishmap[N-1][j] != -1:
                base = fishmap[N - 1][j]
                for i in range(N-1, -1, -1):
                    if fishmap[i][j] == -1:
                        break
                if i == N-2:
                    fishmap[N-1][j] = base
                    break
                first = min(first, j)
                last = max(last, j)
                height = N - i - 1
        if N-last <= height :
            break
        roll = roll_array(fishmap, first, last, height)
        for i in range(N-height, N):
            for j in range(first, last+1):
                fishmap[i][j] = -1
        for i in range(len(roll)):
            for j in range(len(roll[0])):
                fishmap[N-len(roll)-1+i][last+1+j] = roll[i][j]
    return fishmap

def roll_array(find, first, last, height):
    """nXm의 크기의 array를 입력받았을 떄 시계방향으로 90도 회전한 것을 반환"""
    array = [[0]*(last-first+1) for _ in range(height)]
    n = len(array)
    m = len(array[0])
    for i in range(n):
        for j in range(m):
            array[i][j] = find[N-height+i][first+j]
    roll = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            roll[j][n-i-1] = array[i][j]

    return roll
def chemical_fish(fishmap):
    """인접한 물고기 수를 계산하여 물고기 수 조절하는 함수"""
    # print_map(fishmap)
    n = len(fishmap)
    new = [[0] * n for _ in range(n)]
    # print_map(new)
    for i in range(n):
        for j in range(n):
            if fishmap[i][j] != -1:
                for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=ni<n and 0<=nj<n and fishmap[ni][nj] != -1:
                        d = abs(fishmap[i][j] - fishmap[ni][nj]) // 5
                        if d > 0:
                            if fishmap[i][j] > fishmap[ni][nj]:
                                new[i][j] += (-1)*d
                                new[ni][nj] += d
                            else:
                                new[i][j] += d
                                new[ni][nj] += (-1) * d
    # print_map(new)
    for i in range(n):
        for j in range(n):
            fishmap[i][j] += new[i][j] // 2
    # print_map(fishmap)
    return fishmap

def line_fishhouse(fishmap):
    new_fishmap = [[-1]*N for _ in range(N)]
    count = 0
    for j in range(N):
        for i in range(N-1, -1, -1):
            if fishmap[i][j] != -1:
                new_fishmap[N-1][count] = fishmap[i][j]
                count += 1
    # print_map(new_fishmap)
    return new_fishmap
def roll_fishhouse_second(fishmap):
    "N/2 나누기"
    for i in range(N//2):
        fishmap[N-2][i+N//2] = fishmap[N-1][N//2-1-i]
        fishmap[N - 1][N // 2 - 1 - i] = -1
    "N/4 나누기"
    for i in range(2):
        for j in range(N//4):
            fishmap[N-4+i][N-1-j] = fishmap[N-1-i][N//2+j]
            fishmap[N-1-i][N//2+j] = -1
    # print_map(fishmap)
    return fishmap

answer = 0
while True:
    fishmap[N-1] = plus_fish(fishmap[N-1])
    fishmap = roll_fishhouse_first(fishmap)
    fishmap = chemical_fish(fishmap)
    fishmap = line_fishhouse(fishmap)
    fishmap = roll_fishhouse_second(fishmap)
    fishmap = chemical_fish(fishmap)
    fishmap = line_fishhouse(fishmap)
    answer += 1
    if max(fishmap[i][j] for i in range(N) for j in range(N)) - min(fishmap[i][j] for i in range(N) for j in range(N) if not fishmap[i][j] == -1) <= K :
        break
print(answer)