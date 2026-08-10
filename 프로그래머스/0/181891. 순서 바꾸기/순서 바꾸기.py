from collections import deque


def solution(num_list, n):
    answer = []
    num_queue = deque(num_list)

    for _ in range(n):
        num_queue.append(num_queue.popleft())

    answer = list(num_queue)
    
    return answer