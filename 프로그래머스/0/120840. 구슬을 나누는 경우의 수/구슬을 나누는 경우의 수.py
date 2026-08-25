def factorial(n):
    result = 1
    
    for i in range(2, n+1):
        result *= i
    
    return result


def solution(balls, share):
    answer = factorial(balls) // (factorial(balls-share) * factorial(share))
    
    return answer