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

    for k in range(N):
        for i in range(N):
            for j in range(N):
                f[k+1][i][j] = min(f[k][i][j],
                                   f[k][i][k] + f[k][k][j])

    return f[N]

g = input_edges_list()
print_graph_matrix(g)
f = floyd_warshall(g)
print_graph_matrix(f)
