from collections import deque


def solution(t, p):
    answer = 0
    n = len(p)

    end = n
    num_list = deque(t[:n])

    for i in range(n, len(t)):
        if ''.join(num_list) <= p:
            answer += 1

        num_list.popleft()
        num_list.append(t[i])

    if ''.join(num_list) <= p:
        answer += 1

    return answer