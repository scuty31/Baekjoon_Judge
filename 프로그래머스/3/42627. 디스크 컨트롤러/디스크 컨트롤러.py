import heapq


def solution(jobs):
    answer = 0
    queue = []
    
    jobs.sort()
    
    response_time = [jobs[0][1]]
    now_time = 0
    now_time = jobs[0][1] + jobs[0][0]
    idx = 1
    
    if len(jobs) == 1:
        answer = response_time[0]
        return answer
    
    if jobs[idx][0] > now_time and not queue:
        now_time = jobs[idx][0]
        
    while idx < len(jobs) and jobs[idx][0] <= now_time:
        heapq.heappush(queue, (jobs[idx][1], jobs[idx][0]))
        idx += 1
    
    while queue:
        e, s = heapq.heappop(queue)
        
        now_time += e
        response_time.append(now_time - s)
        
        if idx < len(jobs):
            if jobs[idx][0] > now_time and not queue:
                now_time = jobs[idx][0]
                
            while idx < len(jobs) and jobs[idx][0] <= now_time:
                heapq.heappush(queue, (jobs[idx][1], jobs[idx][0]))
                idx += 1
    
    answer = sum(response_time) // len(jobs)
    
    return answer