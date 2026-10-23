def solution(dirs):
    answer = 0
    maps = [[[0, 0, 0, 0] for _ in range(11)] for _ in range(11)]
    
    op_dict = {"U":(-1, 0), "R":(0, 1), "D":(1, 0), "L":(0,-1)}
    op_idx = {"U":0, "D":2, "R":1, "L":3}
    
    x = 5
    y = 5
    
    for i in range(len(dirs)):
        op = dirs[i]
        dx, dy = op_dict[op]
        idx = op_idx[op]
        nx, ny = x + dx, y + dy
        print(x, y, nx, ny, maps[x][y][idx])
        
        if nx < 0 or ny < 0 or nx >= 11 or ny >= 11:
            continue
        
        if maps[x][y][idx] == 0:
            maps[x][y][idx] = 1
            maps[nx][ny][(idx+2)%4] = 1
            answer += 1
        
        x = nx
        y = ny
        
            
    return answer