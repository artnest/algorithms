with open("input.txt", "r") as fin:
    n = int(fin.readline().split()[0])
    vertices = {i: [] for i in range(1, n + 1)}
    for edge in fin.readlines():
        u, v = edge.strip().split()
        u = int(u)
        v = int(v)
        vertices[u].append(v)
        vertices[v].append(u)

with open("output.txt", "w") as fout:
    for v in vertices.values():
        values = " ".join([str(i) for i in v])
        entry = " ".join([str(len(v)), values])
        fout.write(entry + "\n")
