from collections import deque


def find_way(maps_list, S, E, n, m):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0] * m for _ in range(n)]
    q = deque()
    Ex, Ey = E
    
    q.append(S)
    visited[S[0]][S[1]] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps_list[nx][ny] == "X":
                continue
            if visited[nx][ny] != 0:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
            
            if nx == Ex and ny == Ey:
                break
    
    return visited[Ex][Ey] - 1


def solution(maps):
    answer = 0
    maps_list = []
    
    for i in range(len(maps)):
        maps_list.append(list(maps[i]))
    
    S = tuple()
    E = tuple()
    L = tuple()
    n = len(maps)
    m = len(maps[0])
    
    for x in range(n):
        for y in range(m):
            if maps_list[x][y] == "S":
                S = (x, y)
            elif maps_list[x][y] == "E":
                E = (x, y)
            elif maps_list[x][y] == "L":
                L = (x, y)
    
    result = find_way(maps_list, S, L, n, m)
    
    if result == -1:
        return -1
    else:
        answer += result
    
    result = find_way(maps_list, L, E, n, m)
    
    if result == -1:
        return -1
    else:
        answer += result
    
    return answer