"""
4 × 3 = 12이다.

이 식을 통해 다음과 같은 사실을 알 수 있다.

3은 12의 약수이고, 12는 3의 배수이다.

4도 12의 약수이고, 12는 4의 배수이다.

두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

첫 번째 숫자가 두 번째 숫자의 약수이다.                 -> factor
첫 번째 숫자가 두 번째 숫자의 배수이다.                 -> multiple
첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.   -> neither
"""

import sys

while True:
    A, B = map(int, sys.stdin.readline().rstrip().split())
    
    if A == 0 and B == 0:
        break
    elif B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")
