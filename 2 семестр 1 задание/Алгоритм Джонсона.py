import heapq
def bellman_ford(G,start):
    d = {i: float("inf") for i in G}
    d[start] = 0
    for i in range(len(G)-1):
        for node1 in d:
            for node2 in G[node1]:
                if d[node2] > d[node1] + G[node1][node2]:
                    d[node2] = d[node1] + G[node1][node2]
    return d

def dijkstra2(G,start):
    distances = {i: float("inf") for i in G}
    distances[start] = 0
    h = [(0,start)]
    while h:
        cur_dist , cur_node = heapq.heappop(h)
        if cur_dist >distances[cur_node]:
            continue
        for neighbor in G[cur_node]:
            distance = cur_dist + G[cur_node][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(h, (distance, neighbor))
    return distances

M = int(input())
G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2: w}


ver = list(G.keys())
G["S"] = {ver[0]:0}
for i in ver[1:]:
    G["S"][i] = 0
poten = bellman_ford(G, "S")
del G["S"]

for i in G.keys():
    for j in G[i].keys():
        G[i][j] = G[i][j] + poten[i] - poten[j]
start = input("Введите вершину от которой считать ")
print(dijkstra2(G, start))
