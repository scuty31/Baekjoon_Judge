from collections import deque


def solution(A, B):
    answer = 0
    if A == B:
        return 0

    A_queue = deque(A)
    B_queue = deque(B)

    for _ in range(len(A)):
        answer += 1
        A_queue.rotate(1)

        if A_queue == B_queue:
            break
    
    if A_queue != B_queue:
        answer = -1
    
    return answer