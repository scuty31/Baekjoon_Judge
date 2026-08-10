from collections import deque


def solution(numbers, k):
    answer = 0
    queue = deque(numbers)

    for _ in range(k-1):
        queue.rotate(-2)

    answer = queue[0]

    return answer