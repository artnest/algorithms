with open("input.txt", "r") as fin:
    n = int(fin.readline())
    p = [0 for i in range(n)]
    for line in fin.readlines():
        k, i = line.strip().split()
        p[int(i) - 1] = int(k)

with open("output.txt", "w") as fout:
    p_to_file = " ".join([str(i) for i in p])
    fout.write(p_to_file)
