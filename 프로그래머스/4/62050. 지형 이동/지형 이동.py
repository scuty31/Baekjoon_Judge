from collections import deque


def solution(land, height):
    answer = 0
    n = len(land)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    visited = [[0] * n for _ in range(n)]
    
    def bfs(n, x, y, idx, height):
        q = deque()
        q.append((x, y))
        visited[x][y] = idx
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if visited[nx][ny] > 0:
                    continue
                if abs(land[x][y] - land[nx][ny]) > height:
                    continue
                    
                visited[nx][ny] = idx
                q.append((nx, ny))
    
    idx = 1
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                bfs(n, x, y, idx, height)
                idx += 1
    
    parent = list(range(idx+1))
    
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
        
        if ra != rb:
            parent[ra] = rb
            return True
        return False
    
    edges = []
    
    for x in range(n):
        for y in range(n):
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx >= n or ny >= n:
                    continue
                
                if visited[x][y] != visited[nx][ny]:
                    edges.append((abs(land[x][y] - land[nx][ny]), visited[x][y], visited[nx][ny]))

    edges.sort()
    cnt = 0
    
    for w, a, b in edges:
        if union(a, b):
            answer += w
            cnt += 1
            
            if cnt == idx-2:
                break
    return answer