import heapq


def solution(k, m, score):
    answer = 0
    score_hq = []

    for s in score:
        heapq.heappush(score_hq, (-s, s))

    while len(score_hq) >= m:
        box_score = []

        for _ in range(m):
            box_score.append(heapq.heappop(score_hq)[1])

        answer += box_score[-1] * m

    return answer