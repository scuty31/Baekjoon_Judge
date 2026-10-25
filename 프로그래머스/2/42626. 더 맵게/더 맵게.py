import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        min_scoville = heapq.heappop(scoville)
        
        if len(scoville) == 0:
            if min_scoville < K:
                answer = -1
            break
        
        if min_scoville >= K:
            break
        
        next_min_scoville = heapq.heappop(scoville)
        
        new_scoville = min_scoville + (next_min_scoville*2)
        
        heapq.heappush(scoville, new_scoville)
        answer += 1
        
    return answer