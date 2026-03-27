from sys import exit

parent = list(range(1001))
rank = [0] * 1001

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return x

def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

n, m, p = map(int, input().split())

h = set()
if p > 0:
    h = set(map(int, input().split()))

safe = set(range(1, n + 1)) - h

edges = []
for _ in range(m):
    x, y, l = map(int, input().split())
    edges.append((l, x, y))

if n == 1:
    print(0)
    exit()

if n == 2:
    if edges:
        print(min(e[0] for e in edges))
    else:
        print(-1)
    exit()

if len(safe) == 0:
    print(-1)
    exit()

edges.sort()
cost = 0
count = 0
h_connected = set()

for l, x, y in edges:
    if x in safe and y in safe:
        if union(x, y):
            cost += l
            count += 1

for l, x, y in edges:
    if x in h and y in safe:
        if x not in h_connected:
            if union(x, y):
                cost += l
                h_connected.add(x)
                count += 1
    elif y in h and x in safe:
        if y not in h_connected:
            if union(x, y):
                cost += l
                h_connected.add(y)
                count += 1

if count < n - 1 or len(h_connected) < len(h):
    print(-1)
else:
    print(cost)