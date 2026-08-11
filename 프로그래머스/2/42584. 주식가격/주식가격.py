def solution(prices):
    answer = [0] * len(prices)
    stack = []

    # 앞에서부터 순차적으로 탐색
    for i in range(len(prices)):
        # 스택에 들어가 있는 모든 index 별로 현재 가격보다 높은 가격들의 길이 구하기
        while stack and prices[stack[-1]] > prices[i]:  # stack이 비어있지 않고, stack에 들어있는 값이 현재보다 크다면 pop
            prev = stack.pop()
            answer[prev] = i - prev

        stack.append(i)

    # 마지막까지 값이 떨어지지 않은 경우
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1

    return answer