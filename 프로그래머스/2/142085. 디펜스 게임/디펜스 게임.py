import heapq


def solution(n, k, enemy):
    answer = 0
    q = []
    
    for i in range(len(enemy)):
        heapq.heappush(q, enemy[i])
        
        if len(q) > k:
            n -= heapq.heappop(q)

        if n < 0:
            answer = i
            break
    
    if answer == 0:
        answer = len(enemy)
        
    return answer