import math

def bellman_ford(G,start):
    dist = {i: float("inf") for i in G}
    dist[start] = 0
    for i in range(n):
        updated = False
        for v1 in G:
            for v2, weight in G[v1].items():
                if dist[v2] > dist[v1] + weight:
                    dist[v2] = dist[v1] + weight
                    updated = True
                    if i == n - 1:
                        return True
        if not updated:
            break
    return False

G= {}
n = int(input())
for i in range(n):
    v1,v2,w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2] = -math.log(w)
    else:
        G[v1] = {v2: -math.log(w)}
if bellman_ford(G,0):
    print("Скам сработает)))")
else:
    print("Скама нету(((")