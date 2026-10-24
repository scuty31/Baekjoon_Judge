def solution(commands):
    answer = []
    parent = list(range(2500))
    value = [""] * 2500

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            v = value[ra] if value[ra] else value[rb]
            parent[rb] = ra
            value[ra] = v

    def cell(r, c):
        return (int(r) - 1) * 50 + (int(c) - 1)

    for command in commands:
        cmd = command.split()
        if cmd[0] == "UPDATE" and len(cmd) == 4:
            value[find(cell(cmd[1], cmd[2]))] = cmd[3]
        elif cmd[0] == "UPDATE":
            for i in range(2500):
                p = find(i)
                if value[p] == cmd[1]:
                    value[p] = cmd[2]
        elif cmd[0] == "MERGE":
            union(cell(cmd[1], cmd[2]), cell(cmd[3], cmd[4]))
        elif cmd[0] == "UNMERGE":
            a = cell(cmd[1], cmd[2])
            p = find(a)
            v = value[p]
            members = [i for i in range(2500) if find(i) == p]
            for i in members:
                parent[i] = i
                value[i] = ""
            value[a] = v
        else:
            v = value[find(cell(cmd[1], cmd[2]))]
            answer.append(v if v else "EMPTY")
    return answer