def solution(n, costs):
    answer = 0
    parent = list(range(n))
    
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
    
    edges = sorted(list((w, s, e) for s, e, w in costs))
    
    cnt = 0
    
    for w, s, e in edges:
        if union(s, e):
            cnt += 1
            answer += w
            
            if cnt == n-1:
                break
                
    return answer