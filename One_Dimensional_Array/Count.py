"""
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
"""

import sys

N = int(sys.stdin.readline().rstrip())
num = sys.stdin.readline().rstrip().split()
V = sys.stdin.readline().rstrip()

print(num.count(V))
