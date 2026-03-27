from collections import deque

M = int(input())
G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = int(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    if v2 in G:
        G[v2][v1] = 0
    else:
        G[v2] = {v1:0}

def bfs(G, start, finish, dist, parent):
    queue = deque([start])
    dist[start] = 0
    while queue:
        current = queue.popleft()
        for i in G[current]:
            if dist[i] is None and G[current][i] > 0:
                queue.append(i)
                dist[i] = dist[current] + 1
                parent[i] = current
                if i == finish:
                    return True
    return False

def edmonds_karp(G, start, finish):
    left_G = {u: {v: w for v, w in adj.items()} for u, adj in G.items()}
    max_flow = 0
    n = len(G)

    while True:
        dist = {node: None for node in G}
        parent = {node: None for node in G}
        if not bfs(left_G, start, finish, dist, parent):
            break

        path_flow = float('inf')
        s = finish
        while s != start:
            path_flow = min(path_flow, left_G[parent[s]][s])
            s = parent[s]

        v = finish
        while v != start:
            u = parent[v]
            left_G[u][v] -= path_flow
            if v not in left_G:
                left_G[v] = {}
            if u not in left_G[v]:
                left_G[v][u] = 0
            left_G[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow