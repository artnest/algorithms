def dfs(v):
    if used[v]:
        return

    used[v] = True
    for w in adj[v]:
        dfs(w)


with open("input.txt", "r") as fin:
    n = int(fin.readline())
    m = int(fin.readline())
    adj = {i: [] for i in range(1, n + 1)}
    for edge in fin.readlines():
        u, v = edge.strip().split()
        u = int(u)
        v = int(v)
        adj[u].append(v)
        adj[v].append(u)

used = [False] * (n + 1)
components = 0

for vertex in range(1, n + 1):
    if not used[vertex]:
        dfs(vertex)
        components += 1

with open("output.txt", "w") as fout:
    edges_to_connected = components - 1
    fout.write(str(edges_to_connected))
