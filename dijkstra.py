def input_edges_list():
    N = int(input("Количество вершин:"))
    M = int(input("Количество рёбер:"))
    g = [[float('+inf')]*N for i in range(N)]
    for i in range(M):
        a, b, weight = input().split()
        a, b = int(a), int(b)
        weight = float(weight)
        g[a][b] = weight
        g[b][a] = weight
    for i in range(N):
        g[i][i] = 0  # условно -- петли нулевой длины
    return g

def print_graph_matrix(g):
    N = len(g)
    for i in range(N):
        print(*g[i], sep='\t')
    print()
    

def floyd_warshall(g):
    N = len(g)
    f = [[[None]*N for i in range(N)]
         for k in range(N+1)]
    # копирую крайний случай:
    for i in range(N):
        for j in range(N):
            f[0][i][j] = g[i][j]
    # динамическое программирование
    for k in range(N):
        for i in range(N):
            for j in range(N):
                f[k+1][i][j] = min(f[k][i][j],
                                   f[k][i][k] + f[k][k][j])
    return f[N]


def dijkstra(graph, start):
    N = len(graph)
    distance = [float('+inf')]*N
    distance[start] = 0
    used = [False]*N
    while True:
        current = -1
        min_distance = float('+inf')
        for i in range(N):
            if not used[i] and distance[i] < min_distance:
                current = i
                min_distance = distance[i]
        used[current] = True
        # больше нет вершин до которых вообще реально добраться
        if current == -1:break
        # укорачиваю пути к соседям:
        for neighbour in range(N):
            alt_distance = distance[current] + graph[current][neighbour]
            if alt_distance < distance[neighbour]:
                distance[neighbour] = alt_distance
    return distance

g = input_edges_list()
print_graph_matrix(g)
f = floyd_warshall(g)
print_graph_matrix(f)

for start in range(len(g)):
    d = dijkstra(g, start)
    print(*d, sep='\t')
    
