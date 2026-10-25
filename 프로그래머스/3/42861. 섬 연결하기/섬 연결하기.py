def solution(n, costs):
    answer = 0
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
    
    edges = sorted(list((w, a, b) for a, b, w in costs))
    cnt = 0
    
    for w, a, b in edges:
        if union(a, b):
            answer += w
            cnt += 1
            
            if cnt == n-1:
                break
        
    return answer