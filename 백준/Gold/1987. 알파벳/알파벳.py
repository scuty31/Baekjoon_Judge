dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(r, c, maps, visited, x, y, depth):
    # 현재 횟수를 이용해 answer 업데이트
    answer = depth

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # map을 벗어나면 continue
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue

        # bit and로 방문
        bit = 1 << (ord(maps[nx][ny]) - ord('A'))

        # bit or로 추가, 재귀 후 or로 제거
        if visited & bit:
            continue

        answer = max(answer, dfs(r, c, maps, visited | bit, nx, ny, depth + 1))

    return answer


def solution():
    r, c = map(int, input().split())
    maps = list()

    for _ in range(r):
        maps.append(list(input()))

    # bitmask 사용
    start_bit = 1 << (ord(maps[0][0]) - ord('A'))

    answer = dfs(r, c, maps, start_bit, 0, 0, 1)

    return answer


print(solution())