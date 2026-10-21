import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        min_scoville = heapq.heappop(scoville)
        
        if min_scoville >= K:
            break
        
        if len(scoville) == 0:
            answer = -1
            break
        
        second_min_scoville = heapq.heappop(scoville)
        heapq.heappush(scoville, min_scoville + 2*second_min_scoville)
        answer += 1
        
    return answer