from collections import deque

def account_array(answer, draw):
    g = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    array_numer = [0]
    count = 0
    "find group"
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                count += 1
                g[i][j] = count
                group(i, j, count, draw, array_numer, visited, g, array_numer)

    "find connect line"
    chemi = [[0] * (count + 1) for _ in range(count + 1)]
    for i in range(n):
        for j in range(n):
            if not i == n - 1:
                if not g[i][j] == g[i + 1][j]:
                    chemi[g[i][j]][g[i + 1][j]] += 1
                    chemi[g[i + 1][j]][g[i][j]] += 1
            if not j == n - 1:
                if not g[i][j] == g[i][j + 1]:
                    chemi[g[i][j]][g[i][j + 1]] += 1
                    chemi[g[i][j + 1]][g[i][j]] += 1
    """chemistry"""
    for i in range(1, count + 1):
        for j in range(i + 1, count + 1):
            answer += (array_numer[i][0] + array_numer[j][0]) * chemi[i][j] * array_numer[i][1] * array_numer[j][1]
    return answer

def group(i, j, group_number, array, array_number, visited, g, array_numer):
    """ 처음 위치에 대해 array 속의 그룹 찾기 """
    count_group_number = 1
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for nx,ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0<= nx < n and 0<= ny < n and array[nx][ny] == array[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                g[nx][ny] = group_number
                count_group_number += 1
                q.append((nx, ny))
    array_number.append((count_group_number, array[i][j]))

def circle(array, n):
    """왼쪽 위"""
    new = [[] for _ in range(n//2)]
    for j in range(n//2):
        for i in range(n//2-1, -1, -1):
            new[j].append(array[i][j])

    for i in range(n//2):
        array[i][:n//2] = new[i]

    """오른쪽 위"""
    new = [[] for _ in range(n // 2)]
    for j in range(n // 2+1, n):
        for i in range(n // 2 - 1, -1, -1):
            new[j-n//2-1].append(array[i][j])

    for i in range(n//2):
        array[i][n//2+1:] = new[i]

    """왼쪽 아래"""
    new = [[] for _ in range(n//2)]
    for j in range(n//2):
        for i in range(n-1, n//2, -1):
            new[j].append(array[i][j])

    for i in range(n//2):
        array[i+n//2+1][:n//2] = new[i]

    """오른쪽 아래"""
    new = [[] for _ in range(n // 2)]
    for j in range(n // 2+1, n):
        for i in range(n-1, n//2, -1):
            new[j-n//2-1].append(array[i][j])

    for i in range(n // 2):
        array[i + n // 2 + 1][n//2+1:] = new[i]

    """ 십자가 """
    temp = array[n//2][n//2+1:]
    array[n // 2][n // 2 + 1:] = list(array[i][n // 2] for i in range(n // 2 + 1, n))
    swap = array[n//2][:n//2]
    swap.reverse()
    for i in range(n // 2 + 1, n):
        array[i][n//2] = swap[i-n//2-1]
    array[n//2][:n//2] = list(array[i][n//2] for i in range(n//2))
    temp.reverse()
    for i in range(n // 2):
        array[i][n // 2] = temp[i]

    return array


n = int(input())
draw = [list(map(int, input().split())) for _ in range(n)]
answer = 0
answer = account_array(answer, draw)
circle(draw, n)
answer = account_array(answer, draw)
circle(draw, n)
answer = account_array(answer, draw)
circle(draw, n)
answer = account_array(answer, draw)
print(answer)