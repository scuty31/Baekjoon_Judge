"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1):
    print(" "*(N-i) + "*"*i +"*"*(i-1))

for j in range(1, N):
    print(" "*j + "*"*(N-j) + "*"*(N-j-1))
