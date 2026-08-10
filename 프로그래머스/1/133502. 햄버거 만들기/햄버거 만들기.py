def solution(ingredient):
    answer = 0
    stack = []

    for ing in ingredient:
        if len(stack) == 0:
            stack.append(ing)
            continue

        # 빵이 들어오면
        if ing == 1:
            # 햄버거를 만들 수 있는지 확인
            if len(stack) > 2:
                # 만들 수 있다면 햄버거를 포장하고 answer + 1
                if stack[-1] == 3 and stack[-2] == 2 and stack[-3] == 1:
                    for _ in range(3):
                        stack.pop()

                    answer += 1
                    continue
            # 만들 수 없다면 재료 stack에 빵 추가
            stack.append(ing)
            continue

        stack.append(ing)

    return answer