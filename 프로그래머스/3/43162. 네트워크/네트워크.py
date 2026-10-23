def solution(n, computers):
    answer = n
    parent = list(range(n))
    
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
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if union(i, j):
                    answer -= 1
    
    return answer