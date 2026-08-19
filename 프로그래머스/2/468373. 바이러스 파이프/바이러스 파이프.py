from collections import deque


def check_infection(n, infection, graph, open_type):
    next_infection = set()
    q = deque()
    visited = [False] * (n+1)

    for i in infection:
        visited[i] = True
        q.append(i)
        next_infection.add(i)

    while q:
        node = q.popleft()

        for next_node, types in graph[node]:
            if types == open_type and not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
                next_infection.add(next_node)

    return frozenset(next_infection)


def solution(n, infection, edges, k):
    answer = 0
    infection_queue = deque([[infection]])
    graph = [[] for _ in range(n+1)]

    for x, y, types in edges:
        graph[x].append((y, types))
        graph[y].append((x, types))

    visited = set()
    for _ in range(k):
        for _ in range(len(infection_queue)):
            now_infection = infection_queue.popleft()

            for open_type in range(1, 4):
                next_infection = check_infection(n, now_infection, graph, open_type)
                answer = max(answer, len(next_infection))

                if next_infection in visited:
                    continue

                infection_queue.append(next_infection)
                visited.add(next_infection)

    return answer