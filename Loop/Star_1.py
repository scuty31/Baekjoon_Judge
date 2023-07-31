"""
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
"""

import sys
T = int(sys.stdin.readline().rstrip())

for i in range(1, T+1):
    print("*"*i)
