def solution():
    n, k = map(int, input().split())
    temperate = list(map(int, input().split()))

    max_tem = sum(temperate[:k])
    now_tem = max_tem

    j = k
    for i in range(1, n-k+1):
        now_tem -= temperate[i-1]
        now_tem += temperate[j]

        max_tem = max(max_tem, now_tem)

        j += 1

    return max_tem


print(solution())