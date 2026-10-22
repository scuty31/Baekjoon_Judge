from collections import deque


def bfs(maps_list, x, y, visited):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    result = int(maps_list[x][y])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(maps_list) or ny >= len(maps_list[0]):
                continue
            if maps_list[nx][ny] == "X":
                continue
            if visited[nx][ny]:
                continue
            
            result += int(maps_list[nx][ny])
            q.append((nx, ny))
            visited[nx][ny] = 1
    
    return result
        


def solution(maps):
    answer = []
    
    maps_list = []
    for i in range(len(maps)):
        maps_list.append(list(maps[i]))
    
    visited = [[0] * len(maps_list[0]) for _ in range(len(maps_list))]
    
    for x in range(len(maps_list)):
        for y in range(len(maps_list[0])):
            if maps_list[x][y] != 'X' and visited[x][y] == 0:
                result = bfs(maps_list, x, y, visited)
                answer.append(result)
    
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
                        
    return answer