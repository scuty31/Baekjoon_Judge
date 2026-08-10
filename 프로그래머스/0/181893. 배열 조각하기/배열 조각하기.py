from collections import deque


def solution(arr, query):
    answer = []
    arr_queue = deque(arr)

    for i in range(len(query)):
        if i % 2 == 0:
            while len(arr_queue) > query[i]+1:
                arr_queue.pop()

        else:
            for _ in range(query[i]):
                arr_queue.popleft()

    answer = list(arr_queue)

    return answer