"""
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.

이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.

이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
"""

import sys

width = [[0 for _ in range(100)] for _ in range(100)]
count = 0
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    for i in range(10):
        for j in range(10):
            width[x-1+i][y-1+j] = 1

for k in range(len(width)):
    count += sum(width[k])

print(count)
