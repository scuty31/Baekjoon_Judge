def solution(n, costs):
    answer = 0
    parent = list(range(n))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        
        return x
    
    edges = sorted((w, a, b) for a, b, w in costs)
    cnt = 0
    
    for w, a, b in edges:
        ra = find(a)
        rb = find(b)
        
        if ra != rb:
            parent[ra] = rb
            answer += w
            cnt += 1
            
            if cnt == n-1:
                break
        
        
    return answer