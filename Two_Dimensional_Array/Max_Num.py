"""
9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
"""

import sys

n = 9
max_num_coor = [1,1]
max_num = 0

for idx in range(n):
    matrix = list(map(int, sys.stdin.readline().rstrip().split()))
    num = max(matrix)
    if max_num < num:
        max_num = num
        max_num_coor = [idx+1, matrix.index(num)+1]

print(max_num)
print(max_num_coor[0], max_num_coor[1])
