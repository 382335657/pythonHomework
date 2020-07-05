def dijstra(start, end, graph, vertex):
    visited = [0] * vertex
    visited[start] = 1
    used = []
    used.append((start, 0, 0))
    while True:
        idx = -1
        shortest = float("inf")
        dis = float("inf")
        dangerous = float("inf")
        for i in range(0,vertex):
            if not visited[i]:
                for v in used:
                    if i in graph[v[0]]:
                        dis = v[1] + distance[(v[0], i)]
                    if dis < shortest:
                        dangerous=max(v[2],distance[(v[0],i)])
                        shortest = dis
                        idx = i
        if idx==-1:
            break
        else:
            if idx == end:
                return dangerous
            else:
                visited[idx] = 1
                used.append((idx, shortest, dangerous))
    return -1


if __name__ == '__main__':
    distance = {}
    graph = []
    vertex, operate = map(int, input().split(" "))
    res=[]
    ops=[]
    for i in range(vertex):
        graph.append([])
    for i in range(operate):
        op = list(map(int, input().split(" ")))
        ops.append(op)
        if op[0] == 0:
            graph[op[1]].append(op[2])
            graph[op[2]].append(op[1])
            distance.setdefault((op[1], op[2]), op[3])
            distance.setdefault((op[2], op[1]), op[3])
        elif op[0] == 1:
            graph[op[1]].remove(op[2])
            graph[op[2]].remove(op[1])
        elif op[0] == 2:
            res.append(dijstra(op[1], op[2], graph, vertex))
    else:
        for r in res:
            print(r)