import heapq


def solution(jobs):
    answer = 0
    time = 0
    heap = []
    
    jobs.sort()
    time = jobs[0][0] + jobs[0][1]
    response_time = [jobs[0][1]]
    idx = -1
    
    for i in range(1, len(jobs)):
        if jobs[i][0] > time and not heap:
            time = jobs[i][0]
            
        if jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
        else:
            idx = i
            break

    while heap:
        run_time, enter_time = heapq.heappop(heap)
        time += run_time
        response_time.append(time - enter_time)
        
        if idx != -1:
            if jobs[idx][0] > time and not heap:
                time = jobs[idx][0]
                
            while jobs[idx][0] <= time:
                heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
                idx += 1
                
                if idx >= len(jobs):
                    idx = -1
                    break
        
    answer = sum(response_time) // len(jobs)
    
    return answer