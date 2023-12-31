"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""

import sys

N = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
factor_bool = True
count = 0

for i in num:
    if i > 1:
        factor_bool = True

        for j in range(2, int(i**(1/2))+1):
            if i % j == 0:
                factor_bool = False
                break
        
        if factor_bool:
            count += 1

print(count)
