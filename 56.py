with open("input.txt", "r") as fin:
    n = int(fin.readline())
    vertices = fin.readline().strip().split()
    for i, vertex in enumerate(vertices):
        vertices[i] = int(vertex)

    heap_ready = True
    try:
        for i, vertex in enumerate(vertices):
            if not vertices[i] <= vertices[2 * i + 1]:
                heap_ready = False
                break
            if not vertices[i] <= vertices[2 * i + 2]:
                heap_ready = False
                break
    except IndexError:
        pass

with open("output.txt", "w") as fout:
    if heap_ready:
        fout.write("Yes")
    else:
        fout.write("No")
