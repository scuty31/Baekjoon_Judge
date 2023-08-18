"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
"""

import sys

N = int(input())

for i in range(2, int(N**(1/2))+2): 
    while (N%i == 0):
        print(i)

        N //= i
if N != 1:
    print(N)
