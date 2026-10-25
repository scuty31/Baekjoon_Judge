def solution(n, computers):
    answer = n
    parent = list(range(n))
    
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        
        if ra != rb:
            parent[ra] = rb
            return True
        return False
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if union(i, j):
                    answer -= 1
    
    return answer