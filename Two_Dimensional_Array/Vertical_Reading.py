"""
칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.
"""

import sys

n = 5
s_list = []
s = ''

for idx in range(n):
    s_list.append(sys.stdin.readline().rstrip())

max_len = len(max(s_list, key=len))

for i in range(max_len):
    for j in range(n):
        if len(s_list[j]) > i:
            s += s_list[j][i]

print(s)
