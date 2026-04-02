from collections import deque

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

a = [ ]  #кредиты
b = [ ] #лимиты банков

n = len(a)
S, T = 0, 2 * n + 1      # Источник и сток
unlim_float = sum(a)

G =  [[0] * (T+1) for _ in range(T+1)]
for i in range(n):
    G[S][i + 1] = a[i]
for j in range(n):
    G[n + 1 + j][T] = b[j]
for i in range(n):
    for j in range(n):
        G[i + 1][n + 1 + j] = unlim_float

max_flow = edmonds_karp(G, S, T)
if max_flow == sum(a):
    print('YES')
else:
    print("No")