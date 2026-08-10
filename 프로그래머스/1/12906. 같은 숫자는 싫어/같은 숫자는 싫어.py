def solution(arr):
    answer = []

    for s in arr:
        if len(answer) == 0 or answer[-1] != s:
            answer.append(s)

    return answer