def factorial():
    n = int(input())

    result = 1
    for i in reversed(range(1, n+1)):
        result *= i

    result_list = list(str(result))

    answer = 0
    while True:
        if result_list.pop() == '0':
            answer += 1
        else:
            break

    return answer


print(factorial())