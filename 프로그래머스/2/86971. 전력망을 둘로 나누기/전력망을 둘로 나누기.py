def solution(n, wires):
    answer = n
    
    parent = list(range(n+1))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        
        return x
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
        
        if ra == rb:
            return False
        parent[ra] = rb
        
        return True
    
    for i in range(len(wires)):
        parent = list(range(n+1))
        
        for j in range(len(wires)):
            if i == j:
                continue
            union(wires[j][0], wires[j][1])
        
        l = find(wires[i][0])
        r = find(wires[i][1])
        l_cnt = 0
        r_cnt = 0
        
        for k in range(1, n+1):
            if find(k) == l:
                l_cnt += 1
            else:
                r_cnt += 1
        
        result = max(l_cnt, r_cnt) - min(l_cnt, r_cnt)
        answer = min(answer, result)
    
    return answer