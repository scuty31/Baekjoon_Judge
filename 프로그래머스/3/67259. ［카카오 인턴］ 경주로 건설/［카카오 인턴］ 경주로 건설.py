from collections import deque

def solution(board):
    n = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    INF = float('inf')
    visited = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    q = deque()
    res = INF
    for d in (1, 2):
        visited[0][0][d] = 0
        q.append((0, 0, d, 0))

    while q:
        x, y, r, result = q.popleft()
        if visited[x][y][r] != result:
            continue
        if x == n - 1 and y == n - 1:
            res = min(res, result)
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 1:
                continue
            nc = result + (100 if i == r else 600)
            if nc < visited[nx][ny][i]:
                visited[nx][ny][i] = nc
                q.append((nx, ny, i, nc))

    return res