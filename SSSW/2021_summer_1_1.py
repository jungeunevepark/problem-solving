import sys
sys.stdin = open("../greedy/input.txt", "r")

N = int(input())
classroom = [[0] * N for _ in range(N)]
favorite = [list(map(int, input().split())) for _ in range(N**2)]
look = []

def sit_student(list, classroom, look):
    result, result_empty = -1, -1
    resultx, resulty = 0, 0
    for i in range(N):
        for j in range(N):
            if classroom[i][j] > 0:
                continue
            count = 0
            empty = 0
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<= ni <N and 0<=nj<N:
                    if classroom[ni][nj] == 0:
                        empty += 1
                    elif classroom[ni][nj] in list[1:]:
                        count += 1
            if result < count:
                result = count
                result_empty = empty
                resultx = i
                resulty = j

            elif result == count and result_empty < empty:
                # result는 같으므로 갱신 안함
                result_empty = empty
                resultx = i
                resulty = j

    classroom[resultx][resulty] = list[0]
    look.append((resultx, resulty))
    return classroom, look

def find_full(classroom, look, favorite):
    answer = 0
    for idx, (i, j) in enumerate(look):
        count = 0
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < N and 0 <= nj < N and classroom[ni][nj] in favorite[idx][1:]:
                count += 1
        if count == 1:
            answer += 1
        elif count == 2:
            answer += 10
        elif count == 3:
            answer += 100
        elif count == 4:
            answer += 1000
    return answer

for idx in range(len(favorite)):
    classroom, look = sit_student(favorite[idx], classroom, look)
print(find_full(classroom, look, favorite))