"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""

import sys
T = int(sys.stdin.readline().rstrip())


for i in range(1, T+1):
    N = sys.stdin.readline().rstrip().split()
    print("Case #"+str(i)+":", int(N[0]) + int(N[1]))
