def next_sum(level, now_idx):
    global cnt, now_sum

    if now_sum == s:
        cnt += 1
    if level > n:
        return

    for j in range(now_idx+1, n):
        if visited[j]:
            continue
        visited[j] = True
        now_sum += arr[j]

        next_sum(level+1, j)

        visited[j] = False
        now_sum -= arr[j]


n, s = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * n

cnt = 0
now_sum = 0

for i in range(n):
    visited[i] = True
    now_sum += arr[i]

    next_sum(1, i)

    visited[i] = False
    now_sum -= arr[i]

print(cnt)