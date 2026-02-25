#данная версия написана для не ориентированного графа

def check_euler(G):
    visited = []
    euler_path = []
    potential_start = []

    def dfs(G, parent, v, visited):
        for u in G[v]:
            if [v, u] not in visited and [u, v] not in visited:
                visited.append([v, u])
                dfs(G, v, u, visited)
        euler_path.append([parent, v])

    for i in range(len(G)):
        if len(G[i]) % 2 == 1:
            potential_start.append(i)
    if len(potential_start) == 0:
        print("Эйлерова пути нет, но вероятно есть эйлеров цикл")
    if len(potential_start) > 2 or len(potential_start) == 1:
        print("Ни эйлерова пути, ни цикла тут нет")
    if len(potential_start) == 2:
        dfs(G, potential_start[1], potential_start[1], visited)
        print("Эйлеров путь:", *euler_path[::-1])



G = {0:{1,2},1:{0,2,5,3},2:{0,1,5,4},3:{1,5,4},4:{3,5,2},5:{1,2,3,4}}

check_euler(G)