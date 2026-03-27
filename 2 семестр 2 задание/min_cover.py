def dfs(G, visited, matching, v):
    if v in visited:
        return False
    visited.add(v)
    for to in G[v]:
        if matching[to] is None or dfs(G, visited, matching, matching[to]):
            matching[to] = v
            return True
    return False


def Kuhn(G, half):
    matching = {i: None for i in G}
    for i in G:
        visited = set()
        if matching[i] is None:
            dfs(G, visited, matching, i)
    return matching


def min_cover(G, half):
    matching = kuhn(G, half)
    cover = set()
    covered = set()

    for right, left in matching.items():
        if left is not None:
            cover.add((left, right))
            covered.add(left)
            covered.add(right)

    for v in G:
        if v not in covered:
            for i in G[v]:
                cover.add((v, i))
                covered.add(v)
                covered.add(i)
                break

    return cover