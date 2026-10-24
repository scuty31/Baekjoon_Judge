from collections import deque


def solution(land, height):
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n = len(land)
    
    def bfs(height, x, y, idx):
        q = deque()
        
        q.append((x, y))
        visited[x][y] = idx
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= len(land) or ny >= len(land[0]):
                    continue
                if visited[nx][ny] != 0:
                    continue
                if max(land[nx][ny], land[x][y]) - min(land[nx][ny], land[x][y]) > height:
                    continue
                
                visited[nx][ny] = idx
                q.append((nx, ny))

    
    visited = [[0 for _ in range(n)] for _ in range(n)]
    idx = 1
    
    for x in range(n):
        for y in range(n):
            if visited[x][y] != 0:
                continue
            else:
                bfs(height, x, y, idx)
                idx += 1
    
    edges = []
    
    for x in range(len(land)):
        for y in range(n):
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx >= n or ny >= n:
                    continue
                if visited[nx][ny] != visited[x][y]:
                    edges.append((abs(land[x][y] - land[nx][ny]), visited[x][y], visited[nx][ny]))
    
    edges.sort()
    parent = list(range(idx))
    
    def find(x):
        while parent[x] != x:
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
    
    cnt = 0
    
    for w, a, b in edges:
        if union(a, b):
            answer += w
            cnt += 1
            
            if cnt == idx-2:
                break
    
    return answer