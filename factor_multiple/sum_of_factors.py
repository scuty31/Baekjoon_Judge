"""
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.
"""

import sys

while (True):
    n = int(sys.stdin.readline().rstrip())
    factor = []
    answer = ''

    if n == -1:
        break

    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            factor.append(i)
            if i != n//i:
                factor.append(n//i)

    factor.sort()
    factor.pop(-1)

    if(sum(factor) == n):
        answer += str(n) + ' = '
        a = ' + '.join(map(str,factor))
        answer += a

    else:
        answer += str(n) + ' is NOT perfect.'
    
    print(answer)
