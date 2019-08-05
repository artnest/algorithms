with open("input.txt", "r") as fin:
    n = int(fin.readline())
    p = [0 for i in range(n)]

    i = 1
    for line in fin.readlines():
        indices = [i for i, j in enumerate(line.split()) if j == "1"]
        for j in indices:
            p[j] = i
        i += 1

with open("output.txt", "w") as fout:
    p_to_file = " ".join([str(i) for i in p])
    fout.write(p_to_file)
