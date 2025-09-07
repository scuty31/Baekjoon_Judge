from collections import deque


def solution():
    n = int(input())
    visited = [-1 for _ in range(n+1)]

    if n <= 5:
        if n == 2 or n == 5:
            return 1

        elif n == 1 or n == 3:
            return -1

        elif n == 4:
            return 2

    visited[2] = 1
    visited[5] = 1

    q = deque()
    q.append(2)
    q.append(5)

    while q:
        num = q.popleft()

        if num + 2 > n:
            continue

        if visited[num+2] == -1:
            visited[num+2] = visited[num] + 1
            q.append(num + 2)

        elif visited[num+2] > visited[num] + 1:
            visited[num+2] = visited[num] + 1
            q.append(num + 2)

        if num + 5 > n:
            continue

        if visited[num+5] == -1:
            visited[num+5] = visited[num] + 1
            q.append(num + 5)

        elif visited[num+5] > visited[num] + 1:
            visited[num+5] = visited[num] + 1
            q.append(num + 5)

    return visited[n]


print(solution())