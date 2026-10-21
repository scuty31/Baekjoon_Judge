import heapq


def solution(n, k, enemy):
    answer = -1
    queue = []
    
    for i in range(len(enemy)):
        e = enemy[i]
        
        if len(queue) >= k:
            lq = heapq.heappop(queue)
            heapq.heappush(queue, max(lq, e))
            
            n -= min(lq, e)
        
        else:
            heapq.heappush(queue, e)

        if n < 0:
            answer = i
            break
        
    if answer == -1:
        answer = len(enemy)
        
    return answer