"""
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
"""

answer = []
A = list(input().split())
B = list(input().split())
C = list(input().split())

if A[0] == B[0]:
    answer.append(C[0])
elif B[0] == C[0]:
    answer.append(A[0])
else:
    answer.append(B[0])

if A[1] == B[1]:
    answer.append(C[1])
elif B[1] == C[1]:
    answer.append(A[1])
else:
    answer.append(B[1])

print(' '.join(answer))
