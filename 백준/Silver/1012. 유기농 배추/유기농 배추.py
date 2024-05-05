import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y):
    queue = [(x, y)]
    matrix[x][y] = 0
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0]*n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(m):
        for b in range(n):
            if matrix[a][b] == 1:
                BFS(a, b)
                cnt += 1
    print(cnt)
