import heapq


def solution(k, score):
    answer = []
    top_score = []

    # 가수의 점수를 가져옴
    for s in score:
        heapq.heappush(top_score, s)

        # 만약 명예의 전당에 k+1개의 점수가 올라가 있다면 가장 낮은 점수를 빼냄.
        if len(top_score) > k:
            heapq.heappop(top_score)
        
        # 현재 명예의 전당에 올라간 점수들 중 최소 점수를 가져옴.
        answer.append(top_score[0])

    return answer
