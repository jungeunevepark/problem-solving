"""
NxN인 격자에서 연습, (r행, c열), A[r][c]는 (r, c)에 저장된 물의 양
1번 행-N번 행,  1번 열-N번 열 연결되어 있음
비바라기 시전 : (N, 1), (N, 2), (N-1,1), (N-1,2)에 비구름이 생김
이동 명령 di = 방향, si = 거리
1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
3. 구름 모두 제거
4. 2에서 물이 증가한 칸 (r, c)에 물복사 버그 마법을 시전.
    이 경우 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수 만큼 (r,c)에 있는 바구니의 물의 양 증가
    이동과 달리 경계를 넘어가는 칸은 거리가 1인 칸이 아니다
5. 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생기고 물의 양이 2 줄어든다.
    이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
M번의 이동 후, 물의 양의 합을 구하자!
"""
import sys
sys.stdin = open("../implement/input.txt", "r")

N, M = map(int, input().split())
sky = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2,1)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(clouds, sky):
    new_skys = [[0]*N for _ in range(N)]
    new_clouds = []
    for x, y in clouds:
        nx = x+(s % N)*dx[d]
        ny = y+(s % N)*dy[d]
        if nx < 0:
            nx += N
        elif nx >= N:
            nx -= N
        if ny < 0:
            ny += N
        elif ny >= N:
            ny -= N
        new_clouds.append((nx, ny))
        new_skys[nx][ny] = 1
        sky[nx][ny] += 1
    return new_clouds, sky, new_skys


def copy_water(clouds,sky):
    for i, j in clouds:
        count = 0
        for ni, nj in [(i-1, j-1), (i+1, j-1), (i+1, j+1), (i-1, j+1)]:
            if 0 <= ni < N and 0 <= nj < N and sky[ni][nj] > 0:
                count += 1
        sky[i][j] += count
    return sky

def make_clouds(sky, cloud):
    make_cloud = []
    for i in range(N):
        for j in range(N):
            if sky[i][j] >= 2 and cloud[i][j] == 0:
                sky[i][j] -= 2
                make_cloud.append((i, j))
    return make_cloud

for d, s in moves:
    new_clouds, sky, new_skys = move_cloud(clouds, sky)
    sky = copy_water(new_clouds, sky)
    clouds = make_clouds(sky, new_skys)
print(sum(sky[i][j] for i in range(N) for j in range(N)))
