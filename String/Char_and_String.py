"""
단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.
"""

import sys

S = sys.stdin.readline().rstrip()
i = int(sys.stdin.readline().rstrip())

print(S[i-1])
