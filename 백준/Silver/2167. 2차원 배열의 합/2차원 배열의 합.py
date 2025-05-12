def solution():
    n, m = map(int, input().split())
    maps = list()

    for _ in range(n):
        maps.append(list(map(int, input().split())))

    sum_all = [[0] * (m+1) for _ in range(n+1)]

    for idx in range(n):
        for jdx in range(m):
            sum_all[idx+1][jdx+1] = sum_all[idx][jdx+1] + sum_all[idx+1][jdx] - sum_all[idx][jdx] + maps[idx][jdx]

    k = int(input())

    for _ in range(k):
        i, j, x, y = map(int, input().split())
        answer = sum_all[x][y] - sum_all[i-1][y] - sum_all[x][j-1] + sum_all[i-1][j-1]

        print(answer)


solution()