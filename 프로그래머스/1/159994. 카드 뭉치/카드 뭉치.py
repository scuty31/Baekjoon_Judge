from collections import deque


def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1_queue = deque(cards1)
    cards2_queue = deque(cards2)
    goal_queue = deque(goal)

    while goal_queue:
        goal_word = goal_queue.popleft()

        if cards1_queue and cards1_queue[0] == goal_word:
            cards1_queue.popleft()
        elif cards2_queue and cards2_queue[0] == goal_word:
            cards2_queue.popleft()
        else:
            answer = 'No'
            break

    return answer