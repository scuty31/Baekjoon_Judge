from collections import deque


def check_wires(n, graph, s, e):
    result = 0
    visited = [False for _ in range(n+1)]
    q = deque()
    
    q.append(s)
    visited[s] = True
    
    while q:
        node = q.popleft()

        for next_node in graph[node]:
            if next_node == e:
                continue
            if visited[next_node]:
                continue

            visited[next_node] = True
            result += 1
            q.append(next_node)
    
    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    for s, e in wires:
        left = check_wires(n, graph, s, e)
        right = check_wires(n, graph, e, s)
        
        result = max(left, right) - min(left, right)
        answer = min(answer, result)
        
    return answer