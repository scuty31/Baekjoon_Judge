from collections import deque
import heapq


def solution(priorities, location):
    answer = 0
    priority_queue = deque()
    max_priority = []

    for i in range(len(priorities)):
        priority_queue.append((priorities[i], i))
        heapq.heappush(max_priority, (-priorities[i], priorities[i]))


    while True:
        priority, loc = priority_queue.popleft()
        if loc == location and priority == max_priority[0][1]:
            answer += 1
            break

        if priority == max_priority[0][1]:
            heapq.heappop(max_priority)
            answer += 1
        else:
            priority_queue.append((priority, loc))

    return answer