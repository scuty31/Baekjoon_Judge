"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""

T = int(input())
A = []
B = []

for i in range(T):
    n, m = map(int, input().split())
    A.append(n)
    B.append(m)

for i in range(T):
    print(A[i] + B[i])
