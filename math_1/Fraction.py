"""
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
"""

import sys

N = int(sys.stdin.readline().rstrip())
idx = 1
k = 1

while(N>=idx+k):
    idx += k
    k += 1

if k % 2 == 0:
    print("{}/{}".format(1+(N-idx), k-(N-idx)))
else:
    print("{}/{}".format(k-(N-idx), 1+(N-idx)))
