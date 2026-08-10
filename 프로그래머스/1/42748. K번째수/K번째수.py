import heapq


def solution(array, commands):
    answer = []

    for i, j, k in commands:
        array_hq = array[i-1:j]
        heapq.heapify(array_hq)

        for _ in range(k-1):
            heapq.heappop(array_hq)

        answer.append(heapq.heappop(array_hq))

    return answer